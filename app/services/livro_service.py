from app.repositories.livro_repository import LivroRepository

class LivroService:
    @staticmethod
    def adicionar_livro(dados):
        LivroRepository.adicionar_livro(dados)
        return {'mensagem': 'Livro atualizado com sucesso!'}

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
        livro = LivroRepository.atualizar_livro(id, dados)
        return {'mensagem': 'Livro atualizado com sucesso!'}

    @staticmethod
    def deletar_livro(id):
        LivroRepository.deletar_livro(id)
        return {'mensagem': 'Livro deletado com sucesso!'}
