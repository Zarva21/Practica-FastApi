from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import PrestamoModel, LibroModel, EstudianteModel
from app.schemas import PrestamoCrear, PrestamoResponse

router = APIRouter(prefix="/prestamos", tags=["Préstamos"])

@router.post("/", response_model=PrestamoResponse)
def generar_prestamo(prestamo: PrestamoCrear, db: Session = Depends(get_db)):
 estudiante = db.query(EstudianteModel).filter(EstudianteModel.id ==
prestamo.estudiante_id).first()
 if not estudiante:
   raise HTTPException(status_code=404, detail="Estudiante no registrado.")
 
 libro = db.query(LibroModel).filter(LibroModel.id == prestamo.libro_id).first()
 if not libro:
   raise HTTPException(status_code=404, detail="Libro no encontrado.")
 if not libro.disponible:
   raise HTTPException(status_code=400, detail="El libro ya se encuentra prestado.")
 
 libro.disponible = False
 nuevo_prestamo = PrestamoModel(libro_id=prestamo.libro_id,
estudiante_id=prestamo.estudiante_id)
 db.add(nuevo_prestamo)
 db.commit()
 db.refresh(nuevo_prestamo)
 return nuevo_prestamo

@router.get("/", response_model=List[PrestamoResponse])
def listar_prestamos(db: Session = Depends(get_db)):
 return db.query(PrestamoModel).all()
