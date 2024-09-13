from flask import Blueprint, request
from app.mapping import TeamSchema, ResponseSchema, UserRoleTeamSchema
from app.services.response_message import ResponseBuilder
from app.services import TeamService, UserRoleTeamService

team = Blueprint('team', __name__)

team_schema = TeamSchema()
response_schema = ResponseSchema()
urt_schema = UserRoleTeamSchema()

team_service = TeamService()
urt_service = UserRoleTeamService()

# Get: Muestra JSON con todos los teams
@team.route('/teams', methods=['GET'])
def index():
    response_builder = ResponseBuilder()
    data = team_schema.dump(team_service.all(), many=True)
    response_builder.add_message("Teams found").add_status_code(200).add_data(data)

    return response_schema.dump(response_builder.build()), 200
    
# Post: Crea un nuevo usuario a partir de un JSON
@team.route('/teams/add', methods=['POST'])
def add_team():
    response_builder = ResponseBuilder()
    team = team_schema.load(request.json)
    data = team_schema.dump(team_service.save(team))
    response_builder.add_message("Team created").add_status_code(201).add_data(data)

    return response_schema.dump(response_builder.build()), 201

# Delete: Elimina un usuario a partir de su id
@team.route('/teams/<int:id>', methods=['DELETE'])
def delete_team(id):
    team_service.delete(id)
    response_builder = ResponseBuilder()
    response_builder.add_message("Team deleted").add_status_code(200).add_data({'id': id})
    return response_schema.dump(response_builder.build()), 200

# Get: Muestra JSON con los Users y sus Roles asignados de un Team determinado
@team.route('/teams/members/<int:id>', methods=['GET'])
def get_members(id):
    response_builder = ResponseBuilder()
    data = urt_schema.dump(urt_service.get_users_and_roles(id), many=True)
    response_builder.add_message("Members found").add_status_code(200).add_data(data)
    return response_schema.dump(response_builder.build()), 200

# Get: json con los datos del usuario buscado por id
@team.route('/teams/<int:id>', methods=['GET'])
def find(id):
    response_builder = ResponseBuilder()
    data = team_schema.dump(team_service.find(id))
    if data:
        response_builder.add_message("Team found").add_status_code(200).add_data(data)
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Team NOT found").add_status_code(404)
        return response_schema.dump(response_builder.build()), 404

# Put: Actualiza un team
@team.route('/teams/<int:id>', methods=['PUT'])
def update_team(id:int):
    team = team_schema.load(request.json)
    response_builder = ResponseBuilder()
    data =  team_schema.dump(team_service.update(team, id))
    if data:
        response_builder.add_message("Team updated").add_status_code(100).add_data(data)
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Team NOT updated - Team ID not found").add_status_code(404).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 404

# Get: json con los datos del team buscado por team_name
@team.route('/teams/team_name/<team_name>', methods=['GET'])
def find_by_team_name(team_name:str):
    response_builder = ResponseBuilder()
    data = team_schema.dump(team_service.find_by_name(team_name))
    if data:
        response_builder.add_message("Team found").add_status_code(200).add_data(data)
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Team NOT found").add_status_code(404).add_data({'Teamname': team_name})
        return response_schema.dump(response_builder.build()), 404


