import json


COLORS = {
    "rojo": "Color3.fromRGB(255,0,0)",
    "azul": "Color3.fromRGB(0,0,255)",
    "verde": "Color3.fromRGB(0,255,0)",
    "blanco": "Color3.fromRGB(255,255,255)",
    "negro": "Color3.fromRGB(0,0,0)"
}



def generate_luau(action):

    code = ""


    if action["action"] == "CreatePart":

        size = action["properties"].get(
            "size",
            5
        )

        color = action["properties"].get(
            "color",
            "blanco"
        )


        code = f"""
local part = Instance.new("Part")

part.Size = Vector3.new({size},{size},{size})

part.Color = {COLORS.get(color, COLORS["blanco"])}

part.Anchored = true

part.Parent = workspace
"""


    elif action["action"] == "CreateSphere":

        size = action["properties"].get(
            "size",
            5
        )

        color = action["properties"].get(
            "color",
            "blanco"
        )


        code = f"""
local sphere = Instance.new("Part")

sphere.Shape = Enum.PartType.Ball

sphere.Size = Vector3.new({size},{size},{size})

sphere.Color = {COLORS.get(color, COLORS["blanco"])}

sphere.Anchored = true

sphere.Parent = workspace
"""


    return code.strip()



if __name__ == "__main__":

    test = {

        "action": "CreateSphere",

        "properties": {

            "color": "rojo",

            "size": 20

        }

    }


    print(generate_luau(test))
