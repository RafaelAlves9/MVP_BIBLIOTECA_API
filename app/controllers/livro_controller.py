from flask import request, jsonify
from flask_restx import Resource
from app.services.livro_service import LivroService
from app.models.livro_model import Livro
from app.settings.swagger import livro_model

class LivroController:
    @staticmethod
    def adicionar_livro(dados):
        mensagem = LivroService.adicionar_livro(dados)
        return mensagem

    @staticmethod
    def listar_livros():
        livros = LivroService.listar_livros()
        return jsonify(livros)

    @staticmethod
    def pegar_livro(id):
        livro = LivroService.pegar_livro(id)
        return jsonify(livro)

    @staticmethod
    def atualizar_livro(id, dados):
        mensagem = LivroService.atualizar_livro(id, dados)
        return jsonify(mensagem)

    @staticmethod
    def deletar_livro(id):
        mensagem = LivroService.deletar_livro(id)
        return jsonify(mensagem)

    @staticmethod
    def configurar_rotas(swagger):
        ns = swagger.namespace('livros', description='Operações relacionadas aos livros')

        @ns.route('/')
        class LivroResource(Resource):
            @swagger.doc('adicionar_livro')
            @swagger.expect(livro_model)
            def post(self):
                """Adicionar um novo livro"""
                dados = request.json
                novo_livro = Livro(titulo=dados['titulo'], autor=dados['autor'])
                return LivroController.adicionar_livro(novo_livro)

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
            @swagger.expect(livro_model)
            def put(self, id):
                """Atualizar um livro pelo ID"""
                dados = request.json
                livro = Livro(titulo=dados['titulo'], autor=dados['autor'])
                return LivroController.atualizar_livro(id, livro)

            @swagger.doc('deletar_livro')
            def delete(self, id):
                """Deletar um livro pelo ID"""
                return LivroController.deletar_livro(id)
