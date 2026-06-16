from pydantic import BaseModel

class TanqueBase(BaseModel):
    nome: str
    capacidade: float
    nivel_agua: float
    sensor_temperatura: bool
    sensor_ph: bool

class TanqueCreate(TanqueBase):
    pass

class Tanque(TanqueBase):
    id: int

    class Config:
        from_attributes = True

from pydantic import BaseModel, Field

class TanqueCreate(BaseModel):
    nome: str
    capacidade: float = Field(gt=0)
    nivel_agua: float = Field(ge=0)
    sensor_temperatura: bool
    sensor_ph: bool