import asyncio
import sys
from typing import Any
from dotenv import load_dotenv
from agents import Agent, Runner
from agents.mcp import MCPServerSse
from agents.model_settings import ModelSettings

# Load environment variables from .env file
load_dotenv()

async def run(server_mpc_url: str):
    """
    Client of agent openai with continuous conversation
    Developer: leonardojdss
    """
    mcp_server = MCPServerSse(
        name="SSE Python Server",
        params={
            "url": f"{server_mpc_url}",
        },
    )

    # Connect to the MCP server
    await mcp_server.connect()

    try:
        # Agent initialization
        agent = Agent(
            model="gpt-4o-mini",
            name="Assistant",
            instructions="Use the tools to answer the questions when necessary.",
            mcp_servers=[mcp_server],
            model_settings=ModelSettings(tool_choice="auto"), #auto = the agent chooses the tool when necessary and required = ever use the tools
        )

        # Continuous conversation with agent and tools
        print("Type 'exit' or 'quit' to end the conversation")
        memory = ""
        while True:
            input_user = input("You: ")
            if input_user.lower() in ["exit", "quit"]:
                print("Ending conversation...")
                break

            # append memory to new input user
            message = f"lasted messages of chat:\n\n{memory}\n\n new input user:\n\n{input_user}"    

            result = await Runner.run(starting_agent=agent, input=message)
            print("Agent:", result.final_output)
            memory += f"User:{input_user}\nAgent:{result.final_output}"
    finally:
        # Properly handle cleanup to avoid the exceptions
        try:
            if hasattr(mcp_server, "disconnect"):
                await mcp_server.disconnect()
        except Exception as e:
            print(f"Error during disconnection: {e}")

async def main():
    if len(sys.argv) < 2:
        print("Usage: python3 client_local_openai.py <server_url>")
        sys.exit(1)

    server_mpc_url = sys.argv[1]
    
    try:
        await run(server_mpc_url)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
