from flask import request, jsonify, current_app as app
from . import db
from .models import chambreType, chambre, Reservation
from .schemas import chambreTypeSchema, chambreSchema, ReservationSchema

chambre_type_schema = chambreTypeSchema()
chambre_schema = chambreSchema()
reservation_schema = ReservationSchema()
reservation_list_schema = ReservationSchema(many=True)

@app.route('/reservations', methods=['GET', 'POST'])
def manage_reservations():
    if request.method == 'GET':
        reservations = Reservation.query.all()
        return reservation_list_schema.jsonify(reservations)
    
    if request.method == 'POST':
        data = request.json
        
        # Récupérer la chambre
        chambr = chambre.query.filter_by(id=data.get('chambre_id')).first()

        # Vérifier si la chambre existe et est disponible
        if not chambr or chambr.is_rented:
            return jsonify({"message": "cette chambre n'est pas disponible"}), 400

        # Accéder au coût du type de chambre
        cout_par_jour = chambr.type.cout
        total_cout = cout_par_jour * data.get('days')

        # Créer la nouvelle réservation
        new_reservation = Reservation(
            client_nom=data.get('client_nom'),
            client_prenom=data.get('client_prenom'),
            days=data.get('days'),
            total_cout=total_cout,
            chambre_id=chambr.id
        )

        # Marquer la chambre comme louée
        chambr.is_rented = True

        # Sauvegarder dans la base de données
        db.session.add(new_reservation)
        db.session.commit()

        return reservation_schema.jsonify(new_reservation), 201



@app.route('/reservations/<int:id>', methods=['PUT', 'DELETE'])
def modify_delete_reservation(id):
    reservation = Reservation.query.get_or_404(id)

    if request.method == 'PUT':
        data = request.json
        reservation.client_nom = data.get('client_nom', reservation.client_nom)
        reservation.client_prenom = data.get('client_prenom', reservation.client_prenom)
        reservation.days = data.get('days', reservation.days)
        reservation.total_cout = reservation.chambre.type.cout * reservation.days
        db.session.commit()
        return reservation_schema.jsonify(reservation)

    if request.method == 'DELETE':
        chambre = reservation.chambre
        chambre.is_rented = False
        db.session.delete(reservation)
        db.session.commit()
        return '', 204

@app.route('/chambre_types/<int:type_id>/count', methods=['GET'])
def count_rented_chambres(type_id):
    rented_count = chambre.query.filter_by(type_id=type_id, is_rented=True).count()
    return jsonify({"rented_chambres": rented_count})

@app.route('/chambre_stats', methods=['GET'])
def get_chambre_stats():
    chambre_types = chambreType.query.all()
    
    chambre_stats = []
    for chambre_type in chambre_types:
        chambres_louees = chambre.query.filter_by(type_id=chambre_type.id, is_rented=True).count()
        chambres_total = chambre_type.disponible 
        chambres_libres = chambres_total - chambres_louees
        
        chambre_stats.append({
            'type_id': chambre_type.id,
            'description': chambre_type.description,
            'chambres_louees': chambres_louees,
            'chambres_libres': chambres_libres,
            'chambres_total': chambres_total,
        })
    
    return jsonify(chambre_stats)


@app.route('/chambres', methods=['GET', 'POST'])
def manage_chambres():
    if request.method == 'GET':
        chambres = chambre.query.all()
        return jsonify(chambre_schema.dump(chambres, many=True))
    
    if request.method == 'POST':
        data = request.json
        new_chambre = chambre(
            chambre_number=data.get('chambre_number'),
            type_id=data.get('type_id'),
            is_rented=False  # par défaut, la chambre n'est pas louée
        )
        db.session.add(new_chambre)
        db.session.commit()
        return chambre_schema.jsonify(new_chambre), 201
    
@app.route('/liberer_chambre/<int:reservation_id>', methods=['POST'])
def liberer_chambre(reservation_id):
    # Récupérer la réservation
    reservation = Reservation.query.get(reservation_id)
    
    if not reservation:
        return jsonify({"error": "Réservation non trouvée"}), 404
    
    # Récupérer la chambre associée à la réservation
    chambrer = chambre.query.get(reservation.chambre_id)
    
    if not chambrer:
        return jsonify({"error": "Chambre non trouvée"}), 404
    
    # Marquer la chambre comme non louée
    chambrer.is_rented = False
    
    # Sauvegarder les modifications dans la base de données
    db.session.commit()
    
    return jsonify({"message": "La chambre a été libérée avec succès"}), 200


import random
import string

@app.route('/chambre_types', methods=['GET', 'POST'])
def manage_chambre_types():
    if request.method == 'GET':
        chambre_types = chambreType.query.all()
        return jsonify(chambre_type_schema.dump(chambre_types, many=True))
    
    if request.method == 'POST':
        data = request.json
        
        # Créer le nouveau type de chambre
        new_type = chambreType(
            description=data.get('description'),
            cout=data.get('cout'),
            disponible=data.get('disponible')
        )
        db.session.add(new_type)
        db.session.commit()
        
        # Créer automatiquement les chambres en fonction du nombre de chambres disponibles
        for i in range(new_type.disponible):
            chambre_number = generate_chambre_number()
            new_chambre = chambre(
                chambre_number=chambre_number,
                type_id=new_type.id,
                is_rented=False  # Par défaut, la chambre n'est pas louée
            )
            db.session.add(new_chambre)
        
        db.session.commit()
        return chambre_type_schema.jsonify(new_type), 201

def generate_chambre_number():
    # Générer un numéro de chambre unique avec une combinaison de lettres et chiffres
    letters = ''.join(random.choices(string.ascii_uppercase, k=2))
    digits = ''.join(random.choices(string.digits, k=4))
    return letters + digits



