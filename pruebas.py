# Decoradores

def decorate(func):
    def wrapper():
        print("-----------------------------")
        print("Se va a realizar un calculo:")

        func()

        print("Calculo realizado.")
        print("-----------------------------")
    return wrapper

@decorate
def sum():
    print(2+2)

@decorate
def sub():
    print(5-2)

sum()
sub()