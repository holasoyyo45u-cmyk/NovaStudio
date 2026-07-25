import json

# Cargar comandos
with open("NovaCore/commands.json", "r") as file:
    data = json.load(file)

commands = data["commands"]


def translate(text):
    text = text.lower()

    for name, info in commands.items():
        readable_name = name.replace("_", " ")

        if readable_name in text:
            return {
                "command": name,
                "action": info["action"],
                "parameters": info["parameters"],
                "description": info["description"]
            }

    return {
        "command": "unknown",
        "action": "None",
        "parameters": [],
        "description": "No se encontró un comando"
    }


# Prueba
while True:
    user = input("Nova > ")
    result = translate(user)

    print("\n--- Resultado ---")
    print("Comando:", result["command"])
    print("Acción:", result["action"])
    print("Parámetros:", result["parameters"])
    print("Descripción:", result["description"])
