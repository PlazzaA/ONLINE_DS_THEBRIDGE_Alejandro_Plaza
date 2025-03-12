import random

def jugar():
    vidas = 2
    aleatorio = random.randrange(1, 6)
    while vidas > 0:
        intento = input("Di tu número")
    #    print(f"el número es {aleatorio}")
        if int(intento) != aleatorio:
            print("You lose.")
            vidas = vidas - 1
            print("Te quedan", vidas, "vidas")
        elif int(intento) == aleatorio:
            print("You win!")
            break
        else:
            print(f"Has perdido todas las vidas. El número aleatorio era {aleatorio}")

    mensaje = input("Quiere jugar de nuevo? (S/N)")
    if mensaje == "S":
        jugar()