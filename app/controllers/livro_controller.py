from flask import request, jsonify
from app.services.livro_service import LivroService

class LivroController:
    @staticmethod
    def adicionar_livro(dados):
        mensagem = LivroService.adicionar_livro(dados)
        return jsonify(mensagem)

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
