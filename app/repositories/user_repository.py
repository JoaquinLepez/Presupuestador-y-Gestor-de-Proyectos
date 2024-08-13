from typing import List, Optional
from app.models import User
from app import db

class UserRepository:

    def save(self, user: User) -> User:
        db.session.add(user)
        db.session.commit()
        return user
    
    def update(self, user: User, id: int) -> User:
        entity = self.find(id)
        entity.username = user.username
        entity.email = user.email
        db.session.add(entity)
        db.session.commit()
        return entity
    
    def delete(self, user_id: int) -> bool:
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True  # Solo devolver True si el usuario fue eliminado.
        return False  # Devolver False si el usuario no existe.
    
    def all(self) -> List[User]:
        users = db.session.query(User).all()
        return users

    def find(self, id: int) -> Optional[User]:
        if id is None or id == 0:
            return None
        try:
            return db.session.query(User).filter(User.id == id).one()
        except:
            return None
        
    def find_by_username(self, username: str) -> Optional[User]:
        return db.session.query(User).filter(User.username == username).one_or_none()
    
    def find_by_email(self, email: str) -> List[User]:
        return db.session.query(User).filter(User.email.like(f'%{email}%')).all()