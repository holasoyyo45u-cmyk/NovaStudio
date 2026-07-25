import json


def build_action(command):

    action = {
        "action": command.get("action"),
        "properties": {}
    }


    values = command.get(
        "detected_values",
        {}
    )


    if values.get("color"):

        action["properties"]["color"] = values["color"]


    if values.get("size"):

        action["properties"]["size"] = values["size"]


    if values.get("number"):

        action["properties"]["number"] = values["number"]


    return action



if __name__ == "__main__":

    example = {

        "action": "CreateSphere",

        "detected_values": {

            "color": "rojo",

            "size": 20

        }

    }


    result = build_action(example)


    print(
        json.dumps(
            result,
            indent=4,
            ensure_ascii=False
        )
    )
