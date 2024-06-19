from app.repositories import Project_Repository

repository = Project_Repository()

class ProyectService:

    def save(self, proyect):
        return repository.save(proyect)
    
    def update(self, proyect, id):
        return repository.update(proyect, id)
    
    def delete(self, proyect):
        return repository.delete()
    
    def all(self):
        return repository.all()
    
    def find(self, id):
        return repository.find(id)
    
    def find_by_name(self, name):
        return repository.find_by_name(name)