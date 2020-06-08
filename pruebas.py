# -*- coding: utf-8 -*-
def foering_exchange(amount):
    ars_to_usd_rate= 91
    return amount / ars_to_usd_rate

def run():
    print("CALCULADORA DE DIVISAS - by NicolasTerroni")
    print("Convierte pesos argentinos a dolares.")
    print("")

run()

amount=float(input("What amount of pesos do you want to convert to U$S?: "))

resultado = foering_exchange(amount)

print(f"${amount} pesos argentinos, son ${resultado} dolares.")