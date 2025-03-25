## Gerenciamento de Biblioteca

Este projeto é uma aplicação Flask que fornece uma API RESTful para o gerenciamento de uma coleção de livros em uma biblioteca. Utilizando Flask e SQLAlchemy com SQLite como banco de dados.

### Funcionalidades

* CRUD de Livros: Crie, leia, atualize e delete livros usando a API REST.
* Armazenamento com SQLite: Facilita o armazenamento e recuperação de dados de livros.

### Tecnologias Utilizadas

* Flask
* Flask-SQLAlchemy
* SQLite

### Como Configurar

#### Pré-Requisitos

* Python 3.6 ou superior
* pip

#### Instalação

1. Clone o repositório para sua máquina local:

```bash
git clone <URL do repositório>
```

2. Navegue até o diretório do projeto:

```bash
cd <nome do diretório do projeto>
```

3. Instale as dependências necessárias:

```
pip install -r requirements.txt
```

### Como Executar

1. Inicie o servidor Flask executando:

```
python run.py
```

2. A aplicação agora estará rodando em http://localhost:5000/. Você pode acessar os endpoints definidos utilizando o swaggerna rota /swagger.
