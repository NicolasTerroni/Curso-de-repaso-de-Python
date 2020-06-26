import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

def run():
    for i in range(7,13):
        response = requests.get(f'https://xkcd.com/{i}')
        soup = BeautifulSoup(response.content, 'html.parser')
        image_container = soup.find(id='comic')

        image_url = image_container.find('img')['src']
        image_name = image_url.split('/')[-1]
        print(f'Descargando la imagen "{image_name}"')
        urlretrieve(f"https:{image_url}", image_name)

#ejecutar en consola o no te los baja en la ubicacion del archivo

if __name__ == "__main__":
    run() 