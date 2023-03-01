from flask import Blueprint
instrumentos_blueprint = Blueprint('instrumentos', __name__)
from repository.instrumento_repository import InstrumentoRepository

@instrumentos_blueprint.route('/instrumentos/')
def get_instrumentos():
    return InstrumentoRepository.get_instrumentos()

# @instrumentos_blueprint.route('/instrumentos/<string:coin_name>/<string:day>')
# def get_fibo_limits(coin_name, day):
#     return get_fibo_limits(coin_name)

# @instrumentos_blueprint.route('/instrumentos/<string:name>')
# def get_instrumentos_limits(name):
#     test = FiboRepository()
#     return test.get_current_levels(name)