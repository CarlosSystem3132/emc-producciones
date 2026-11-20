from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def paquetes_health():
    return {"module": "paquetes", "status": "ok"}