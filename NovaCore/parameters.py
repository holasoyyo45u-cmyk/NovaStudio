import re


COLORS = [
    "rojo",
    "azul",
    "verde",
    "amarillo",
    "negro",
    "blanco",
    "morado",
    "rosa"
]


SIZES = {
    "pequeño": 2,
    "mediano": 5,
    "grande": 10,
    "gigante": 20
}



def extract_parameters(text):

    text = text.lower()

    result = {
        "color": None,
        "size": None,
        "number": None
    }


    # Detectar color
    for color in COLORS:

        if color in text:

            result["color"] = color
            break



    # Detectar tamaño
    for size, value in SIZES.items():

        if size in text:

            result["size"] = value
            break



    # Detectar números
    numbers = re.findall(
        r"\d+",
        text
    )

    if numbers:

        result["number"] = int(numbers[0])


    return result



if __name__ == "__main__":

    while True:

        text = input("Texto > ")

        print(
            extract_parameters(text)
        )
