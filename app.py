from fastapi import FastAPI
from database import engine, Base, SessionLocal

import crud
import schemas
import sensor

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AquaFeed API"
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {
        "mensagem": "AquaFeed funcionando!"
    }


# -------------------------
# CRUD DE TANQUES
# -------------------------

@app.post("/tanques")
def criar_tanque(tanque: schemas.TanqueCreate):

    db = SessionLocal()

    return crud.criar_tanque(
        db,
        tanque
    )


@app.get("/tanques")
def listar_tanques():

    db = SessionLocal()

    return crud.listar_tanques(db)


@app.get("/tanques/{tanque_id}")
def buscar_tanque(tanque_id: int):

    db = SessionLocal()

    return crud.buscar_tanque(
        db,
        tanque_id
    )


@app.put("/tanques/{tanque_id}")
def atualizar_tanque(
    tanque_id: int,
    tanque: schemas.TanqueCreate
):

    db = SessionLocal()

    return crud.atualizar_tanque(
        db,
        tanque_id,
        tanque
    )


@app.delete("/tanques/{tanque_id}")
def deletar_tanque(tanque_id: int):

    db = SessionLocal()

    return crud.deletar_tanque(
        db,
        tanque_id
    )


# -------------------------
# SENSORES
# -------------------------

@app.get("/sensores")
def ler_sensores():

    return sensor.gerar_leitura()


# -------------------------
# ALARMES
# -------------------------

@app.get("/alarmes")
def verificar_alarme():

    leitura = sensor.gerar_leitura()

    if leitura["alerta"]:

        return {
            "status": "ALERTA",
            "acao": "Enviar Email/SMS",
            "dados": leitura
        }

    return {
        "status": "OK",
        "dados": leitura
    }