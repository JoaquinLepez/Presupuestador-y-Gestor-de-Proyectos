from flask import Blueprint, request
from app.mapping import ProjectSchema, ResponseSchema, TaskSchema
from app.services.response_message import ResponseBuilder
from app.services import ProjectService

project = Blueprint('project', __name__)

project_schema = ProjectSchema()
response_schema = ResponseSchema()
task_schema = TaskSchema()

project_service = ProjectService()

# Get: Muestra JSON con todos los projects
@project.route('/projects', methods=['GET'])
def index():
    response_builder = ResponseBuilder()
    data = project_schema.dump(project_service.all(), many=True)
    response_builder.add_message("Projects found").add_status_code(200).add_data(data)

    return response_schema.dump(response_builder.build()), 200
    
# Post: Crea un nuevo project a partir de un JSON
@project.route('/projects/add', methods=['POST'])
def add_project():
    response_builder = ResponseBuilder()
    project = project_schema.load(request.json)
    data = project_schema.dump(project_service.save(project))
    response_builder.add_message("Project created").add_status_code(201).add_data(data)
    return response_schema.dump(response_builder.build()), 201
    
# Delete: Elimina un project a partir de su id
@project.route('/projects/<int:id>', methods=['DELETE'])
def delete_project(id):
    project_service.delete(id)
    response_builder = ResponseBuilder()
    response_builder.add_message("Project deleted").add_status_code(200).add_data({'id': id})
    return response_schema.dump(response_builder.build()), 200

# Get: json con los datos del usuario buscado por id
@project.route('/projects/<int:id>', methods=['GET'])
def find(id):
    response_builder = ResponseBuilder()
    data = project_schema.dump(project_service.find(id))
    if data:
        response_builder.add_message("Project found").add_status_code(200).add_data(data)
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Project NOT found").add_status_code(404)
        return response_schema.dump(response_builder.build()), 404

# Put: Actualiza un project a partir de un JSON
@project.route('/projects/<int:id>', methods=['PUT'])
def update_project(id:int):
    project = project_schema.load(request.json)
    response_builder = ResponseBuilder()
    data =  project_schema.dump(project_service.update(project, id))
    if data:
        response_builder.add_message("Project updated").add_status_code(100).add_data(data)
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Project NOT updated - Team ID not found").add_status_code(404).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 404

# Get: json con los datos del project buscado por nombre de project
@project.route('/projects/name/<name>', methods=['GET'])
def find_by_name(name:str):
    response_builder = ResponseBuilder()
    data = project_schema.dump(project_service.find_by_name(name))
    if data:
        response_builder.add_message("Project found").add_status_code(200).add_data(data)
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Project NOT found").add_status_code(404).add_data({'Name': name})
        return response_schema.dump(response_builder.build()), 404

@project.route('/projects/tasks/<int:id>')
def get_tasks(id):
    response_builder = ResponseBuilder()
    data = task_schema.dump(project_service.get_tasks(id), many=True)
    if data:
        response_builder.add_message("Tasks found").add_status_code(200).add_data(data)
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Tasks NOT found").add_status_code(404)
        return response_schema.dump(response_builder.build()), 404
    
