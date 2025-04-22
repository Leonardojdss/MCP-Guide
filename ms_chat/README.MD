# MCP Guide - Chatbot com Claude LLM

Este projeto é uma demonstração do conceito de MCP (Model Context Protocol), integrando um chatbot com LLM (Claude) e ferramentas externas, permitindo a execução de comandos e fluxos dinâmicos via protocolo MCP.

## Propósito

O objetivo deste projeto é testar e demonstrar o conceito de MCP (Model Context Protocol), que permite a integração de modelos de linguagem com ferramentas externas de forma padronizada, facilitando a criação de agentes inteligentes capazes de executar tarefas complexas.

## Funcionalidades

- Interface web via Streamlit para interação com o chatbot.
- Integração com Claude LLM (Anthropic) para processamento de linguagem natural.
- Suporte a ferramentas externas via MCP.
- Exemplo de chat contínuo com histórico de mensagens.

## Como iniciar

### 1. Clonar o repositório

```bash
git clone https://github.com/Leonardojdss/MCP-Guide.git
cd MCP-Guide/ms_chat
```

### 2. Instalar dependências

Recomenda-se o uso de um ambiente virtual (venv ou conda):

```bash
pip install -r requirements.txt
```

### 3. Configurar variáveis de ambiente

Crie um arquivo `.env` com as chaves necessárias para o Anthropic e outras integrações, por exemplo:

```
ANTHROPIC_API_KEY=your_anthropic_api_key
```

### 4. Rodar localmente com Streamlit

```bash
streamlit run app.py
```

Acesse `http://localhost:8501` no navegador.

### 5. Rodar com Docker

```bash
docker build -t app_mcp .
docker run -d -p 8501:8501 app_mcp
```

## Estrutura dos arquivos principais

- `app.py`: Interface web com Streamlit.
- `client_server.py`: Cliente MCP que conecta ao servidor e integra com Claude.
- `client_local.py`: Variante para uso local.
- `README.MD`: Este arquivo de documentação.

## Observações

- O projeto é experimental e serve para explorar o conceito de MCP.
- Certifique-se de ter acesso à API do Anthropic.
- O servidor MCP deve estar disponível e configurado corretamente.

---