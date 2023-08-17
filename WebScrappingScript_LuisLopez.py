import json
from urllib.request import urlopen
import datetime
import boto3

def lambda_handler(event, context):
    # TODO implement
    

    
    # URL de la página a hacer web scraping
    url = 'https://www.eltiempo.com'
    
    # Realizamos la solicitud GET a la URL
    response = urlopen(url)
    
    # Verificamos si la solicitud fue exitosa
    if response.status == 200:
        # Leemos el contenido de la respuesta
        contenido = response.read().decode('utf-8')
        
        # Obtenemos el título de la página
        inicio_titulo = contenido.find('<title>')
        fin_titulo = contenido.find('</title>', inicio_titulo)
        titulo = contenido[inicio_titulo + 7:fin_titulo]
        
        # Generamos el nombre del archivo usando la fecha actual
        fecha_actual = datetime.datetime.now().strftime('%Y-%m-%d')
        
        aux = ' '
        nombre_archivo = f'{fecha_actual}.html'
        aux = nombre_archivo
        # Creamos y escribimos el contenido en el archivo
        nombre_archivo = '/tmp/' + nombre_archivo
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido)
        
    
        bucket_name = "yasuojonia"     
        
        
        s3 = boto3.client("s3")
        s3.upload_file(nombre_archivo, bucket_name, aux)
        
        print(f"El archivo '{aux}' se subio a '{bucket_name}'")
        
    else:
        print('Error al acceder a la página web.')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
