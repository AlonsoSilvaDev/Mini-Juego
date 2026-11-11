import random

OPCIONES = ["piedra", "papel", "tijera"]
GANA_A = {"piedra": "tijera", "papel": "piedra", "tijera": "papel"}


def piedra_papel_tijera():
    victorias = 0
    derrotas = 0
    print("Piedra, papel o tijera. Escribe 'salir' para terminar.")

    while True:
        jugador = input("Tu jugada: ").strip().lower()
        if jugador == "salir":
            break
        if jugador not in OPCIONES:
            print("Opción no válida.")
            continue

        pc = random.choice(OPCIONES)
        print(f"La computadora eligió: {pc}")

        if jugador == pc:
            print("Empate.")
        elif GANA_A[jugador] == pc:
            print("¡Ganaste esta ronda!")
            victorias += 1
        else:
            print("Perdiste esta ronda.")
            derrotas += 1

        print(f"Marcador -> Tú: {victorias} | PC: {derrotas}\n")

    print("Fin del juego.")


if __name__ == "__main__":
    piedra_papel_tijera()
