from app.notification.notification import NotificationService
from flask import jsonify
from app.repositories.livro_repository import LivroRepository

class LivroService:

    def __init__(self):
        self.repository = LivroRepository()
        self.notification = NotificationService()

    @staticmethod
    def adicionar_livro(dados):
        titulo = dados.titulo

        if len(titulo) < 2:
            return NotificationService.notify_error('O titulo deve ter pelo menos 2 caracteres.')
        elif len(titulo) > 100:
            return NotificationService.notify_error('O titulo não pode ultrapassar 100 caracteres.')

        LivroRepository.adicionar_livro(dados)
        return jsonify({'mensagem': 'Livro adicionado com sucesso!'})

    @staticmethod
    def listar_livros():
        livros = LivroRepository.listar_livros()
        return [{'id': livro.id, 'titulo': livro.titulo, 'autor': livro.autor} for livro in livros]

    @staticmethod
    def atualizar_livro(id, dados):
        titulo = dados.titulo
        
        if len(titulo) < 2:
            return NotificationService.notify_error('O titulo deve ter pelo menos 2 caracteres.')
        elif len(titulo) > 100:
            return NotificationService.notify_error('O titulo não pode ultrapassar 100 caracteres.')
        
        LivroRepository.atualizar_livro(id, dados)
        return {'mensagem': 'Livro atualizado com sucesso!'}

    @staticmethod
    def deletar_livro(id):
        LivroRepository.deletar_livro(id)
        return {'mensagem': 'Livro deletado com sucesso!'}
