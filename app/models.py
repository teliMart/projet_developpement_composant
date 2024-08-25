from . import db

class chambreType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    cout = db.Column(db.Float, nullable=False)
    disponible = db.Column(db.Integer, nullable=False)
    chambres = db.relationship('chambre', backref='type', lazy=True)

class chambre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chambre_number = db.Column(db.String(50), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('chambre_type.id'), nullable=False)
    is_rented = db.Column(db.Boolean, default=False)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_nom = db.Column(db.String(100), nullable=False)
    client_prenom = db.Column(db.String(100), nullable=False)
    days = db.Column(db.Integer, nullable=False)
    total_cout = db.Column(db.Float, nullable=False)
    chambre_id = db.Column(db.Integer, db.ForeignKey('chambre.id'), nullable=False)
    chambre = db.relationship('chambre', backref='reservations')
