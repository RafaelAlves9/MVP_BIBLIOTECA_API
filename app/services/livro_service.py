from app.notification.notification import NotificationService
from flask import jsonify, make_response
from app.repositories.livro_repository import LivroRepository

class LivroService:

    def __init__(self):
        self.repository = LivroRepository()
        self.notification = NotificationService()

    @staticmethod
    def adicionar_livro(dados):
        titulo = dados.titulo

        if len(titulo) < 2:
            return self.notification.notify_error('O título deve ter pelo menos 2 caracteres.')
        elif len(titulo) > 100:
            return self.notification.notify_error('O título não pode ultrapassar 100 caracteres.')

        LivroRepository.adicionar_livro(dados)
        return self.notification.notify_error('Livro atualizado com sucesso!', 200)


    @staticmethod
    def listar_livros():
        livros = LivroRepository.listar_livros()
        return [{'id': livro.id, 'titulo': livro.titulo, 'autor': livro.autor} for livro in livros]

    @staticmethod
    def pegar_livro(id):
        livro = LivroRepository.pegar_livro(id)
        return {'id': livro.id, 'titulo': livro.titulo, 'autor': livro.autor}

    @staticmethod
    def atualizar_livro(id, dados):
        # Validação
        if len(titulo) < 2:
            return {'erro': 'O título deve ter pelo menos 2 caracteres.'}, 400
        elif len(titulo) > 100:
            return {'erro': 'O título não pode ultrapassar 100 caracteres.'}, 400
        
        LivroRepository.atualizar_livro(id, dados)
        return {'mensagem': 'Livro atualizado com sucesso!'}

    @staticmethod
    def deletar_livro(id):
        LivroRepository.deletar_livro(id)
        return {'mensagem': 'Livro deletado com sucesso!'}
