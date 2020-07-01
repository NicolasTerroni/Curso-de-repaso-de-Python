# convertir app de encriptacion al sistema binario

def cipher(message):
    ciphered = " ".join(format(x, 'b') for x in bytearray(message,'UTF-8'))
    return ciphered

def decipher(message):
    words = message.split(" ")
    deciphered = "".join(chr(int(x,base=2)) for x in words)
    return deciphered

def run():
    while True:
        command = input("""
        What do you want to do?
        1) Cipher.
        2) Decipher.
        3) Exit.
        ----------> """)
        if command == "1":
            message = str(input("Input message to cipher: "))
            res = cipher(message)
            print(f"Ciphered message: {res}")
            continue
        elif command == "2":
            message = str(input("Input a binary message: "))
            res = decipher(message)
            print(f"Deciphered message: {res}")
            continue
        elif command == "3":
            print("See you later!")
            return False
        else:
            print("There's no such command")


if __name__ == "__main__":
    print("------- W E L C O M E -------")
    run()