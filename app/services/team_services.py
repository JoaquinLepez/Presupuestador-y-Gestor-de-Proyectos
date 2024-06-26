from app.repositories import TeamRepository

repository = TeamRepository()

class TeamService:

    def save(self, team):
        return repository.save(team)
    
    def update(self, team, id):
        return repository.update(team, id)
    
    def delete(self, team):
        return repository.delete(team)
    
    def all(self):
        return repository.all()
    
    def find(self, id):
        return repository.find(id)
    
    def find_by_name(self, name):
        return repository.find_by_name(name)