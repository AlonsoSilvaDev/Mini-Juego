import random

META = 50


def tirar_dados():
    return random.randint(1, 6) + random.randint(1, 6)


def dados_a_50():
    puntos_jugador = 0
    puntos_pc = 0
    print(f"Dados: gana quien llegue primero a {META} puntos.")

    while puntos_jugador < META and puntos_pc < META:
        input("\nPresiona Enter para tirar tus dados...")
        tirada = tirar_dados()
        puntos_jugador += tirada
        print(f"Tú sacaste {tirada}. Total: {puntos_jugador}")

        if puntos_jugador >= META:
            break

        tirada_pc = tirar_dados()
        puntos_pc += tirada_pc
        print(f"La PC sacó {tirada_pc}. Total: {puntos_pc}")

    if puntos_jugador >= META:
        print("\n¡Ganaste!")
    else:
        print("\nGanó la computadora.")


if __name__ == "__main__":
    dados_a_50()
