# Autor: Henzer Garcia
# Fecha: 16/03/2017
# Librerias necesarias: requests
import requests
import re

# Funcion que obtiene la data a partir de una url proporcionada.
# Parametros: url(str)
def get_data(url):
    # Descarga la data
    data = requests.get(url, headers={}).text
    print data
    data = validation(data)
    
    # La guarda en un archivo tsv
    file = open('data.tsv', 'w')
    file.write(data)
    file.close()

# Funcion para validar que contenga el formato indicado.
def validation(data):
    # Expresion regular que solo permite numeros separados por tabs
    regex = re.compile('(\d+[\t+\d]+\n)*')
    if regex.match(data) == None:
        print 'Data incorrecta'
        return ''
    else:
        return data
    
# Se llama a la funcion
print 'Descargando la data.'
get_data('https://www.random.org/integers/?num=100&min=1&max=100&col=4&base=10&format=plain&rnd=new')
print 'Archivo guardado'

