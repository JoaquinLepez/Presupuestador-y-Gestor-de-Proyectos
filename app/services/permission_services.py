from app.repositories import PermissionRepository

repository = PermissionRepository()

class PermissionService:

    def save(self, permission):
        return repository.save(permission)
    
    def update(self, permission, id):
        return repository.update(permission, id)
    
    def delete(self, permission):
        return repository.delete(permission)
    
    def all(self):
        return repository.all()
    
    def find(self, id):
        return repository.find(id)