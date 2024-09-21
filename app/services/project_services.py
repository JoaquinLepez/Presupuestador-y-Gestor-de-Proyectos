from typing import List, Optional
from app.models import Project, Task
from app.repositories import ProjectRepository

repository = ProjectRepository()

class ProjectService:

    def save(self, project: Project) -> Project:
        return repository.save(project)
    
    def update(self, project: Project, id: int) -> Project:
        return repository.update(project, id)
    
    def delete(self, id_project: Project) -> None:
        project = repository.find(id_project)
        return repository.delete(project)
    
    def all(self) -> List[Project]:
        return repository.all()
    
    def find(self, id: int) -> Project:
        return repository.find(id)
    
    def find_by_name(self, name: str) -> Optional[Project]:
        return repository.find_by_name(name)
    
    def get_tasks(self, id: int) -> List[Task]:
        return repository.get_tasks(id)