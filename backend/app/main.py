from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routers import auth, projects

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="VonderBoard API",
    description="Sistema de gestión de proyectos y tareas",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api")
app.include_router(projects.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "VonderBoard API funcionando"}