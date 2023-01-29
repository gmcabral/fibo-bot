from flask import Flask
from controllers.users import users_blueprint
from controllers.fibos import fibos_blueprint
# from items import items_blueprint

app = Flask(__name__)
app.register_blueprint(users_blueprint)
app.register_blueprint(fibos_blueprint)

# app.register_blueprint(items_blueprint)