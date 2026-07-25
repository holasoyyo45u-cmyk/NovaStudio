from translator import translate
from action_builder import build_action
from Luau.generator import generate_luau

texto = "crea una esfera roja gigante"

print("Entrada:")
print(texto)


comando = translate(texto)

print("\nComando:")
print(comando)


accion = build_action(comando)

print("\nAcción:")
print(accion)


codigo = generate_luau(accion)

print("\nLuau generado:")
print(codigo)
