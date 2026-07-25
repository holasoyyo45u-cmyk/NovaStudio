import json

# Cargar comandos
with open("NovaCore/commands.json", "r") as file:
    data = json.load(file)

commands = data["commands"]

def translate(text):
    text = text.lower()

    for name, info in commands.items():
        if name.replace("_", " ") in text:
            return {
                "command": name,
                "action": info["action"]
            }

    return {
        "command": "unknown",
        "action": "None"
    }


# Prueba
while True:
    user = input("Nova > ")
    result = translate(user)
    print(result)
