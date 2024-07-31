from app import db
from app.models import Permission

class PermissionRepository:

    def save(self, permission):
        db.session.add(permission)
        db.session.commit()
        return permission
    
    def update(self, permission, id):
        entity = self.find(id)
        entity.name = permission.name
        db.session.add(entity)
        db.session.commit()
        return entity

    def delete(self, permission):
        db.session.delete(permission)
        db.session.commit()

    def all(self):
        permissions = db.session.query(Permission).all()
        return permissions
    
    def find(self, id):
        if id is None or id == 0:
            return None
        try:
            return db.session.query(Permission).filter(Permission.id == id).one()
        except:
            return None
        