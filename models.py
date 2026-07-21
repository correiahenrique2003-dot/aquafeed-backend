from sqlalchemy import Column, Integer, String, Float, Boolean

from database import Base

class Tanque(Base):
    __tablename__ = "tanques"

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String)

    capacidade = Column(Float)

    nivel_agua = Column(Float)

    temperatura = Column(Float, default=0)

    oxigenio = Column(Float, default=0)

    sensor_temperatura = Column(Boolean)

    sensor_ph = Column(Boolean)