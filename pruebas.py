# Busqueda binaria, tambien agregamos que la ordene y la imprima antes del resultado.

list = [24,8,82,1,54,2,6,4,47,18,7,15]

def binary(list, get_number, low, high):
    list.sort()
    if low > high:
        # primer caso base (si no encontramos el numero)
        return False
    
    mid = (low + high) // 2
    
    if list[mid] == get_number:
        # segundo caso base (si encontramos el numero)
        return True
    elif list[mid] > get_number:
        return binary(list,get_number,low,mid - 1)
    else:
        return binary(list,get_number,mid + 1,high)

get_number = int(input("Danos el numero para buscar: "))
res = binary(list,get_number,0, len(list)-1)

if res is True:
    print(list)
    print(f"Si se encuentra en la lista.")
else:
    print(list)
    print("El numero no esta en la lista.")
