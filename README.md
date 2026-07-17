# AquaFeed API



Sistema de monitoramento inteligente para tanques de piscicultura desenvolvido em Python utilizando FastAPI.

<p align="center">
Equipe do projeto AquaFeed durante o desenvolvimento no Programa Bolsa Futuro Digital – Instituto Federal de Sergipe (IFS), Campus Lagarto.
  <img src="docs/equipe.jpg" width="750">
</p>

---

## Sobre o Projeto

O AquaFeed é uma API REST desenvolvida para auxiliar no monitoramento de tanques de piscicultura, permitindo o gerenciamento dos tanques e a simulação de sensores de temperatura e pH.

O sistema também possui um mecanismo de alerta capaz de identificar condições inadequadas e simular o envio de notificações para os responsáveis.

---

## Arquitetura do Sistema

O projeto foi desenvolvido seguindo o padrão CRUD (Create, Read, Update e Delete), utilizando:

- FastAPI para disponibilização dos endpoints;
- SQLAlchemy para manipulação do banco de dados;
- PostgreSQL hospedado no Supabase para armazenamento das informações.

### Estrutura do Projeto

```
app.py          → Rotas da API
models.py       → Modelos do banco de dados
schemas.py      → Validação dos dados
crud.py         → Operações CRUD
database.py     → Conexão com PostgreSQL
sensor.py       → Simulação dos sensores
```

---

## Tecnologias Utilizadas

- Python 3
- FastAPI
- SQLAlchemy
- PostgreSQL
- Supabase
- Uvicorn
- Pytest
- Locust
- Git
- GitHub
- Render

---

## Banco de Dados

O projeto utiliza PostgreSQL hospedado no Supabase para armazenamento dos dados.

### Estrutura da tabela Tanques

| Campo | Tipo |
|-------|------|
| id | Integer |
| nome | String |
| capacidade | Float |
| nivel_agua | Float |
| sensor_temperatura | Boolean |
| sensor_ph | Boolean |

---

## Funcionalidades

### CRUD de Tanques

- Criar tanque
- Listar tanques
- Buscar tanque por ID
- Atualizar tanque
- Excluir tanque

### Simulação de Sensores

- Temperatura da água
- pH da água

### Sistema de Alarmes

- Identificação automática de temperatura acima do limite
- Simulação de envio de alerta por Email/SMS

---

## Endpoints

| Método | Endpoint | Descrição |
|---------|----------|-----------|
| GET | / | Página inicial |
| GET | /tanques | Lista todos os tanques |
| POST | /tanques | Cadastra um tanque |
| GET | /tanques/{id} | Busca um tanque |
| PUT | /tanques/{id} | Atualiza um tanque |
| DELETE | /tanques/{id} | Remove um tanque |
| GET | /sensores | Simula leitura dos sensores |
| GET | /alarmes | Verifica condições de alerta |

---

## Documentação da API

A documentação automática da API foi gerada utilizando Swagger.

**Acesse:**

https://aquafeed-backend.onrender.com/docs

![Swagger](docs/swagger.png)

---

## Deploy

A aplicação encontra-se publicada em produção utilizando Render.

**API Online**

https://aquafeed-backend.onrender.com

**Documentação Swagger**

https://aquafeed-backend.onrender.com/docs

**Banco de Dados**

PostgreSQL (Supabase)

---

## Executando Localmente

### Clonar o repositório

```bash
git clone https://github.com/correiahenrique2003-dot/aquafeed-backend.git
```

### Entrar na pasta

```bash
cd aquafeed-backend
```

### Criar ambiente virtual

```bash
python -m venv venv
```

### Ativar ambiente virtual

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

### Instalar as dependências

```bash
pip install -r requirements.txt
```

### Executar a aplicação

```bash
uvicorn app:app --reload
```

---

## Testes

### Testes Unitários

Os testes foram desenvolvidos utilizando Pytest para validar os principais endpoints da API.

Testes implementados:

- Home (/)
- Listagem de tanques (/tanques)
- Leitura dos sensores (/sensores)

Executar os testes:

```bash
python -m pytest
```

Resultado esperado:

```
====================
3 passed
====================
```

---

### Teste de Carga

Foi realizado um teste de carga utilizando o Locust com 20 usuários simultâneos.

![Teste de Carga](docs/teste-carga.png)

---

## Status do Projeto

- ✅ CRUD completo
- ✅ API REST com FastAPI
- ✅ PostgreSQL integrado ao Supabase
- ✅ SQLAlchemy
- ✅ Simulação de sensores
- ✅ Sistema de alarmes
- ✅ Testes unitários com Pytest
- ✅ Teste de carga com Locust
- ✅ Deploy no Render
- ✅ Documentação automática com Swagger
- ✅ Controle de versão utilizando Git e GitHub

**Status:** Projeto concluído.

---

## Autor

**Henrique Correia Alves da Silva**

Projeto desenvolvido para fins acadêmicos no programa **Bolsa Futuro Digital**.
