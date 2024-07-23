from app import db

class UserRoleTeam(db.Model):
    __tablename__ = 'users_roles_teams'
     # Atributos Foraneos
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), primary_key = True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), primary_key = True)

    # Relaciones con otras tablas
    # User 1:N
    user = db.relationship('User', back_populates = 'teams_roles')
    # Roles 1:N
    role = db.relationship('Role', back_populates = 'users_teams')
    # Teams 1:N
    team = db.relationship('Team', back_populates = 'users_roles')
