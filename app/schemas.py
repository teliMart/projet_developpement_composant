from . import ma
from .models import chambreType, chambre, Reservation

class chambreTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = chambreType
        include_relationships = True
        load_instance = True

class chambreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = chambre
        include_fk = True
        load_instance = True

class ReservationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Reservation
        include_fk = True
        load_instance = True
