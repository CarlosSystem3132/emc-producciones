from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def usuarios_health():
    return {"module": "usuarios", "status": "ok"}