import logging
from flask import Blueprint, jsonify, request
from app.models.task import Task
from app.models.category import Category
from app import db

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bp = Blueprint('task', __name__, url_prefix='/tasks')


# GET all tasks, optionally filter by category
@bp.route('/', methods=['GET'])
def get_tasks():
    """Retrieve all tasks, optionally filtered by category."""
    try:
        category_id = request.args.get('category_id')
        if category_id:
            tasks = Task.query.filter_by(category_id=category_id).all()
        else:
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

    if not data or 'title' not in data:
        logger.warning("Title is required for task creation.")
        return jsonify({'error': 'Title is required'}), 400

    title = data.get('title')
    description = data.get('description')

    # Initialize category_id to None or retrieve it from category_name if provided
    category_id = None
    category_name = data.get('category')
    if category_name:
        category = Category.query.filter_by(name=category_name).first()
        if category:
            category_id = category.id
        else:
            logger.warning(f"Category '{category_name}' not found.")
            return jsonify({'error': f"Category '{category_name}' not found"}), 400
    else:
        category_id = data.get('category_id')

    try:
        # Create and save the new task
        task = Task(title=title, description=description, category_id=category_id)
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
    data = request.get_json()

    try:
        task = Task.query.get_or_404(id)

        if not data:
            logger.warning(f"No input data provided for task ID {id}.")
            return jsonify({'error': 'No input data provided'}), 400

        # Update the task attributes
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.completed = data.get('completed', task.completed)

        # Get category_name from request and fetch category_id
        category_name = data.get('category')
        if category_name:
            category = Category.query.filter_by(name=category_name).first()
            if category:
                task.category_id = category.id
            else:
                logger.warning(f"Category '{category_name}' not found.")
                return jsonify({'error': f"Category '{category_name}' not found"}), 400
        else:
            # Use the existing category ID if no new category is provided
            task.category_id = data.get('category_id', task.category_id)

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
