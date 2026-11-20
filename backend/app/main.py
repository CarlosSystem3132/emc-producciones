from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1 import auth, usuarios, empresas, stands, paquetes, reservas, chat

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    description="API comercial para gestión de empresas, stands, paquetes y reservas."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4321",
        "http://127.0.0.1:4321",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix=f"{settings.API_V1_PREFIX}/auth", tags=["Autenticación"])
app.include_router(usuarios.router, prefix=f"{settings.API_V1_PREFIX}/usuarios", tags=["Usuarios"])
app.include_router(empresas.router, prefix=f"{settings.API_V1_PREFIX}/empresas", tags=["Empresas"])
app.include_router(stands.router, prefix=f"{settings.API_V1_PREFIX}/stands", tags=["Stands"])
app.include_router(paquetes.router, prefix=f"{settings.API_V1_PREFIX}/paquetes", tags=["Paquetes"])
app.include_router(reservas.router, prefix=f"{settings.API_V1_PREFIX}/reservas", tags=["Reservas"])
app.include_router(chat.router, prefix=f"{settings.API_V1_PREFIX}/chat", tags=["Chat IA"])


@app.get("/health")
def health():
    return {"status": "ok", "service": "EMC Producciones API"}