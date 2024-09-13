from flask import Blueprint, request
from app.mapping import TaskSchema, ResponseSchema
from app.services.response_message import ResponseBuilder
from app.services import TaskService

task = Blueprint('task', __name__)

task_schema = TaskSchema()
response_schema = ResponseSchema()

task_service = TaskService()

# Get: Muestra JSON con todos las tasks
@task.route('/tasks', methods=['GET'])
def index():
    response_builder = ResponseBuilder()
    data = task_schema.dump(task_service.all(), many=True)
    response_builder.add_message("Tasks found").add_status_code(200).add_data(data)

    return response_schema.dump(response_builder.build()), 200
    
# Post: Crea una nueva task a partir de un JSON
@task.route('/tasks/add', methods=['POST'])
def add_task():
    response_builder = ResponseBuilder()
    task = task_schema.load(request.json)
    data = task_schema.dump(task_service.save(task))
    response_builder.add_message("Task created").add_status_code(201).add_data(data)

    return response_schema.dump(response_builder.build()), 201

# Delete: Elimina una task a partir de su id
@task.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task_service.delete(id)
    response_builder = ResponseBuilder()
    response_builder.add_message("Task deleted").add_status_code(200).add_data({'id': id})
    return response_schema.dump(response_builder.build()), 200


# Get: json con los datos de la taskbuscado por id
@task.route('/tasks/<int:id>', methods=['GET'])
def find(id):
    response_builder = ResponseBuilder()
    data = task_schema.dump(task_service.find(id))
    if data:
        response_builder.add_message("Task found").add_status_code(200).add_data(data)
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Task NOT found").add_status_code(404)
        return response_schema.dump(response_builder.build()), 404

# Put: Actualiza una task a partir de un JSON
@task.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id:int):
    task = task_schema.load(request.json)
    response_builder = ResponseBuilder()
    data =  task_schema.dump(task_service.update(task, id))
    if data:
        response_builder.add_message("Task updated").add_status_code(100).add_data(data)
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Task NOT updated - Team ID not found").add_status_code(404).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 404

# Get: json con los datos del project buscado por nombre de project
@task.route('/tasks/name/<name>', methods=['GET'])
def find_by_name(name:str):
    response_builder = ResponseBuilder()
    data = task_schema.dump(task_service.find_by_name(name))
    if data:
        response_builder.add_message("Task found").add_status_code(200).add_data(data)
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Task NOT found").add_status_code(404).add_data({'Name': name})
        return response_schema.dump(response_builder.build()), 404
