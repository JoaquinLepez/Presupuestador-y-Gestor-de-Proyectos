from app import db

# Tablas Intermedias
users_tasks = db.Table('users_tasks', db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key = True), db.Column('task_id', db.Integer, db.ForeignKey('tasks.id'), primary_key = True))
users_teams = db.Table('users_teams', db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key = True), db.Column('team_id', db.Integer, db.ForeignKey('teams.id'), primary_key = True))