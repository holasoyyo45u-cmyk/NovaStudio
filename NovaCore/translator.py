import json
import re

# Cargar comandos
with open("NovaCore/commands.json", "r", encoding="utf-8") as file:
    data = json.load(file)

commands = data["commands"]


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-záéíóúñ0-9 ]", "", text)
    return text


def calculate_score(text, keywords):
    score = 0

    for keyword in keywords:
        keyword = clean_text(keyword)

        if keyword in text:
            score += len(keyword)

    return score


def translate(text):
    text = clean_text(text)

    best_command = None
    best_score = 0

    for name, info in commands.items():

        score = calculate_score(
            text,
            info.get("keywords", [])
        )

        if score > best_score:
            best_score = score
            best_command = {
                "command": name,
                "action": info["action"],
                "parameters": info["parameters"],
                "description": info["description"],
                "confidence": score
            }

    if best_command:
        return best_command

    return {
        "command": "unknown",
        "action": "None",
        "parameters": [],
        "description": "No entendí la orden",
        "confidence": 0
    }


# Prueba del sistema
while True:
    user = input("\nNova > ")

    result = translate(user)

    print("\n--- Nova entiende ---")
    print("Comando:", result["command"])
    print("Acción:", result["action"])
    print("Parámetros:", result["parameters"])
    print("Confianza:", result["confidence"])    print("\n--- Resultado ---")
    print("Comando:", result["command"])
    print("Acción:", result["action"])
    print("Parámetros:", result["parameters"])
    print("Descripción:", result["description"])
