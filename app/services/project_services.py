from app.repositories import ProjectRepository

repository = ProjectRepository()

class ProjectService:

    def save(self, project):
        return repository.save(project)
    
    def update(self, project, id):
        return repository.update(project, id)
    
    def delete(self, project):
        return repository.delete(project)
    
    def all(self):
        return repository.all()
    
    def find(self, id):
        return repository.find(id)
    
    def find_by_name(self, name):
        return repository.find_by_name(name)