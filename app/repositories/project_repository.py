from app.models import Project
from app import db

class ProjectRepository:

    def save(self, project):
        db.session.add(project)
        db.session.commit()
        return project
    
    def update(self, project, id):
        entity = self.find(id)
        entity.name = project.name
        entity.description = project.description
        entity.start_date = project.start_date
        entity.deadline = project.deadline
        entity.state = project.state
        db.session.add(entity)
        db.session.commit()
        return entity
    
    def delete(self, project):
        db.session.delete(project)
        db.session.commit()

    def all(self):
        projects = db.session.query(Project).all()
        return projects

    def find(self, id):
        if id is None or id == 0:
            return None
        try:
            return db.session.query(Project).filter(Project.id == id).one()
        except:
            return None
        
    def find_by_name(self, name):
        return db.session.query(Project).filter(Project.name == name).one_or_none()