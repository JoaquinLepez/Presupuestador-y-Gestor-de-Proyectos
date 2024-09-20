from app import db

class Project(db.Model):
    __tablename__ = 'projects'
    # Atributos propios
    id: int = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name: str = db.Column(db.String(80), nullable = False)
    description: str = db.Column(db.String(250), nullable = False)
    start_date: str = db.Column(db.DateTime, nullable = False)
    deadline: str = db.Column(db.DateTime, nullable = False)
    state: str = db.Column(db.String(64), nullable = False)

    # Atributos Foraneos
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))

    # Relaciones con otras tablas
    # Teams 1:1
    team = db.relationship('Team', uselist = False, back_populates = 'project')
    # Tasks 1:N
    tasks = db.relationship('Task', back_populates = 'project', cascade = 'delete, delete-orphan')
