from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def stands_health():
    return {"module": "stands", "status": "ok"}