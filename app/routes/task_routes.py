from flask import Blueprint, request, jsonify

from app.services.task_service import TaskService

task_routes = Blueprint('task_routes', __name__, url_prefix='/api/v1/tasks')
task_service = TaskService()


@task_routes.route('', methods=['POST'])
def create_task():
    task_name = request.json.get('task_name')
    task_description = request.json.get('task_description')
    task = task_service.create_task(task_name, task_description)
    return jsonify(task.serialize())


@task_routes.route('', methods=['GET'])
def get_all_tasks():
    tasks = task_service.get_all_tasks()
    return jsonify([task.serialize() for task in tasks])


@task_routes.route('/<task_id>', methods=['GET'])
def get_task(task_id):
    task = task_service.get_task(task_id)
    if task:
        return jsonify(task.serialize())
    return jsonify({'message': 'Task not found'}), 404


@task_routes.route('/<task_id>', methods=['PUT'])
def update_task(task_id):
    task_name = request.json.get('task_name')
    task_description = request.json.get('task_description')
    task_status = request.json.get('task_status')
    task = task_service.update_task(task_id, task_name, task_description, task_status)
    if task:
        return jsonify(task.serialize())
    return jsonify({'message': 'Task not found'}), 404


@task_routes.route('/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = task_service.delete_task(task_id)
    if task:
        return jsonify(task.serialize())
    return jsonify({'message': 'Task not found'}), 404
