from pydantic import BaseModel, Field


class TanqueBase(BaseModel):
    nome: str
    capacidade: float = Field(gt=0)
    nivel_agua: float = Field(ge=0)
    temperatura: float = 0
    oxigenio: float = 0
    sensor_temperatura: bool
    sensor_ph: bool


class TanqueCreate(TanqueBase):
    pass


class Tanque(BaseModel):
    id: int
    nome: str
    capacidade: float
    nivel_agua: float
    temperatura: float
    oxigenio: float
    sensor_temperatura: bool
    sensor_ph: bool

    class Config:
        from_attributes = True


class LeituraCreate(BaseModel):
    temperatura: float
    oxigenio: float