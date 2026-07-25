import json
import os

MEMORY_FILE = "NovaCore/memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {
            "projects": {},
            "learned_commands": {},
            "history": []
        }

    with open(MEMORY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(
            memory,
            file,
            indent=4,
            ensure_ascii=False
        )


def add_history(command):
    memory = load_memory()

    memory["history"].append(command)

    save_memory(memory)


def learn_command(name, data):
    memory = load_memory()

    memory["learned_commands"][name] = data

    save_memory(memory)


# Prueba
if __name__ == "__main__":
    memory = load_memory()

    print("Memoria de Nova:")
    print(memory)

    add_history("Primer comando de Nova")

    print("Guardado correctamente")
