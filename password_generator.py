# Generador automatico de passwords
import random

def generate_password():
    password = []
    while len(password) < 16:
        random_char = chr(random.randint(33,122))
        if random_char.isalnum() == True:
            password.append(random_char)
        else:
            continue
    password= "".join(password)
    return password

if __name__ == "__main__":
    password = generate_password()
    
print(password)