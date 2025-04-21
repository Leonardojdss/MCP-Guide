from fastapi import APIRouter

router = APIRouter()

@router.get("/", operation_id="sum two numbers")
async def hello(a: int, b: int):
    """
    sum two numbers.
    """
    return {"result": a + b}
