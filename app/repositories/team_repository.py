from app.models import Team
from app import db

class TeamRepository:

    def save(self, team):
        db.session.add(team)
        db.session.commit()
        return team
    
    def update(self, team, id):
        entity = self.find(id)
        entity.name = team.name
        db.session.add(entity)
        db.session.commit()
        return entity
    
    def delete(self, team):
        db.session.delete(team)
        db.session.commit()
    
    def all(self):
        teams = db.session.query(Team).all()
        return teams

    def find(self, id):
        if id is None or id == 0:
            return None
        try:
            return db.session.query(Team).filter(Team.id == id).one()
        except:
            return None
        
    def find_by_name(self, name):
        return db.session.query(Team).filter(Team.name == name).one_or_none()
    

