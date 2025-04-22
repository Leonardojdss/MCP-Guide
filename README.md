# MCP Guide

Este repositório demonstra o conceito de MCP (Model Context Protocol) integrando LLMs (Claude/Anthropic) com ferramentas externas via protocolo MCP, utilizando uma arquitetura de microsserviços.

## Visão Geral

O projeto é composto por dois principais microsserviços:

- **ms_mcp**: Servidor MCP implementado com FastAPI, responsável por expor ferramentas de CRUD de clientes em PostgreSQL via protocolo MCP.
- **ms_chat**: Chatbot com interface web (Streamlit) que integra o LLM Claude (Anthropic) e se conecta ao servidor MCP para executar comandos e fluxos dinâmicos.

A arquitetura permite que agentes inteligentes (LLMs) utilizem ferramentas externas de forma padronizada, facilitando a criação de aplicações avançadas de IA.

## Estrutura do Projeto

```
MCP-Guide/
│
├── ms_mcp/      # Servidor MCP (FastAPI, PostgreSQL)
│   ├── mcp_server.py
│   ├── api/
│   ├── infra/
│   ├── requirements.txt
│   └── README.MD
│
├── ms_chat/     # Chatbot com Claude LLM + MCP Client (Streamlit)
│   ├── app.py
│   ├── client_server.py
│   ├── requirements.txt
│   └── README.MD
│
└── README.md    # Este arquivo
```

## Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/Leonardojdss/MCP-Guide.git
cd MCP-Guide
```

### 2. Configurar e rodar o servidor MCP

Veja instruções detalhadas em [`ms_mcp/README.MD`](ms_mcp/README.MD).

Resumo:
- Configure o banco Azure PostgreSQL ou local e variáveis de ambiente no `.env`.
- Instale dependências: `pip install -r ms_mcp/requirements.txt`
- Rode localmente:  
  `uvicorn mcp_server:app --host 0.0.0.0 --port 8000`
- Ou via Docker.

### 3. Rodar o chatbot com Claude

Veja instruções detalhadas em [`ms_chat/README.MD`](ms_chat/README.MD).

Resumo:
- Configure sua chave da Anthropic no `.env`.
- Instale dependências: `pip install -r ms_chat/requirements.txt`
- Rode localmente:  
  `streamlit run ms_chat/app.py`
- Ou via Docker.

## Exemplo de Uso

1. Inicie o servidor MCP.
2. Inicie o chatbot.
3. No chatbot, conecte-se ao endpoint do servidor MCP (ex: `http://localhost:8000`).
4. Interaja com o assistente, que poderá executar comandos CRUD em clientes via MCP.

## Dependências Principais

- Python 3.10+
- FastAPI, FastMCP, fastapi-mcp
- Anthropic (Claude)
- Streamlit
- PostgreSQL

## Documentação dos Microsserviços

- [ms_mcp/README.MD](ms_mcp/README.MD): Documentação do servidor MCP.
- [ms_chat/README.MD](ms_chat/README.MD): Documentação do chatbot e integração com Claude.

## Scripts Úteis

### Exemplo de tabela no PostgreSQL

```sql
CREATE TABLE IF NOT EXISTS customer (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

Este projeto é experimental e serve para explorar o conceito de MCP, integração de LLMs e ferramentas externas.