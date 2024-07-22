from app import db

# Tablas Intermedias

# User - Task
users_tasks = db.Table('users_tasks', db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key = True), db.Column('task_id', db.Integer, db.ForeignKey('tasks.id'), primary_key = True))

# User - Team
users_teams = db.Table('users_teams', db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key = True), db.Column('team_id', db.Integer, db.ForeignKey('teams.id'), primary_key = True))

# Role - Permission
roles_permissions = db.Table('roles_permissions', db.Column('role_id', db.Integer, db.ForeignKey('roles.id'), primary_key = True), db.Column('permission_id', db.Integer, db.ForeignKey('permissions.id'), primary_key = True))
