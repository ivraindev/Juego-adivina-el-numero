import random

def run():
    numero_aleatorio = random.randint (1, 100)
    numero_elegido = int(input("elige un número del 1 al 100: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print ("busca un número más grande")
        else:
            print ("busca un número más pequeño")
        numero_elegido = int (input("elige otro número: "))
    print ("Congratulation")


if __name__ == "__main__":
    run()