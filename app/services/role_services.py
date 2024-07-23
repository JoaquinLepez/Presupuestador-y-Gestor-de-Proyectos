from app.repositories import RoleRepository

repository = RoleRepository()

class RoleService:

    def save(self, role):
        return repository.save(role)
    
    def update(self, role, id):
        return repository.update(role, id)
    
    def delete(self, role):
        return repository.delete(role)
    
    def all(self):
        return repository.all()
    
    def find(self, id):
        return repository.find(id)
    
