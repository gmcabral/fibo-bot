from flask import Flask
from controllers.instrumentos import instrumentos_blueprint
# from controllers.fibos import fibos_blueprint
# from items import items_blueprint

app = Flask(__name__)
app.register_blueprint(instrumentos_blueprint)
# app.register_blueprint(fibos_blueprint)

# app.register_blueprint(items_blueprint)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)