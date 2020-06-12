#Diccionarios,iterar mostrando una lista de claififcaciones y calcular promedio de notas

calificaciones = {}
print("              Calificaciones                     ")
print("----------------------------------------------------")
calificaciones["Alumno-1"] = 9.3
calificaciones["Alumno-2"] = 8.8
calificaciones["Alumno-3"] = 9.0
calificaciones["Alumno-4"] = 7.9
calificaciones["Alumno-5"] = 9.2
lista = []
promedio = 0
for key, value in calificaciones.items():
    print(f"{key}.................................{value}")
    lista.append(value)
    promedio+=value
    
promedio = promedio/(len(lista))
print("----------------------------------------------------")
print(f"Promedio de calificaciones: {promedio}")
print("----------------------------------------------------")