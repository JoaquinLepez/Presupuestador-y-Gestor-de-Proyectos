from app import db
from app.models.relations import roles_permissions

class Permission(db.Model):
    __tablename__ = 'permissions'
    # Atributos propios
    id: int = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name: str = db.Column(db.String(80), nullable = False)
    
    # Relaciones con otras tablas
    # Role M:N
    roles = db.relationship('Role', secondary = roles_permissions, back_populates = 'permissions')
    
    