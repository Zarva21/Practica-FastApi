from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import LibroModel
from app.schemas import LibroBase, LibroResponse

router = APIRouter(prefix="/libros", tags=["Libros"])

@router.post("/", response_model=LibroResponse)
def crear_libro(libro: LibroBase, db: Session = Depends(get_db)):
 db_libro = db.query(LibroModel).filter(LibroModel.id == libro.id).first()
 if db_libro:
 raise HTTPException(status_code=400, detail="El ID del libro ya existe.")
 nuevo_libro = LibroModel(**libro.model_dump())
 db.add(nuevo_libro)
 db.commit()
 db.refresh(nuevo_libro)
 return nuevo_libro

@router.get("/", response_model=List[LibroResponse])
def listar_libros(db: Session = Depends(get_db)):
 return db.query(LibroMod