from typing import List, Optional
from app.models import Team
from app import db

class TeamRepository:

    def save(self, team: Team) -> Team:
        db.session.add(team)
        db.session.commit()
        return team
    
    def update(self, team: Team, id: int) -> Optional[Team]:
        entity = self.find(id)
        if entity:
            entity.team_name = team.team_name
            db.session.add(entity)
            db.session.commit()
            return entity
        else:
            return None
    
    def delete(self, team: Team) -> None:
        db.session.delete(team)
        db.session.commit()
    
    def all(self) -> List[Team]:
        teams = db.session.query(Team).all()
        return teams

    def find(self, id: int) -> Optional[Team]:
        if id is None or id == 0:
            return None
        try:
            return db.session.query(Team).filter(Team.id == id).one()
        except:
            return None
        
    def find_by_name(self, name: str) -> Optional[Team]:
        return db.session.query(Team).filter(Team.team_name == name).one_or_none()