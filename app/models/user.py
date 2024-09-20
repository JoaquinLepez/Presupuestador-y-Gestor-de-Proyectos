from app import db
from app.models.relations import users_tasks

class User(db.Model):
    __tablename__ = 'users'
    # Atributos propios
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username: str = db.Column(db.String(80), unique=True, nullable=False)
    password: str = db.Column(db.String(255), nullable=False)
    email: str = db.Column(db.String(120), unique=True, nullable=False)

    # Relaciones con otras tablas
    # Userdata 1:1
    data = db.relationship('UserData', uselist=False, back_populates='user', cascade = 'delete, delete-orphan')
    # Tasks N:M
    tasks = db.relationship('Task', secondary = users_tasks, back_populates = 'users', cascade = 'delete, delete')
    # UserRoleTeam 1:N
    teams_roles = db.relationship('UserRoleTeam', back_populates = 'user', cascade = 'delete, delete-orphan')




