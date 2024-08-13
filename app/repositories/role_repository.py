from typing import List
from app import db
from app.models import Role

class RoleRepository:

    def save(self, role: Role) -> Role:
        db.session.add(role)
        db.session.commit()
        return role
    
    def update(self, role: Role, id: int) -> Role:
        entity = self.find(id)
        entity.name = role.name
        db.session.add(entity)
        db.session.commit()
        return entity

    def delete(self, role: Role) -> None:
        db.session.delete(role)
        db.session.commit()

    def all(self) -> List[Role]:
        roles = db.session.query(Role).all()
        return roles
    
    def find(self, id: int) -> Role:
        if id is None or id == 0:
            return None
        try:
            return db.session.query(Role).filter(Role.id == id).one()
        except:
            return None