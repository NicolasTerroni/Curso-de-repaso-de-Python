# Utilizando el programa del profesor para generar numeros aleatorios y llevarnos a el, debemos modificarlo para hacerlo mas complejo
import random
def play():
    number_found = False
    From = int(input("Desde que numero queres jugar? ----> "))
    To = int(input("Hasta que numero queres jugar? ----> "))
    random_number = random.randint(From, To)
    while not number_found:
        number = int(input('Intenta un número：'))
        if number == random_number:
            print('Felicidades. Encontraste el número')
            number_found = True
        elif number > random_number:
            print('El número es más pequeño')
        else:
            print('El número es más grande')

again = True
while again:
    play()
    play_again = input("Jugar de nuevo? Y/N ---> ")
    if play_again.upper() == "Y":
        again = True
    elif play_again.upper() == "N":
        again = False
    else:
        print("Debes ingresar Y o N. ")
"""
- Ahora podemos establecer desde donde a donde se generara el rango.
- Podemos elegir si jugar de nuevo o no

TARDE COMO MEDIA HORA. PERO APRENDI UN POCO MAS!

"""