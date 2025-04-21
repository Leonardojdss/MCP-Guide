# Guia MCP

## Iniciar o MCP Inspector

Para testar um servidor MCP instalar o inspector desenvolvido pela anthopic com `npx`. Por exemplo, se o seu servidor está localizado em `build/index.js`, execute o seguinte comando:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

## Exemplo de tabela no PostgreSQL

Abaixo está o script da criação de tabela no PostgreSQL no exemplo:

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