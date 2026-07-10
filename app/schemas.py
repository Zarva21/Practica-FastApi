from pydantic import BaseModel
from datetime import date
from typing import Optional

class LibroBase(BaseModel):
 id: int
 titulo: str
 autor: str
 disponible: Optional[bool] = True

class LibroResponse(LibroBase):
 class Config: from_attributes = True

class EstudianteBase(BaseModel):
 id: int
 nombre: str
 carrera: str

class EstudianteResponse(EstudianteBase):
 class Config: from_attributes = True

class PrestamoCrear(BaseModel):
 libro_id: int
 estudiante_id: int

class PrestamoResponse(BaseModel):
 id: int
 libro_id: int
 estudiante_id: int
 fecha_prestamo: date
 devuelto: bool
 class Config: from_attributes = True
