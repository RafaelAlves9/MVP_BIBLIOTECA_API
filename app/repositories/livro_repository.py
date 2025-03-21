from app.models.livro_model import Livro, db

class LivroRepository:
    @staticmethod
    def adicionar_livro(dados):
        db.session.add(dados)
        db.session.commit()
        return dados

    @staticmethod
    def listar_livros():
        return Livro.query.all()

    @staticmethod
    def pegar_livro(id):
        return Livro.query.get_or_404(id)

    @staticmethod
    def atualizar_livro(id, dados):
        livro = Livro.query.get_or_404(id)
        livro.titulo = dados.titulo
        livro.autor = dados.autor
        db.session.commit()
        return livro

    @staticmethod
    def deletar_livro(id):
        livro = Livro.query.get_or_404(id)
        db.session.delete(livro)
        db.session.commit()
        return livro
