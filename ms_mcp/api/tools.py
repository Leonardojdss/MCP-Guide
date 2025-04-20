from fastapi import APIRouter

router = APIRouter()

@router.get("/hello/{name}", operation_id="hello world")
async def hello(name: str):
    """
    A simple hello world endpoint.
    """
    return {"message": f"Hello World, {name}!"}
