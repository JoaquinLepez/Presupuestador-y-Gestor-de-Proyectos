from app.repositories import TaskRepository

repository = TaskRepository()

class TaskService:

    def save(self, task):
        return repository.save(task)
    
    def update(self, task, id):
        return repository.update(task, id)
    
    def delete(self, task):
        return repository.delete(task)
    
    def all(self):
        return repository.all()
    
    def find(self, id):
        return repository.find(id)
    
    def find_by_name(self, name):
        return repository.find_by_name(name)