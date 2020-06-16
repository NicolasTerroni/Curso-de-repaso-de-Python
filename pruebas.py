""" 
Encontrar el primer caracter que no se repita adentro de un string.
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y 
"""

def finding_char(str_to_look):
    for letter in str_to_look:
        if str_to_look.count(letter) == 1:
            return letter
    return "_"

if __name__ == "__main__":
    str_to_look = str(input("Input string: "))
    
    result = finding_char(str_to_look)
    
    if result == "_":
        print("Todos los caracteres se repiten")
    else:
        print(f"El primer caracter no repetido fue {result}")