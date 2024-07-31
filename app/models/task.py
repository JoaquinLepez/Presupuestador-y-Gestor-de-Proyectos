from app import db
from app.models.relations import users_tasks

class Task(db.Model):
    __tablename__ = 'tasks'
    # Atributos propios
    id: int = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name: str = db.Column(db.String(80), nullable = False)
    description: str = db.Column(db.String(64), nullable = False)
    start_date: str = db.Column(db.DateTime, nullable = False)
    deadline: str = db.Column(db.DateTime, nullable = False)
    priority: str = db.Column(db.String(64), nullable = False)
    difficulty: str = db.Column(db.String(64), nullable = False)
    state: str = db.Column(db.String(64), nullable = False)

    # Atributos Foraneos
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))

    # Relaciones con otras tablas
    # Projects N:1
    project = db.relationship('Project', back_populates = 'task')

    # Users M:N
    users = db.relationship('User', secondary = users_tasks, back_populates = 'tasks')
    
    