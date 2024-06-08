from app.repositories import UserRepository
from app.services import Security

repository = UserRepository()

class UserService:

    def save(self, user):
        user.password = Security.generate_password(user.password)
        return repository.save(user)
    
    def update(self, user, id):
        return repository.update(user, id)
    
    def delete(self, user):
        return repository.delete(user)
    
    def all(self):
        return repository.all()
    
    def find(self, id):
        return repository.find(id)
    
    def find_by_username(self, username):
        return repository.find_by_username(username)
    
    def find_by_email(self, email):
        return repository.find_by_email(email)
    
    def check_auth(self, username, password):
        user = self.find_by_username(username)
        if user is not None:
            return Security.check_password(user.password, password)
        else:
            return False
