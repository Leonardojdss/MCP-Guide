from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
from api.tools import router

app = FastAPI()

# tool CRUD
app.include_router(router)

mcp = FastApiMCP(
    app,
    name="POC mcp server",
    description="POC mcp server",
    base_url="http://localhost:8000",
    describe_all_responses=True,
    describe_full_response_schema=True)

# Mount the MCP server directly to your FastAPI app
mcp.mount(router=router)

if __name__ == "__main__":
    import uvicorn
    # Run the FastAPI app with Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
