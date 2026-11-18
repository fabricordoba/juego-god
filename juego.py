import random

def jugar():
    numero_secreto = random.randint(1, 20)
    intentos = 0

    print("¡Bienvenido a Adivina el Número!")
    print("Estoy pensando en un número entre el 1 y el 20.")

    while True:
        try:
            adivinanza = int(input("\nIngresa tu número: "))
            intentos += 1

            if adivinanza < numero_secreto:
                print("Muy bajo. Intenta con un número más grande.")
            elif adivinanza > numero_secreto:
                print("Muy alto. Intenta con un número más pequeño.")
            else:
                print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, escribe solo números válidos.")

jugar()

