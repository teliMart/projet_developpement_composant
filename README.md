# projet_developpement_composant
# Système de Gestion de Réservations d'Hôtel
Ce projet est un système de gestion de réservations d'hôtel basé sur Flask, permettant de gérer les types de chambres, les chambres, et les réservations dans un hôtel. Le système utilise une base de données MySQL pour stocker les données et fournit une API RESTful pour interagir avec ces données.

# Structure du Projet

├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│   └── db_utils.py
├── run.py
├── requirements.txt
└── README.md

# Fichiers
pp/config.py : Fichier de configuration de l'application. Il inclut l'URI de la base de données et d'autres configurations.
app/models.py : Définit les modèles SQLAlchemy pour chambreType, chambre, et Reservation.
app/routes.py : Contient les routes Flask pour gérer les réservations, les chambres, et les types de chambres.
app/schemas.py : Définit les schémas Marshmallow pour sérialiser et désérialiser les instances des modèles.
run.py : Point d'entrée pour exécuter l'application Flask.
requirements.txt : Liste des dépendances Python nécessaires pour exécuter l'application.

# Prérequis
Avant d'exécuter l'application, assurez-vous d'avoir installé les éléments suivants :

Python 3.x
MySQL
Flask
pip

# Installation
Clonez le dépôt :
git clone https://github.com/teliMart/projet_developpement_composant.git
cd hotel-reservation-management

# Configurez un environnement virtuel (optionnel mais recommandé) :
python -m venv venv
source venv/bin/activate   # Sur Windows : venv\Scripts\activate

# Installez les packages Python requis :
pip install -r requirements.txt

# Configurez la base de données MySQL :
Créez une base de données nommée db_hotel.
Mettez à jour l'URI de la base de données dans app/config.py si nécessaire.

# Exécutez l'application :
python run.py

# Points de Terminaison de l'API
Types de Chambres
GET /chambre_types : Récupérer tous les types de chambres.
POST /chambre_types : Créer un nouveau type de chambre.
Chambres
GET /chambres : Récupérer toutes les chambres.
POST /chambres : Créer une nouvelle chambre.

# Réservations
GET /reservations : Récupérer toutes les réservations.
POST /reservations : Créer une nouvelle réservation.
PUT /reservations/<int:id> : Mettre à jour une réservation.
DELETE /reservations/<int:id> : Supprimer une réservation.
POST /liberer_chambre/<int:reservation_id> : Libérer une chambre réservée.

# Statistiques
GET /chambre_types/<int:type_id>/count : Obtenir le nombre de chambres louées pour un type spécifique.
GET /chambre_stats : Obtenir des statistiques sur la disponibilité et l'occupation des chambres.

# Configuration
L'application est configurée via le fichier app/config.py. Assurez-vous que l'URI de la base de données pointe vers votre instance MySQL.

# Exécution des Tests
Pour tester l'API, vous pouvez utiliser des outils comme Postman ou cURL pour envoyer des requêtes HTTP aux points de terminaison de l'API.
