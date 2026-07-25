import json

from translator import translate
from action_builder import build_action
from Luau.generator import generate_luau



def run_nova():

    print("=== Nova Studio Core ===")
    print("Escribe 'salir' para cerrar")


    while True:

        user = input("\nTú > ")


        if user.lower() == "salir":
            print("Nova cerrado")
            break



        # 1. Entender comando

        command = translate(user)


        if command["action"] == "None":

            print("Nova: No entendí la orden")
            continue



        # 2. Crear acción

        action = build_action(command)



        print("\n--- Acción creada ---")

        print(
            json.dumps(
                action,
                indent=4,
                ensure_ascii=False
            )
        )



        # 3. Generar Luau

        luau = generate_luau(action)



        print("\n--- Código Luau ---")

        print(luau)




if __name__ == "__main__":

    run_nova()
