import asyncio
from typing import Optional
from contextlib import AsyncExitStack

from mcp import ClientSession
from mcp.client.sse import sse_client

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

class MCPClient:
    def __init__(self):
        # Initialize the MCP client
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.anthropic = Anthropic()

    async def connect_to_server(self, server_url: str):
        """
        Connect to the MCP server.
        """
        # Connect to the MCP server
        sse_transport = await self.exit_stack.enter_async_context(sse_client(server_url))
        self.sse, self.write = sse_transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.sse, self.write))

        await self.session.initialize()

        #list available tools
        response = await self.session.list_tools()
        tools = response.tools
        print(f"Available tools: {tools}")

        print(f"Connected to MCP server at {server_url}")
        
    async def close(self):
        """
        Close the connection and release resources.
        """
        if self.exit_stack:
            await self.exit_stack.aclose()
            print("Connection closed and resources released.")

    

async def main():
    # Create an instance of MCPClient
    client = MCPClient()
    try:
        # Connect to the server
        await client.connect_to_server("http://191.101.71.186:8000/mcp")
        # Aqui você pode adicionar mais código para interagir com o servidor
        # Por exemplo, um pequeno delay para manter a conexão aberta por um tempo
        await asyncio.sleep(5)
    finally:
        # Ensure resources are properly closed
        await client.close()

if __name__ == "__main__":
    asyncio.run(main())