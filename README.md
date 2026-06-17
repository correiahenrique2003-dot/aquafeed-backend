# AquaFeed API

Sistema de monitoramento inteligente para tanques de piscicultura desenvolvido em Python com FastAPI.

## Sobre o Projeto

O AquaFeed é uma API desenvolvida para auxiliar no monitoramento de tanques de criação de peixes, permitindo o gerenciamento dos tanques e a simulação de sensores de temperatura e pH.

O sistema também possui um mecanismo de alerta capaz de identificar condições inadequadas e simular o envio de notificações para os responsáveis.

## Arquitetura do Sistema

O projeto foi desenvolvido seguindo o padrão CRUD (Create, Read, Update e Delete), utilizando FastAPI para disponibilização dos endpoints, SQLAlchemy para manipulação do banco de dados e SQLite para armazenamento das informações.

Estrutura principal:

* app.py → Rotas da API
* models.py → Modelos do banco de dados
* schemas.py → Validação de dados
* crud.py → Operações CRUD
* database.py → Conexão com banco de dados
* sensor.py → Simulação dos sensores

## Tecnologias Utilizadas

* Python 3
* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn
* Git
* GitHub
* Render

## Banco de Dados

O projeto utiliza SQLite para armazenamento dos dados dos tanques.

### Tabela Tanque

| Campo              | Tipo    |
| ------------------ | ------- |
| id                 | Integer |
| nome               | String  |
| capacidade         | Float   |
| nivel_agua         | Float   |
| sensor_temperatura | Boolean |
| sensor_ph          | Boolean |

## Funcionalidades

### CRUD de Tanques

* Criar tanque
* Listar tanques
* Buscar tanque por ID
* Atualizar tanque
* Deletar tanque

### Simulação de Sensores

* Temperatura da água
* pH da água

### Sistema de Alarmes

* Identificação automática de temperatura acima do limite
* Simulação de envio de alerta por Email/SMS

## Endpoints

### Home

GET /

### Tanques

GET /tanques

POST /tanques

GET /tanques/{id}

PUT /tanques/{id}

DELETE /tanques/{id}

### Sensores

GET /sensores

### Alarmes

GET /alarmes

## Documentação da API

Swagger:

https://aquafeed-backend.onrender.com/docs

![Swagger](docs/swagger.png)

## Deploy Online

API publicada no Render:

https://aquafeed-backend.onrender.com

## Executando Localmente

### Clonar repositório

git clone https://github.com/correiahenrique2003-dot/aquafeed-backend.git

### Entrar na pasta

cd aquafeed-backend

### Criar ambiente virtual

python -m venv venv

### Ativar ambiente virtual

Windows:

venv\Scripts\activate

### Instalar dependências

pip install -r requirements.txt

### Executar aplicação

uvicorn app:app --reload

## Autor

Henrique Correia Alves da Silva

Projeto desenvolvido para fins acadêmicos no programa Bolsa Futuro Digital.
