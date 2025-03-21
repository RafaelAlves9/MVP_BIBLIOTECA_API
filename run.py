from flask import Flask, request, jsonify
from flask_restx import Api
from flask_cors import CORS
from app.models.livro_model import db
from app.controllers.livro_controller import LivroController
from app.settings.swagger import swagger

# Inicializando o Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["DEBUG"] = True
app.config["PROPAGATE_EXCEPTIONS"] = True
db.init_app(app)

# Configurando o CORS para permitir qualquer origem (*)
CORS(app, resources={r"/*": {"origins": "*"}})

# Inicializando o Swagger (API)
swagger.init_app(app)

# Configurando as rotas do Swagger dentro do controlador
LivroController.configurar_rotas(swagger)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
