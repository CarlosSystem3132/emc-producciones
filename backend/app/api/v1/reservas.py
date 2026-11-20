from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def reservas_health():
    return {"module": "reservas", "status": "ok"}