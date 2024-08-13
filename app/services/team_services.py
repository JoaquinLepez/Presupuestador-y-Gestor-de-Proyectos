from app.repositories import TeamRepository
from app.models import Team
from typing import List

repository = TeamRepository()

class TeamService:

    def save(self, team: Team) -> Team:
        return repository.save(team)
    
    def update(self, team: Team, id: int) -> Team:
        return repository.update(team, id)
    
    def delete(self, team: Team) -> bool:
        return repository.delete(team)
    
    def all(self) -> List[Team]:
        return repository.all()
    
    def find(self, id: int) -> Team:
        return repository.find(id)
    
    def find_by_name(self, name: str) -> Team:
        return repository.find_by_name(name)