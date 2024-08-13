from typing import List
from app.models import Role
from app.repositories import RoleRepository

repository = RoleRepository()

class RoleService:

    def save(self, role: Role) -> Role:
        return repository.save(role)
    
    def update(self, role: Role, id: int) -> Role:
        return repository.update(role, id)
    
    def delete(self, role: Role) -> None:
        return repository.delete(role)
    
    def all(self) -> List[Role]:
        return repository.all()
    
    def find(self, id: int) -> Role:
        return repository.find(id)