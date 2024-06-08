from app import db

class UserData(db.Model):
    __tablename__ = 'users_data'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname: str = db.Column(db.String(80), nullable=False)
    lastname: str = db.Column(db.String(80), nullable=False)
    phone: str = db.Column(db.String(120), nullable=False)
    address: str = db.Column(db.String(120), nullable=False)
    city: str   = db.Column(db.String(120), nullable=False)
    country: str = db.Column(db.String(120), nullable=False)
    
    # ForeignKey de la tabla Users
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Relaciones con otras tablas
    # Users 1:1
    user = db.relationship('User', back_populates='data', uselist=False)