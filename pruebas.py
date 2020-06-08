edad=int(input("Ingresar edad: "))

if 0<edad<100:
    print("Edad ingresada correctamente")
    if edad<18:
        print("Usted es menor de edad.")
    else:
        print("Usted es mayor de edad.")
else:
    print("Numero no valido.")