from app import db
from app.models.relations import roles_permissions

class Role(db.Model):
    __tablename__ = 'roles'
    # Atributos propios
    id: int = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name: str = db.Column(db.String(80), nullable = False)
    
    # Relaciones con otras tablas
    # Permission M:N
    permissions = db.relationship('Permission', secondary = roles_permissions, back_populates = 'roles')
    # UserRoleTeam 1:N
    users_teams = db.relationship('UserRoleTeam', back_populates = 'role')
    
    