from fastapi import FastAPI
from app.database import engine, Base
from app.routers import libros, estudiantes, prestamos

Base.metadata.create_all(bind=engine)

app = FastAPI(
 title="Biblioteca Universitaria API",
 description="Manual Universitario de APIs Modulares con PostgreSQL Serverless.",
 version="2.0.0"
)

app.include_router(libros.router)
app.include_router(estudiantes.router)
app.include_router(prestamos.router)

@app.get("/")
def read_root():
 return {"status": "Online", "docs": "/docs"}