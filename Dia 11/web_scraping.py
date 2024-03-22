import bs4
import requests

# resultado = requests.get('https://www.escueladirecta.com')
resultado = requests.get('https://www.escueladirecta.com/courses/')

# print(resultado.text)

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

# print(sopa.select('title')[0].getText())

# parrafo_especial = sopa.select('p')[3].getText()

imagenes = sopa.select('.course-box-image')[0]['src']
print(imagenes)

for i in imagenes:
    print(i)
