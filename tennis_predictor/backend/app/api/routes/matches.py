from fastapi import APIRouter

router = APIRouter()

@router.get("/upcoming")
async def get_upcoming_matches():
    return {"matches": []}