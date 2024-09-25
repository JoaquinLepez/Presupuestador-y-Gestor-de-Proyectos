from app.repositories import UserRepository
from app.services import SecurityManager, WerkzeugSecurity
from app.models import User
from typing import List, Optional

repository = UserRepository()

class UserService:

    def __init__(self) -> None:
        self.__security = SecurityManager(WerkzeugSecurity())

    def save(self, user: User) -> User:
        # Verificar si UserData está presente
        if not user.data:
            raise ValueError("UserData is required for creating a new user.")
        
        user.password = self.__security.generate_password(user.password)
        return repository.save(user)
    
    def update(self, user: User, id: int) -> User:
        return repository.update(user, id)
    
    def delete(self, user_id: int) -> None:
        user = repository.find(user_id)
        repository.delete(user)
    
    def all(self) -> List[User]:
        return repository.all()
    
    def find(self, id: int) -> Optional[User]:
        return repository.find(id)
    
    def find_by_username(self, username: str) -> Optional[User]:
        return repository.find_by_username(username)
    
    def find_by_email(self, email: str) -> Optional[User]:
        return repository.find_by_email(email)
    
    def check_auth(self, username: str, password: str) -> bool:
        user = self.find_by_username(username)
        if user is not None:
            return self.__security.check_password(user.password, password)
        else:
            return False