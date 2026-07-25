import json
import os

CONTEXT_FILE = "NovaCore/context.json"


def load_context():

    if not os.path.exists(CONTEXT_FILE):
        return {
            "last_object": None,
            "last_command": None
        }

    with open(CONTEXT_FILE, "r", encoding="utf-8") as file:
        return json.load(file)



def save_context(context):

    with open(CONTEXT_FILE, "w", encoding="utf-8") as file:
        json.dump(
            context,
            file,
            indent=4,
            ensure_ascii=False
        )



def update_context(command, obj=None):

    context = load_context()

    context["last_command"] = command

    if obj:
        context["last_object"] = obj

    save_context(context)



def get_context():

    return load_context()
