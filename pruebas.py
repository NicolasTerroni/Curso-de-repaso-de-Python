# Detectar si una palabra es un palindromo, lo voy a hacer en ingles porque la vida lo quiso asi

word = input("Input word -------------> ")
if word == word[::-1]:
    print(f"YES! '{word}' IS A PALINDROME")
else:
    print(f"No,'{word}' isn't a palindrome. You suck at this.")

""" try "larutanosaportootropasonatural" 
        "severlasalreves"
    sorry i dont know anyone in english
"""