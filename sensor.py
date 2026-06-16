import random

def enviar_alerta(temperatura):

    print("=" * 40)
    print("ALERTA DISPARADO")
    print(f"Temperatura detectada: {temperatura}°C")
    print("EMAIL/SMS ENVIADO COM SUCESSO")
    print("=" * 40)


def gerar_leitura():

    temperatura = random.randint(20, 40)

    ph = round(
        random.uniform(6.0, 9.0),
        1
    )

    alerta = False
    mensagem = "Normal"

    if temperatura > 30:

        alerta = True
        mensagem = "Temperatura acima do limite"

        enviar_alerta(temperatura)

    return {
        "temperatura": temperatura,
        "ph": ph,
        "alerta": alerta,
        "mensagem": mensagem
    }