# Funcion que sume recursivamente

def suma():
    num1 = int(input("Input first numer: "))
    num2 = int(input("Input second numer: "))
    res = num1+num2
    print(res)
    while True:
        command = input("Do you want to sum another number? (y/n)")
        if command == "y":
            new_number = int(input("Input new number: "))
            res = res + new_number
            print(res)
        else:
            return False

suma()