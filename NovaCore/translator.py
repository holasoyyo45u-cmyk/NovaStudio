import json
import re

from .memory import add_history, get_learned_commands
from context import update_context
from parameters import extract_parameters


# Cargar comandos base
with open("NovaCore/commands.json", "r", encoding="utf-8") as file:
    data = json.load(file)

base_commands = data["commands"]



def clean_text(text):
    text = text.lower()
    text = re.sub(
        r"[^a-záéíóúñ0-9 ]",
        "",
        text
    )
    return text.strip()



def get_all_commands():

    commands = {}

    commands.update(base_commands)

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

                "parameters": info.get(
                    "parameters",
                    []
                ),

                "description": info.get(
                    "description",
                    ""
                ),

                "confidence": score

            }


    if best_command:

        detected_parameters = extract_parameters(text)

        best_command["detected_values"] = detected_parameters


        add_history({

            "input": text,

            "result": best_command

        })


        update_context(

            best_command["action"],

            parameters=detected_parameters

        )


        return best_command



    return {

        "command": "unknown",

        "action": "None",

        "parameters": [],

        "detected_values": {},

        "description": "Nova no entendió la orden",

        "confidence": 0

    }



if __name__ == "__main__":

    while True:

        user = input("\nNova > ")

        result = translate(user)

        print("\n--- Nova ---")

        print(
            json.dumps(
                result,
                indent=4,
                ensure_ascii=False
            )
        )
