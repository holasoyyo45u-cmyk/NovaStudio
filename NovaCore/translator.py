import json
import re
from memory import add_history, get_learned_commands


# Cargar comandos base
with open("NovaCore/commands.json", "r", encoding="utf-8") as file:
    data = json.load(file)

base_commands = data["commands"]


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-záéíóúñ0-9 ]", "", text)
    return text


def get_all_commands():
    commands = {}

    # Agregar comandos originales
    commands.update(base_commands)

    # Agregar comandos aprendidos
    learned = get_learned_commands()

    commands.update(learned)

    return commands



def calculate_score(text, keywords):
    score = 0

    for keyword in keywords:
        keyword = clean_text(keyword)

        if keyword in text:
            score += len(keyword)

    return score



def translate(text):

    clean = clean_text(text)

    commands = get_all_commands()

    best_command = None
    best_score = 0


    for name, info in commands.items():

        score = calculate_score(
            clean,
            info.get("keywords", [])
        )


        if score > best_score:

            best_score = score

            best_command = {
                "command": name,
                "action": info["action"],
                "parameters": info.get("parameters", []),
                "description": info["description"],
                "confidence": score
            }


    if best_command:

        add_history({
            "input": text,
            "result": best_command
        })

        return best_command


    return {
        "command": "unknown",
        "action": "None",
        "parameters": [],
        "description": "Nova no reconoce esa orden",
        "confidence": 0
    }



while True:

    user = input("\nNova > ")

    result = translate(user)

    print("\n--- Nova ---")
    print(result)
