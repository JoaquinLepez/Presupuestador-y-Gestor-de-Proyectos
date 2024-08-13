from typing import List, Optional
from app import db
from app.models import Task

class TaskRepository:

    def save(self, task: Task) -> Task:
        db.session.add(task)
        db.session.commit()
        return task
    
    def update(self, task: Task, id: int) -> Optional[Task]:
        entity = self.find(id)
        entity.name = task.name
        entity.description = task.description
        entity.start_date = task.start_date
        entity.deadline = task.deadline
        entity.priority = task.priority
        entity.difficulty = task.difficulty
        entity.state = task.state
        db.session.add(entity)
        db.session.commit()
        return entity

    def delete(self, task: Task) -> None:
        db.session.delete(task)
        db.session.commit()

    def all(self) -> List[Task]:
        tasks = db.session.query(Task).all()
        return tasks
    
    def find(self, id: int) -> Optional[Task]:
        if id is None or id == 0:
            return None
        try:
            return db.session.query(Task).filter(Task.id == id).one()
        except:
            return None
        
    def find_by_name(self, name: str) -> Optional[Task]:
        return db.session.query(Task).filter(Task.name == name).one_or_none()