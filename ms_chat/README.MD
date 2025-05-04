# MCP Guide - Chatbot com Claude LLM

Este projeto é uma demonstração do conceito de MCP (Model Context Protocol), integrando um chatbot com LLM (Claude) e ferramentas externas, permitindo a execução de comandos e fluxos dinâmicos via protocolo MCP.

## Propósito

O objetivo deste projeto é testar e demonstrar o conceito de MCP (Model Context Protocol), que permite a integração de modelos de linguagem com ferramentas externas de forma padronizada, facilitando a criação de agentes inteligentes capazes de executar tarefas complexas.

## Funcionalidades

- Interface web via Streamlit para interação com o chatbot.
- Integração com Claude LLM (Anthropic) para processamento de linguagem natural.
- Suporte a ferramentas externas via MCP.
- Exemplo de chat contínuo com histórico de mensagens.

# 1. Como iniciar APP STREAMLIT

### 1.1 Clonar o repositório

```bash
git clone https://github.com/Leonardojdss/MCP-Guide.git
cd MCP-Guide/ms_chat
```

### 1.2 Instalar dependências

Recomenda-se o uso de um ambiente virtual (venv ou conda):

```bash
pip install -r requirements.txt
```

### 1.3 Configurar variáveis de ambiente

Crie um arquivo `.env` com as chaves necessárias para o Anthropic e outras integrações, por exemplo:

```
ANTHROPIC_API_KEY=your_anthropic_api_key
```

### 1.4 Rodar localmente com Streamlit

```bash
streamlit run app.py
```

Acesse `http://localhost:8501` no navegador.

### 1.5 Rodar com Docker

```bash
docker build -t app_mcp .
docker run -d -p 8501:8501 app_mcp
```

## Estrutura dos arquivos principais

- `app.py`: Interface web com Streamlit.
- `client_server_claude.py`: Cliente MCP que conecta ao servidor e integra com Claude para uso no streamlit.
- `client_local_claude.py`: Variante para uso local.
- `README.MD`: Este arquivo de documentação.

## Observações

- O projeto é experimental e serve para explorar o conceito de MCP.
- Certifique-se de ter acesso à API do Anthropic.
- O servidor MCP deve estar disponível e configurado corretamente.

# 2. Rodar chat sem front-end

## Client Claude

Execute o chat localmente usando Claude (Anthropic) e integração MCP via terminal:

```bash
python3 client_local_claude.py <URL_DO_SERVIDOR_MCP>
```

- Substitua `<URL_DO_SERVVIDOR_MCP>` pelo endereço do seu servidor MCP.
- Será solicitado seu input no terminal. Digite "exit" para sair.
- Certifique-se de ter configurado a variável `ANTHROPIC_API_KEY` no `.env`.

## Client Azure Openai

Execute o chat localmente usando Azure OpenAI e integração MCP via terminal:

```bash
python3 client_local_azure_openai.py <URL_DO_SERVIDOR_MCP>
```

- Substitua `<URL_DO_SERVIDOR_MCP>` pelo endereço do seu servidor MCP.
- Configure as variáveis `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_API_VERSION`, `AZURE_OPENAI_ENDPOINT` e `AZURE_OPENAI_DEPLOYMENT` no `.env`.

## Cliente Openai

Execute o chat localmente usando OpenAI (API padrão) e integração MCP via terminal:

```bash
python3 client_local_openai.py <URL_DO_SERVIDOR_MCP>
```

- Substitua `<URL_DO_SERVIDOR_MCP>` pelo endereço do seu servidor MCP.
- Configure a variável `OPENAI_API_KEY` no `.env` se necessário.

---