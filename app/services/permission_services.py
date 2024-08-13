from typing import List
from app.models import Permission
from app.repositories import PermissionRepository

repository = PermissionRepository()

class PermissionService:

    def save(self, permission: Permission) -> Permission:
        return repository.save(permission)
    
    def update(self, permission: Permission, id: int) -> Permission:
        return repository.update(permission, id)
    
    def delete(self, permission: Permission) -> None:
        return repository.delete(permission)
    
    def all(self) -> List[Permission]:
        return repository.all()
    
    def find(self, id: int) -> Permission:
        return repository.find(id)