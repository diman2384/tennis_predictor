from fastapi import APIRouter

router = APIRouter()

@router.post("/telegram")
async def auth_telegram():
    return {"status": "ok"}