from flask import Blueprint, jsonify, request
from app.models.task import Task
from app import db
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bp = Blueprint('task', __name__, url_prefix='/tasks')


# GET all tasks
@bp.route('/', methods=['GET'])
def get_tasks():
    """Retrieve all tasks."""
    try:
        tasks = Task.query.all()
        return jsonify([task.to_dict() for task in tasks]), 200
    except Exception as e:
        logger.error(f"Error retrieving tasks: {e}")
        return jsonify({'error': 'Failed to retrieve tasks'}), 500


# GET a specific task by ID
@bp.route('/<int:id>', methods=['GET'])
def get_task(id):
    """Retrieve a specific task by ID."""
    try:
        task = Task.query.get_or_404(id)
        return jsonify(task.to_dict()), 200
    except Exception as e:
        logger.error(f"Error retrieving task with ID {id}: {e}")
        return jsonify({'error': 'Failed to retrieve task'}), 500


# POST a new task
@bp.route('/', methods=['POST'])
def create_task():
    """Create a new task."""
    data = request.get_json()

    if not data:
        logger.warning("No input data provided for task creation.")
        return jsonify({'error': 'No input data provided'}), 400

    title = data.get('title')
    description = data.get('description')

    if not title:
        logger.warning("Title is required for task creation.")
        return jsonify({'error': 'Title is required'}), 400

    try:
        task = Task(title=title, description=description)
        db.session.add(task)
        db.session.commit()
        logger.info(f"Task created successfully with ID {task.id}.")
        return jsonify(task.to_dict()), 201
    except Exception as e:
        logger.error(f"Error creating task: {e}")
        db.session.rollback()
        return jsonify({'error': 'Failed to create task'}), 500


# PUT (update) a specific task
@bp.route('/<int:id>', methods=['PUT'])
def update_task(id):
    """Update a specific task."""
    try:
        task = Task.query.get_or_404(id)
        data = request.get_json()

        if not data:
            logger.warning(f"No input data provided for task ID {id}.")
            return jsonify({'error': 'No input data provided'}), 400

        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.completed = data.get('completed', task.completed)

        db.session.commit()
        logger.info(f"Task with ID {id} updated successfully.")
        return jsonify(task.to_dict()), 200
    except Exception as e:
        logger.error(f"Error updating task with ID {id}: {e}")
        db.session.rollback()
        return jsonify({'error': 'Failed to update task'}), 500


# DELETE a specific task
@bp.route('/<int:id>', methods=['DELETE'])
def delete_task(id):
    """Delete a specific task."""
    try:
        task = Task.query.get_or_404(id)
        db.session.delete(task)
        db.session.commit()
        logger.info(f"Task with ID {id} deleted successfully.")
        return jsonify({'message': 'Task deleted successfully'}), 204
    except Exception as e:
        logger.error(f"Error deleting task with ID {id}: {e}")
        db.session.rollback()
        return jsonify({'error': 'Failed to delete task'}), 500
