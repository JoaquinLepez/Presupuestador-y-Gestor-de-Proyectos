from app import db
from app.models.relations import users_teams

class Team(db.Model):
    __tablename__ = 'teams'
    # Atributos propios
    id: int = db.Column(db.Integer, primary_key = True, autoincrement = True)
    team_name: str = db.Column(db.String(64), nullable = False)

    # Relaciones con otras tablas
    # Projects 1:1
    project = db.relationship('Project', uselist = False, back_populates = 'team')

    # Users M:N
    users = db.relationship('User', secondary = users_teams, back_populates = 'teams')
