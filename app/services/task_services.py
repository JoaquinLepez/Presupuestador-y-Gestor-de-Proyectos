from app.repositories import TaskRepository
from app.models import Task
from typing import List

repository = TaskRepository()

class TaskService:

    def save(self, task: Task) -> Task:
        return repository.save(task)
    
    def update(self, task: Task, id: int) -> Task:
        return repository.update(task, id)
    
    def delete(self, task: Task) -> bool:
        return repository.delete(task)
    
    def all(self) -> List[Task]:
        return repository.all()
    
    def find(self, id: int) -> Task:
        return repository.find(id)
    
    def find_by_name(self, name: str) -> Task:
        return repository.find_by_name(name)