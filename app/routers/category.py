import logging
from flask import Blueprint, jsonify, request
from app.models.category import Category
from app import db

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

category = Blueprint('category', __name__, url_prefix='/categories')


# GET all categories
@category.route('/', methods=['GET'])
def get_categories():
    """Retrieve all categories."""
    try:
        categories = Category.query.all()
        return jsonify([category.to_dict() for category in categories]), 200
    except Exception as e:
        logger.error(f"Error retrieving categories: {e}")
        return jsonify({'error': 'Failed to retrieve categories'}), 500


# GET a specific category by ID
@category.route('/<int:id>', methods=['GET'])
def get_category(id):
    """Retrieve a specific category by ID."""
    try:
        category = Category.query.get_or_404(id)
        return jsonify(category.to_dict()), 200
    except Exception as e:
        logger.error(f"Error retrieving category with ID {id}: {e}")
        return jsonify({'error': 'Failed to retrieve category'}), 500


# POST a new category
@category.route('/', methods=['POST'])
def create_category():
    """Create a new category."""
    data = request.get_json()

    if not data or 'name' not in data:
        logger.warning("Name is required for category creation.")
        return jsonify({'error': 'Name is required'}), 400

    name = data.get('name')
    description = data.get('description')

    # Check if category already exists
    if Category.query.filter_by(name=name).first():
        logger.warning(f"Category with name '{name}' already exists.")
        return jsonify({'error': 'Category already exists'}), 409

    try:
        category = Category(name=name, description=description)
        db.session.add(category)
        db.session.commit()
        logger.info(f"Category created successfully with ID {category.id}.")
        return jsonify(category.to_dict()), 201
    except Exception as e:
        logger.error(f"Error creating category: {e}")
        db.session.rollback()
        return jsonify({'error': 'Failed to create category'}), 500


# PUT (update) a specific category
@category.route('/<int:id>', methods=['PUT'])
def update_category(id):
    """Update a specific category."""
    data = request.get_json()

    try:
        category = Category.query.get_or_404(id)

        if not data:
            logger.warning(f"No input data provided for category ID {id}.")
            return jsonify({'error': 'No input data provided'}), 400

        category.name = data.get('name', category.name)
        category.description = data.get('description', category.description)

        db.session.commit()
        logger.info(f"Category with ID {id} updated successfully.")
        return jsonify(category.to_dict()), 200
    except Exception as e:
        logger.error(f"Error updating category with ID {id}: {e}")
        db.session.rollback()
        return jsonify({'error': 'Failed to update category'}), 500


# DELETE a specific category
@category.route('/<int:id>', methods=['DELETE'])
def delete_category(id):
    """Delete a specific category."""
    try:
        category = Category.query.get_or_404(id)
        db.session.delete(category)
        db.session.commit()
        logger.info(f"Category with ID {id} deleted successfully.")
        return jsonify({'message': 'Category deleted successfully'}), 204
    except Exception as e:
        logger.error(f"Error deleting category with ID {id}: {e}")
        db.session.rollback()
        return jsonify({'error': 'Failed to delete category'}), 500
