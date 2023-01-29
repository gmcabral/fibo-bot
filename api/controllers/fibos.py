from flask import Blueprint
fibos_blueprint = Blueprint('fibos', __name__)
from repository.fibo_repository import FiboRepository
# @fibos_blueprint.route('/fibos/<string:coin_name>/<string:day>')
# def get_fibo_limits(coin_name, day):
#     return get_fibo_limits(coin_name)

@fibos_blueprint.route('/fibos/<string:coin_name>')
def get_fibo_limits(coin_name):
    test = FiboRepository()
    return test.get_current_levels(coin_name)