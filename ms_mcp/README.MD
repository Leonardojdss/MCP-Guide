# MCP Server - POC

Este projeto é uma Prova de Conceito (POC) para testar o conceito de MCP (Model Context Protocol) utilizando FastAPI. O objetivo é demonstrar como implementar um servidor MCP padronizando o uso de ferramentas, uma forma de conceder essas ferramentas aos agentes.

## Propósito

O propósito deste projeto é validar e testar o conceito de MCP (Model Context Protocol), permitindo a criação, consulta, atualização e remoção de clientes via API RESTful, além de expor endpoints compatíveis com o protocolo MCP.

## Como iniciar

### 1. Clonar o repositório

```bash
git clone https://github.com/Leonardojdss/MCP-Guide.git
cd ms_mcp
```

### 2. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

#### Para uso local:
```
DBHOST=localhost
DBNAME=seu_banco
DBUSER=seu_usuario
DBPASSWORD=sua_senha
SSLMODE=prefer
```

#### Para uso com Azure PostgreSQL:
```
DBHOST="nome_do_servidor.postgres.database.azure.com"
DBNAME=seu_banco
DBUSER=seu_usuario
DBPASSWORD=sua_senha
SSLMODE="require"
```

### 3. Instalar dependências

#### Localmente

Recomenda-se o uso de um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Docker

Para rodar via Docker:

```bash
docker build -t mcp_server .
docker run -d -p 8000:8000 --env-file .env mcp_server
```

### 4. Iniciar o servidor

#### Docker

```bash
docker run -d -p 8000:8000 --env-file .env mcp_server
```

#### Localmente

```bash
uvicorn mcp_server:app --host 0.0.0.0 --port 8000
```

## Endpoints

- CRUD de clientes: `/customers`
- Integração MCP: endpoints expostos via FastAPI-MCP

Acesse a documentação interativa em: [http://localhost:8000/docs](http://localhost:8000/docs)

---