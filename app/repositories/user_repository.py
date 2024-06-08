from app.models import User
from app import db

class UserRepository:

    def save(self, user):
        db.session.add(user)
        db.session.commit()
        return user
    
    def update(self, user, id):
        entity = self.find(id)
        entity.username = user.username
        entity.email = user.email
        db.session.add(entity)
        db.session.commit()
        return entity
    
    def delete(self, user):
        db.session.delete(user)
        db.session.commit()
    
    def all(self):
        users = db.session.query(User).all()
        return users

    def find(self, id):
        if id is None or id == 0:
            return None
        try:
            return db.session.query(User).filter(User.id == id).one()
        except:
            return None
        
    def find_by_username(self, username):
        return db.session.query(User).filter(User.username == username).one_or_none()
    
    def find_by_email(self, email):
        return db.session.query(User).filter(User.email.like(f'%{email}%')).all()


