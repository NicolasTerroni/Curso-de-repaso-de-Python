# Archivos externos, contar cuantas veces aparece una palabra en un archivo .css
from io import open
f = open("Desktop/prueba.txt","r")

list = f.readlines()
counter = 0
find = input("Ingrese palabra a buscar: ")
for line in list:
    if find in line:
        counter += 1

print(f"La palabra '{find}', aparece {counter} veces en el archivo.")

f.close()

"""
file: 

body
{
    color: #333;
    text-align: center;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 18px;
    margin: 0;
    padding: 0;
}

#cabecera
{
    text-align: center;
    background: #6c7181;
    box-shadow: 0px 2px 20px 0px rgba(0,0,0,0.5);
    color: white;
    font-weight: bold;
    margin: 0;
    padding: 0.5em;
}

#cabecera #logo
{
    text-align: center;
    width: 20px;
    vertical-align: middle;
}

#cabecera #tagline
{
    text-align: center;
    padding: 0 0 0 1em;
    font-weight: normal;
    font-size: 0.8em;
}


#container
{
    width: 70%;
    padding: 0;
    text-align: left;
    border: 1px solid #DDD;
    margin: 0 auto;
}

#container h1
{
    font-size: 20px;
}
#post
{
    text-align: center;
    padding: 1em;
}

#footer
{
    background: #777;
    color: white;
    text-align: center;
    padding: 0.5em;
}
"""