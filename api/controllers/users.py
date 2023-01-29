from flask import Blueprint
users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/users')
def get_users():
    return 'List of users'

@users_blueprint.route('/users/<int:user_id>')
def get_user(user_id):
    return f'User with ID {user_id}'
