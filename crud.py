from sqlalchemy.orm import Session

from models import Tanque
from schemas import TanqueCreate


def criar_tanque(db: Session, tanque: TanqueCreate):
    novo = Tanque(**tanque.model_dump())

    db.add(novo)

    db.commit()

    db.refresh(novo)

    return novo


def listar_tanques(db: Session):
    return db.query(Tanque).all()


def buscar_tanque(db: Session, tanque_id: int):
    return db.query(Tanque).filter(
        Tanque.id == tanque_id
    ).first()

def deletar_tanque(db: Session, tanque_id: int):
    tanque = buscar_tanque(db, tanque_id)

    if not tanque:
        return {"erro": "Tanque não encontrado"}

    db.delete(tanque)
    db.commit()

    return {"mensagem": "Tanque deletado com sucesso"}

def atualizar_tanque(db: Session, tanque_id: int, dados):
    
    tanque = buscar_tanque(db, tanque_id)

    if tanque:

        tanque.nome = dados.nome
        tanque.capacidade = dados.capacidade
        tanque.nivel_agua = dados.nivel_agua
        tanque.sensor_temperatura = dados.sensor_temperatura
        tanque.sensor_ph = dados.sensor_ph

        db.commit()
        db.refresh(tanque)

    return tanque

from schemas import LeituraCreate


def atualizar_leitura(
    db: Session,
    tanque_id: int,
    leitura: LeituraCreate
):
    tanque = buscar_tanque(db, tanque_id)

    if not tanque:
        return None

    tanque.temperatura = leitura.temperatura
    tanque.oxigenio = leitura.oxigenio

    db.commit()
    db.refresh(tanque)

    return tanque