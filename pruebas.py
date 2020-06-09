# Hacer un programa que calcule el factorial de un numero usando funciones recursivas

def calcula_fact(num):
    #0 es nuestro caso base, si no lo hubieramos establecido entramos en bucle infinito
    if num == 0:
        return 1
    return num*calcula_fact(num-1)
#mi error al pensar este ejercicio fue creer que el return acumulaba los resultados, cuando en realidad solo multiplicaba en ciclo por el numero anterior hasta que al ser 0 le digamos que devuelva 1 (LOGIC)
num = int(input("Ingrese el numero: "))

res = calcula_fact(num)
print(res)
