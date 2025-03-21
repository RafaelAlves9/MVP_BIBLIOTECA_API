from flask import Flask, request, jsonify
from flask_restx import Resource
from flask_cors import CORS
from app.models.livro_model import db, Livro
from app.controllers.livro_controller import LivroController
from app.settings.swagger import swagger, livro_model  # Importando a instância do Swagger e o modelo

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
swagger.init_app(app)  # Inicializando a instância do Swagger no app
ns = swagger.namespace('livros', description='Operações relacionadas aos livros')

# Classe para o recurso Livro
@ns.route('/')
class LivroResource(Resource):
    @swagger.doc('adicionar_livro')
    @swagger.expect(livro_model)  # Especificando o modelo para a documentação do Swagger
    def post(self):
        """Adicionar um novo livro"""
        dados = request.json
        novo_livro = Livro(titulo=dados['titulo'], autor=dados['autor'])
        return LivroController.adicionar_livro(novo_livro)  # Passar os dados para o controller

    @swagger.doc('listar_livros')
    def get(self):
        """Listar todos os livros"""
        return LivroController.listar_livros()

@ns.route('/<int:id>')
class LivroByIdResource(Resource):
    @swagger.doc('pegar_livro')
    def get(self, id):
        """Pegar um livro pelo ID"""
        return LivroController.pegar_livro(id)

    @swagger.doc('atualizar_livro')
    @swagger.expect(livro_model)  # Esperando os dados do livro para atualização
    def put(self, id):
        """Atualizar um livro pelo ID"""
        dados = request.json
        livro = Livro(titulo=dados['titulo'], autor=dados['autor'])
        return LivroController.atualizar_livro(id, livro)  # Passar os dados para o controller

    @swagger.doc('deletar_livro')
    def delete(self, id):
        """Deletar um livro pelo ID"""
        return LivroController.deletar_livro(id)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria o banco de dados e as tabelas dentro do contexto da aplicação
    app.run(debug=True)
