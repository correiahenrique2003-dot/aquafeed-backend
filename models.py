from sqlalchemy import Column, Integer, String, Float, Boolean

from database import Base

class Tanque(Base):
    __tablename__ = "tanques"

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String)

    capacidade = Column(Float)

    nivel_agua = Column(Float)

    sensor_temperatura = Column(Boolean)

    sensor_ph = Column(Boolean)