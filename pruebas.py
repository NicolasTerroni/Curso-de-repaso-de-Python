# Encriptar con diccionarios
"""
Esto es un simple juego, las computadoras literalmente podrian
probar todas las combinaciones posibles para tratar de darle
sentido al mensaje. Si viajas al pasado y te llevas este codigo a una epoca
sin computadoras te puede servir para encriptar lo que quieras.
Suerte! (perdon estoy viendo la serie Dark)
Para practicar voy a encriptar mi llave privada SSH xDDDDDDDDDDD  
"""
#9w JaY1w1 ai3dm xw1w JaW Mwi aMdxbdIw1d 1a 8wi dxiwi U,a JwMdi CwxbaI1dD .aYd Id3d xdMd Ma tw83w 1aiwYYd88wY M,xCw 8d0bxw m aI3aI1bMbaI3d 1a8 8aI0,w!aZ 94 ?us5O4 rsO496sr ?rGjPujG5n4
KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}
def cifrar(mensaje):
    palabras = mensaje.split(" ")
    cifrado = []

    for palabra in palabras:
        palabra_cifrada = ""
        for letra in palabra:
            palabra_cifrada += KEYS[letra]
        
        cifrado.append(palabra_cifrada)

    return " ".join(cifrado)

def descifrar(mensaje):
    palabras = mensaje.split(" ")
    descifrado = []

    for palabra in palabras:
        palabra_descifrada = ""
        
        for letra in palabra:

            for key, value in KEYS.items():
                if value == letra:
                    palabra_descifrada += key
    
        descifrado.append(palabra_descifrada)

    return " ".join(descifrado)

#No podemos obtener directamente los valores, accedemos a lo largo de todas las llaves comparando si el valor coincide con la letra, ahi obtenemos la clave (o key)

def run():
    while True:
            print("---------------------------------------------------")
            print("            E N C R P I T A C I O N")
            print("---------------------------------------------------")
            print("""        Que desea hacer?

- Cifrar un mensaje------ Ingrese: 1
- Descifrar un mensaje--- Ingrese: 2
- Salir ----------------- Ingrese: 3
            """)
            
            command = int(input("-------> "))
            
            if command == 1:
                mensaje = str(input("Ingrese el mensaje a cifrar (solo alfanumerico): "))
                cifrado = cifrar(mensaje)
                print(f"MENSAJE CIFRADO: {cifrado}")
            elif command == 2:
                mensaje = str(input("Ingrese el mensaje a descifrar (solo alfanumerico): "))
                descifrado = descifrar(mensaje)
                print(f"MENSAJE DESCIFRADO: {descifrado}")
            elif command == 3:
                print("Hasta luego!")
                return False
            else:
                continue


if __name__ == "__main__":
    run()