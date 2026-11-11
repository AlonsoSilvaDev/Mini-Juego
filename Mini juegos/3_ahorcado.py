import random

PALABRAS = ["python", "programa", "computadora", "teclado", "variable", "portafolio"]
MAX_ERRORES = 6


def ahorcado():
    palabra = random.choice(PALABRAS)
    adivinadas = set()
    errores = 0

    print("Juego del ahorcado.")

    while errores < MAX_ERRORES:
        mostrada = " ".join(letra if letra in adivinadas else "_" for letra in palabra)
        print(f"\n{mostrada}")
        print(f"Errores: {errores}/{MAX_ERRORES}")

        if "_" not in mostrada:
            print("¡Ganaste! La palabra era:", palabra)
            return

        letra = input("Escribe una letra: ").strip().lower()
        if len(letra) != 1 or not letra.isalpha():
            print("Escribe solo una letra.")
            continue
        if letra in adivinadas:
            print("Ya la usaste.")
            continue

        adivinadas.add(letra)
        if letra not in palabra:
            errores += 1
            print("Esa letra no está.")

    print(f"\nPerdiste. La palabra era: {palabra}")


if __name__ == "__main__":
    ahorcado()
