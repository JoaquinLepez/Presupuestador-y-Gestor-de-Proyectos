from typing import List, Optional
from app.models import Project, Task, User
from app import db
from sqlalchemy.orm import joinedload

class ProjectRepository:

    def save(self, project: Project) -> Project:
        db.session.add(project)
        db.session.commit()
        return project
    
    def update(self, project: Project, id: int) -> Project:
        entity = self.find(id)
        if entity:
            entity.name = project.name
            entity.description = project.description
            entity.start_date = project.start_date
            entity.deadline = project.deadline
            entity.state = project.state
            db.session.add(entity)
            db.session.commit()
            return entity
        else:
            return None
    
    def delete(self, project: Project) -> None:
        db.session.delete(project)
        db.session.commit()

    def all(self) -> List[Project]:
        projects = db.session.query(Project).all()
        return projects

    def find(self, id: int) -> Optional[Project]:
        if id is None or id == 0:
            return None
        try:
            return db.session.query(Project).filter(Project.id == id).one()
        except:
            return None
        
    def find_by_name(self, name: str) -> Optional[Project]:
        return db.session.query(Project).filter(Project.name == name).one_or_none()
    
    def get_tasks(self, id: int) -> List[Task]:
        return db.session.query(Task).filter(Task.project_id == id).options(
            joinedload(Task.users).load_only(User.username, User.email),
            joinedload(Task.users).noload(User.data)).all()
