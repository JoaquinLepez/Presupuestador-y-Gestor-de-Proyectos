from flask import Blueprint, request
from app.mapping import UserSchema, ResponseSchema, UserRoleTeamSchema
from app.services.response_message import ResponseBuilder
from app.services import UserService, UserRoleTeamService

user = Blueprint('user', __name__)

user_schema = UserSchema()
response_schema = ResponseSchema()
urt_schema = UserRoleTeamSchema()

user_service = UserService()
urt_service = UserRoleTeamService()

# Get: Muestra JSON con todos los usuarios
@user.route('/users', methods=['GET'])
def index():
    return {"users": user_schema.dump(user_service.all(),many=True)}, 200

# Post: Crea un nuevo usuario a partir de un JSON
@user.route('/users/add', methods=['POST'])
def post_user():
    user = user_schema.load(request.json)

    # Verificar si UserData está presente
    if not user.data:
        response_builder = ResponseBuilder()
        response_builder.add_message("UserData es requerido para crear un nuevo usuario").add_status_code(400)
        return response_schema.dump(response_builder.build()), 400

    return {"user": user_schema.dump(user_service.save(user))}, 201

# Delete: Elimina un usuario a partir de su id
@user.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user_service.delete(id)

    response_builder = ResponseBuilder()
    response_builder.add_message("Usuario borrado").add_status_code(100).add_data({'id': id})
    return response_schema.dump(response_builder.build()), 200

# Get: json con los datos del usuario buscado por id
@user.route('/users/<int:id>', methods=['GET'])
def find(id):
    response_builder = ResponseBuilder()
    response_builder.add_message("Usuario encontrado").add_status_code(100).add_data(user_schema.dump(user_service.find(id)))
    return response_schema.dump(response_builder.build()), 200

# Put: Actualiza un usuario
@user.route('/users/<int:id>', methods=['PUT'])
def update_user(id:int):
    user = user_schema.load(request.json)
    response_builder = ResponseBuilder()
    response_builder.add_message("Usuario actualizado").add_status_code(100).add_data( user_schema.dump(user_service.update(user, id)))
    return response_schema.dump(response_builder.build()), 200

# Get: json con los datos del usuario buscado por username
@user.route('/users/username/<username>', methods=['GET'])
def find_by_username(username:str):
    response_builder = ResponseBuilder()
    user = user_service.find_by_username(username)
    if user is not None:
        response_builder.add_message("Usuario encontrado").add_status_code(100).add_data(user_schema.dump(user))
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Usuario no encontrado").add_status_code(300).add_data({'username': username})
        return response_schema.dump(response_builder.build()), 404

# Get: json con los datos del usuario buscado por email
@user.route('/users/email/<email>', methods=['GET'])
def find_by_email(email:str):
    response_builder = ResponseBuilder()
    user = user_service.find_by_email(email)
    print(user.data)
    if user is not None:
        response_builder.add_message("Usuario encontrado").add_status_code(100).add_data(user_schema.dump(user))
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Usuario no encontrado").add_status_code(300).add_data({'email': email})
        return response_schema.dump(response_builder.build()), 404


# Get: Muestra JSON con los Teams y Roles de un usuario
@user.route('/users/teams/<int:id>', methods=['GET'])
def get_roles_and_teams(id):
    return {"teams": urt_schema.dump(urt_service.get_teams_and_roles(id),many=True)}, 200