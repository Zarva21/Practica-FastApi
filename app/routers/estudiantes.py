from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import EstudianteModel
from app.schemas import EstudianteBase, EstudianteResponse

router = APIRouter(prefix="/estudiantes", tags=["Estudiantes"])

@router.post("/", response_model=EstudianteResponse)
def crear_estudiante(estudiante: EstudianteBase, db: Session = Depends(get_db)):
 db_est = db.query(EstudianteModel).filter(EstudianteModel.id == estudiante.id).first()
 if db_est:
    raise HTTPException(status_code=400, detail="El ID del estudiante ya existe.")
 nuevo_estudiante = EstudianteModel(**estudiante.model_dump())
 db.add(nuevo_estudiante)
 db.commit()
 db.refresh(nuevo_estudiante)
 return nuevo_estudiante

@router.get("/", response_model=List[EstudianteResponse])
def listar_estudiantes(db: Session = Depends(get_db)):
 return db.query(EstudianteModel).all()
