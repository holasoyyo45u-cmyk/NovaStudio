import json
import os


CONTEXT_FILE = "NovaCore/context.json"


def default_context():

    return {
        "last_object": None,
        "last_command": None,
        "last_parameters": {},
        "variables": {}
    }



def load_context():

    if not os.path.exists(CONTEXT_FILE):

        return default_context()


    with open(
        CONTEXT_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



def save_context(context):

    with open(
        CONTEXT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            context,
            file,
            indent=4,
            ensure_ascii=False
        )



def update_context(
    command,
    obj=None,
    parameters=None
):

    context = load_context()


    context["last_command"] = command


    if obj:

        context["last_object"] = obj


    if parameters:

        context["last_parameters"] = parameters


    save_context(context)



def set_variable(
    name,
    value
):

    context = load_context()

    context["variables"][name] = value

    save_context(context)



def get_variable(name):

    context = load_context()

    return context["variables"].get(name)



def get_context():

    return load_context()
