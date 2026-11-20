from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def empresas_health():
    return {"module": "empresas", "status": "ok"}