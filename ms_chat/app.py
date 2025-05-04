import streamlit as st
import asyncio
from ms_chat.client_server_claude import MCPClient

with st.sidebar:
    st.title("MCP Chatbot with Claude LLM")    
    server_url = st.text_input("Enter the server URL:")
    button = st.button("Connect to Server MCP and start chat")
    if button:
        st.session_state.server_url = server_url
        st.success("Connected to server!")

async def ask_bot(server_url, prompt):
    client = MCPClient()
    await client.connect_to_server(server_url)
    response = await client.process_query(prompt)
    await client.close()
    return response

# Initialize history of messages in session
if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat history e chat input
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

history = ""
for msg in st.session_state.messages:
    history += f"{msg['role']}: {msg['content']}\n"

prompt = st.chat_input("Fale com o sistema de informacão de Clientes")
if server_url and prompt:
    st.chat_message("user").write(prompt)
    user = st.session_state.messages.append({"role": "user", "content": prompt})

    full_prompt = history + f"user: {prompt}\n"
    response = asyncio.run(ask_bot(server_url, full_prompt))
    st.chat_message("assistant").write(response)
    assistant = st.session_state.messages.append({"role": "assistant", "content": response})