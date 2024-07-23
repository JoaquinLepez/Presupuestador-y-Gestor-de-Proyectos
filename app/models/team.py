from app import db

class Team(db.Model):
    __tablename__ = 'teams'
    # Atributos propios
    id: int = db.Column(db.Integer, primary_key = True, autoincrement = True)
    team_name: str = db.Column(db.String(64), nullable = False)

    # Relaciones con otras tablas
    # Projects 1:1
    project = db.relationship('Project', uselist = False, back_populates = 'team')
    # UserRoleTeam 1:N
    users_roles = db.relationship('UserRoleTeam', back_populates = 'team')
