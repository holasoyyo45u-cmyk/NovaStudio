import json
from memory import learn_command


def create_command(name, action, keywords):

    command = {
        "action": action,
        "keywords": keywords,
        "parameters": [],
        "description": "Comando aprendido por Nova"
    }

    learn_command(name, command)

    print("Nova aprendió:", name)



# Prueba
if __name__ == "__main__":

    create_command(
        "abrir_puerta",
        "OpenDoor",
        [
            "abrir puerta",
            "abre la puerta"
        ]
    )
