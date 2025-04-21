import asyncio
import sys
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

    async def process_query(self, query: str):
        """
        Process a query using Claude and available tools.
        """
        messages = [
            {
                "role": "user",
                "content": query,
            }
        ]

        response = await self.session.list_tools()
        available_tools = [{
            "name": tool.name,
            "description": tool.description,
            "input_schema": tool.inputSchema
        } for tool in response.tools]

        # initialize the Anthropic client
        response = self.anthropic.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            messages=messages,
            tools=available_tools
        )

        #process response and handle tools calls
        final_text = []
        
        for content in response.content:
            if content.type == "text":
                final_text.append(content.text)
            elif content.type == "tool_use":
                tool_name = content.name
                tools_args = content.input

                # execute the tool
                result = await self.session.call_tool(tool_name, tools_args)
                final_text.append(f"[calling tool {tool_name} with args {tools_args}]")

                # continue the conversation with the tool's result
                if hasattr(content, "text") and content.text:
                    messages.append({
                            "role": "assistant",
                            "content": content.text,
                        })
                messages.append({
                    "role": "user",
                    "content": result.content,
                    })

                # get next response from claude
                response = self.anthropic.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=1000,
                    messages=messages
                )

                final_text.append(response.content[0].text)

        return "\n".join(final_text)

    async def chat_loop(self):
        """
        Start a chat loop to interact with the user.
        """
        print("\nMCP Client Started!")
        print("Type 'exit' to quit the chat.")

        while True:
            try:
                query = input("You: ").strip()

                if query.lower() == "exit":
                    print("Exiting chat...")
                    break

                response = await self.process_query(query)
                print("\n" + response)
            
            except Exception as e:
                print(f"An error occurred: {e}")
            
    async def cleanup(self):
        """
        Cleanup resources and close the connection.
        """
        await self.exit_stack.aclose()

async def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <server_url>")
        sys.exit(1)

    client = MCPClient()
    try:
        await client.connect_to_server(sys.argv[1])
        await client.chat_loop()
    finally:
        await client.cleanup()

if __name__ == "__main__":
    import sys
    asyncio.run(main())