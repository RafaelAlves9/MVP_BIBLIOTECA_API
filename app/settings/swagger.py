from flask_restx import Api, fields

# Criação da instância do Swagger
swagger = Api(
    version='1.0',
    title='API de Livros',
    description='Uma API para gerenciar livros',
    doc='/swagger',
)

livro_model = swagger.model('Livro', {
    'titulo': fields.String(required=True, description='Título do livro'),
    'autor': fields.String(required=True, description='Autor do livro')
})