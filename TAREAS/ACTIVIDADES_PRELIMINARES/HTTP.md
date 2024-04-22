<H1>Programación HTTP</H1> 

# INTRODUCCIÓN:

<p>En esta actividad se presentará el protocolo HTTP y veremos como podemos recuperar y manipularcontenido web usando Python. También echamos un vistazo a la biblioteca estándar de urllib, asícomo a request y los paquetes httpx. Además, veremos el módulo request de terceros, que es unaalternativa muy popular a urllib. También veremos mecanismos de autenticación HTTP y cómopodemos administrarlos con el módulo request.Esta actividad nos proporcionará la base para familiarizarnos con diferentes alternativas dentro dePython cuando necesitemos usar un módulo que proporcione diferentes funcionalidades pararealizar solicitudes a un servicio web o API REST</p>

## Marco teórico:

<p>El protocolo HTTPHTTP es un protocolo de capa de aplicación que define las reglas que los clientes, proxies yservidores deben seguir para el intercambio de información. Básicamente consta de doselementos:</p>

<p>1. Una solicitud realizada por el cliente, que solicita al servidor un recurso específicoespecificado por una URL.
2. Una respuesta, enviada por el servidor, que suministra el recurso solicitado por el cliente.
3. 
El protocolo HTTP es un protocolo de transferencia de datos de hipertexto sin estado que noalmacena la información intercambiada entre el cliente y el servidor. Al ser un protocolo sin estadopara almacenar información relacionada con una transacción HTTP, es necesario recurrir a otrastécnicas para almacenar datos de intercambio, como cookies (valores almacenados en el lado delcliente) o sesiones (espacios de memoria temporal reservados para almacenar información sobreuno o más transacciones HTTP en el lado del servidor).Los servidores devuelven un código HTTP que indica el resultado de una operación solicitada por el cliente. Además, las solicitudes pueden usar encabezados para incluir información adicional tanto enlas solicitudes como en las respuestas. También es importante tener en cuenta que el protocoloHTTP utiliza sockets de bajo nivel para establecer una conexión cliente-servidor.En Python, tenemos la posibilidad de usar un módulo de nivel superior, que nos abstrae del serviciode socket de bajo nivel.</p>

## METODOLOGÍA
<p>Para empezar, nos dirigimos a colab y exploramos el [código FUENTE](https://github.com/kapumota/Actividades-CC8280/tree/main/Sockets/tcp) ,  luego antes de consumir un servicio web, tenemos que importar lo siguiente:</p>

```
#! /usr/bin/env python3
import urllib.request
import urllib.parse
```
<p>Usando la función urlopen, se genera un objeto similar a un archivo en el que leer de la URL. Esteobjeto tiene métodos como read, readline, readlines y close, que funcionan exactamente igual que en los objetos de archivo, aunque en realidad estamos trabajando con métodos que nos abstraendel uso de sockets de bajo nivel.La función urlopen proporciona un parámetro de datos opcional para enviar información adirecciones HTTP utilizando el método POST, donde la propia solicitud envía parámetros.Este parámetro es una cadena con la codificación correcta:</p>
 
  ```
  urllib.request.urlopen (url, data = None, [timeout,] *, cafile = None,capath = None, cadefault = False, contexto = None)
  ```
<p>En el siguiente script, estamos usando el método urlopen para hacer una solicitud POST usando elparámetro de datos como diccionario.Revisa el código urllib_post_ request.py y analiza los resultados.Recuperar el contenido de una URL es un proceso sencillo cuando se hace con urllib. Puede abrir elintérprete de Python y ejecutar las siguientes instrucciones:</p>

```
from urllib.request import urlopenresponse = urlopen('https://elearning.uni.edu/')response...response.readline()
```

Aquí estamos usando el método ```urllib.request.urlopen () ``` para enviar una solicitud y recibir unarespuesta para el recurso en una dirección web, en este caso una página HTML.Luego imprimimos la primera línea del HTML que recibimos, con el método``` readline()``` del objeto derespuesta. El método ```urlopen ()``` también admite la especificación de un tiempo de espera para lasolicitud que representa el tiempo de espera en la solicitud; es decir, si la página tarda más de lo queindicamos, dará como resultado un error.En el ejemplo podemos ver que el método``` urlopen ()``` devuelve una instancia de la clase ```http.client.HTTPResponse.``` El objeto de respuesta nos devuelve información con datos solicitados yde respuesta.Si obtenemos una respuesta en formato JSON, podemos usar el módulo Python json para procesar larespuesta``` json```.Revisa el código ```json_response.py```, explica los resultados.

# ANÁLISIS
## 1. Análisis,Ejecución y Resultados del código : request_http_client.py 

Código:
```
import http.client

connection = http.client.HTTPConnection("www.google.com")
connection.request("GET", "/")
response = connection.getresponse()
print(type(response))
print(response.status, response.reason)

if response.status == 200:
    data = response.read()
    print(data)
```
Resultados:
```
<class 'http.client.HTTPResponse'>
200 OK
b'[...]
```
Análisis:

<p>El código que proporcionaste es un ejemplo de cómo hacer una solicitud HTTP a un servidor utilizando el módulo http.client en Python. Analicemos cada parte:

Importación del módulo http.client:
La primera línea importa el módulo http.client, que proporciona funcionalidades para trabajar con conexiones HTTP.
Estableciendo una conexión HTTP:
La línea connection = http.client.HTTPConnection("www.google.com") crea una conexión HTTP con el servidor en www.google.com.
Realizando una solicitud GET:
La línea connection.request("GET", "/") envía una solicitud HTTP GET al servidor para obtener la página raíz (“/”) del sitio web.
Obteniendo la respuesta:
La línea response = connection.getresponse() obtiene la respuesta del servidor.
response es un objeto que contiene información sobre la respuesta, como el estado (código de estado) y los datos devueltos por el servidor.
Verificando el estado de la respuesta:
La línea print(response.status, response.reason) muestra el código de estado y la razón de la respuesta.
Si el estado es 200, significa que la solicitud fue exitosa (OK).
Leyendo los datos de la respuesta:
Si la respuesta es exitosa (estado 200), la línea data = response.read() lee los datos devueltos por el servidor.
En este caso, data contendría el contenido de la página raíz de Google.
El método get response () devuelve una instancia de la clase
http.client.HTTPResponse. El objeto de respuesta devuelve información sobre los datos de recursos
solicitados y las propiedades y metadatos de respuesta.  
El método read() nos permite leer los datos de recursos solicitados y devolver el número
especificado de bytes.</p>

## 2. Análisis,ejecución y resultados del código: urllib_post_request.py

Código:
```
import urllib.request
import urllib.parse

#POST request

data_dictionary = {"id": "0123456789"}
data = urllib.parse.urlencode(data_dictionary)
data = data.encode('ascii')

with urllib.request.urlopen("http://httpbin.org/post", data) as response:
	print(response.read().decode('utf-8'))
```

Resultado:
```
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "id": "0123456789"
  }, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Content-Length": "13", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-6625669a-28ab0114569085063d5b7526"
  }, 
  "json": null, 
  "origin": "34.82.183.36", 
  "url": "http://httpbin.org/post"
}
```
Análisis:

El código que proporcionado realiza una solicitud POST a la URL http://httpbin.org/post utilizando el módulo urllib de Python.Aquí describimos las fases del código:

Importación de módulos:
import urllib.request: Importa el módulo para abrir y leer URLs.
import urllib.parse: Importa el módulo para parsear URLs.
Creación de datos para la solicitud POST:
data_dictionary = {"id": "0123456789"}: Crea un diccionario con los datos que se enviarán en la solicitud POST.
data = urllib.parse.urlencode(data_dictionary): Codifica el diccionario en una cadena de consulta.
data = data.encode('ascii'): Codifica la cadena de consulta en bytes, utilizando la codificación ASCII.
Envío de la solicitud POST y recepción de la respuesta:
with urllib.request.urlopen("http://httpbin.org/post", data) as response:: Abre la URL como un objeto de respuesta, pasando los datos codificados de la solicitud POST.
print(response.read().decode('utf-8')): Lee la respuesta y la decodifica de UTF-8 a una cadena de caracteres, luego la imprime.
El resultado es un objeto JSON que contiene varios campos:

"args": {}: Vacío porque no se enviaron argumentos en la URL.
"data": "": Vacío porque los datos se enviaron en el cuerpo del formulario.
"files": {}: Vacío porque no se enviaron archivos.
"form": {"id": "0123456789"}: Muestra los datos del formulario que se enviaron, en este caso, un ID.
"headers": Contiene los encabezados de la solicitud, incluyendo el tipo de contenido, longitud del contenido, y el agente de usuario.
"json": null: No hay datos JSON porque los datos se enviaron como formulario.
"origin": "34.82.183.36": La dirección IP desde la que se hizo la solicitud.
"url": "http://httpbin.org/post": La URL a la que se hizo la solicitud.
## 3.Análisis,Ejecución y Resultados del código : json_response.py


3. Analisis,ejecución  y resultados de  json_response.py:
   Código:
```
   #!/usr/bin/env python3

import urllib.request
import json

url= "http://httpbin.org/get"

with urllib.request.urlopen(url) as response_json:
    data_json= json.loads(response_json.read().decode("utf-8"))
    print(data_json)
```
   REesultados:
```
   {'args': {}, 'headers': {'Accept-Encoding': 'identity', 'Host': 'httpbin.org', 'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36', 'X-Amzn-Trace-Id': 'Root=1-6625669f-335f87ba08793ee951145325'}, 'origin': '34.82.183.36', 'url': 'http://httpbin.org/get'}
```
Analisis:
Bien! Examinemos a cuidado cada línea de este código, si bien , estamos comenzando con la importación de urllib.request para abrir la dirección URL y comunicarnos con la red, también fusionamos archivos JSON.

Esta Url: “http://httpbin.org/get”.
solicita al protocolo HTTP abrirla la dirección mediante variable url, la cual se lee en formato JSON, a través de decodificación en  response_json.read().decode("utf-8").

Después se suben los datos JSON, con ayuda de json.loads(), los cuales precisamente transforman en diccionario de python la respuesta obtenida, para posteriormente, almacenarse en data_json.

En el output, los datos contenidos mostrados provienen de dicho diccionario data_json.

Adicionalmente, este diccionario, muestra los detalles de la solicitud HTTP GET, enviada a httpbin.org, donde se mostraron resumidos a continuación:

 ENCABEZADO:el diccionario con los encabezados HTTP enviados por el cliente.
DIRECCIÓN IP DE CLIENTE: 34.82.183.36(origin)
SIN ARGUMENTOS DE CONSULTA.


## 4.Análisis,Ejecución y Resultados del código : get_headers_response_request.py
codigo:
```

import urllib.request
from urllib.request import Request

url="http://python.org"
USER_AGENT = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36'

def chrome_user_agent():
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', USER_AGENT)]
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(url)
    print("Response headers")
    print("--------------------")
    for header,value in response.getheaders():
        print(header + ":" + value)

    request = Request(url)
    request.add_header('User-agent', USER_AGENT)
    print("\nRequest headers")
    print("--------------------")
    for header,value in request.header_items():
	    print(header + ":" + value)

if __name__ == '__main__':
    chrome_user_agent()
```

Resultado:
```
User-agent:Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36

```
Response headers
--------------------
Connection:close
Content-Length:50792
Content-Type:text/html; charset=utf-8
X-Frame-Options:SAMEORIGIN
Via:1.1 varnish, 1.1 varnish
Accept-Ranges:bytes
Date:Sun, 21 Apr 2024 19:19:02 GMT
Age:318
X-Served-By:cache-iad-kiad7000025-IAD, cache-bfi-krnt7300057-BFI
X-Cache:HIT, HIT
X-Cache-Hits:497, 3
X-Timer:S1713727143.633481,VS0,VE0
Vary:Cookie
Strict-Transport-Security:max-age=63072000; includeSubDomains; preload

Request headers
------
User-agent:Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36

Análisis:
En la secuencia de comandos anterior, estamos personalizando el encabezado User-agent con una
versión específica del navegador Chrome. Para cambiar el User-agent, hay dos alternativas. El
primero es usar la propiedad addheaders del objeto opener. El segundo implica usar el método
add_header () del objeto Request para agregar encabezados al mismo tiempo que creamos el objeto
request.
El código anterior te enseña a usar encabezados en el paquete urllib.request para obtener
información sobre el servidor web.

## 5.Análisis,Ejecución y Resultados del código : get_emails_url_request.py 

Código:
```
import urllib.request
import re

USER_AGENT = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36'

url =  input("Enter url:http://")


opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', USER_AGENT)]
urllib.request.install_opener(opener)

response = urllib.request.urlopen('http://'+url)
html_content= response.read()
pattern = re.compile("[-a-zA-Z0-9._]+[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+.[a-zA-Z0-9_.]+")
mails = re.findall(pattern,str(html_content))
print(mails)
```
Resultado:

```
Enter url:http://google.com
[]
```
Análisis:
## 6.Análisis,Ejecución y Resultados del código :  download_file.py 
Código:
```
#!/usr/bin/python

import urllib.request

print("Empezando la descarga....")

url="https://www.python.org/static/img/python-logo.png"

#download file with urlretrieve
urllib.request.urlretrieve(url, "python.png")

#download file with urlopen
with urllib.request.urlopen(url) as response:
    print("Estado:", response.status)
    print( "Descargando python.png")
    with open("python.png", "wb" ) as image:
        image.write(response.read())
```

Resultado:
```
Empezando la descarga....
Estado: 200
Descargando python.png
```
Análisis:
# Análisis
Primeramente se ha llevado a cabo una importación de urllib.request para abrir e interpretar la información contenida en dicha URL con urllib.request.

Porsupuesto! Seguirá con el empezando la descarga en cuando el proceso esté en inicio.

A posteriori, se implementará la variable url, una dirección del archivo png a descargar.

En seguida, se procede a descargar el contenido de URL, y lo que hace es guardarlo en un local file de nombre python.png, usando urlretrieve.

Lo que sucede a continuación es muy interesante, ya que en el código se sobreescribe la descarga de la imagen dos veces, ahora es el turno de urlopen, con lo cual tenemos la siguiente ruta:
1. Se abre la URL, luego pasamos a obtener la respuesta dentro de with.
2. Para seguir la línea de este análisis, se imprime el estado de respuesta HTTP, mediante print("Estado:", response.status). Con el resultado de 200, porque esta operación fue exitosa.

En este momento, se abre el archivo previamente creado de python.png en modo binario de escritura ("wb"), aplicando with open("python.png", "wb") as image.

Por consiguiente, se lee el contenido de respuesta y es adjudicado a python.png, con el comando image.write(response.read()).

## 7.Análisis,Ejecución y Resultados del código :count_words_file.py
Código:
```
#6 count_words_file.py 
#!/usr/bin/env python3

import urllib.request
import urllib.error

def count_words_file(url):
    try:
        file_response = urllib.request.urlopen(url)
    except urllib.error.URLError as error:
        print('Exception', error)
        print('reason', error.reason)
    else:
        content = file_response.read()
        return len(content.split())


print(count_words_file('https://www.gutenberg.org/cache/epub/2000/pg2000.txt'))

count_words_file('https://not-exists.txt')
```


Resultado:
````
Exception HTTP Error 504: Gateway Time-out
reason Gateway Time-out
None
Exception <urlopen error [Errno -2] Name or service not known>
reason [Errno -2] Name or service not known
````
Análisis:
El script `count_words_file.py` está diseñado para contar la cantidad de palabras en un archivo de texto accesible a través de una URL. Vamos a su exploración!

1. Shebang y Módulos:
   - `#!/usr/bin/env python3`: Shebang para indicar que el script debe ejecutarse con Python 3.
   - `import urllib.request`: Importa el módulo para abrir URLs.
   - `import urllib.error`: Importa el módulo para manejar excepciones relacionadas con URLs.

2. Definición de la Función `count_words_file`:
   - `def count_words_file(url)`: Define una función que toma una URL como argumento.

3. Manejo de Excepciones:
   - `try`: Intenta ejecutar el código que podría lanzar una excepción.
   - `file_response = urllib.request.urlopen(url)`: Intenta abrir la URL y obtener una respuesta.

4. Excepción URLError:
   - `except urllib.error.URLError as error`: Captura la excepción `URLError` si ocurre.
   - `print('Exception', error)`: Imprime el tipo de excepción.
   - `print('reason', error.reason)`: Imprime la razón de la excepción.

5. Procesamiento de la Respuesta:
   - `else`: Si no hay excepciones, ejecuta el siguiente bloque de código.
   - `content = file_response.read()`: Lee el contenido de la respuesta.
   - `return len(content.split())`: Divide el contenido en palabras y devuelve la cantidad.

6. Llamadas a la Función:
   - `print(count_words_file('https://www.gutenberg.org/cache/epub/2000/pg2000.txt'))`: Imprime la cantidad de palabras del archivo de texto de Project Gutenberg.
   - `count_words_file('https://not-exists.txt')`: Intenta contar las palabras de una URL que no existe.

Resultados:
- Primera Llamada: No se muestra el resultado, pero si la URL es correcta, debería devolver el número de palabras del texto.
- Segunda Llamada: Muestra dos excepciones debido a problemas al intentar acceder a la URL:
   - `Exception HTTP Error 504: Gateway Time-out`: Indica que hubo un tiempo de espera de la puerta de enlace.
   - `reason Gateway Time-out`: La razón del error 504.
   - `None`: Se imprime porque la función no devuelve nada cuando se captura una excepción.
   - `Exception <urlopen error [Errno -2] Name or service not known>`: Indica que el nombre de la URL no se pudo resolver.
   - `reason [Errno -2] Name or service not known`: La razón del error de resolución de nombre.

Este script es útil para contar palabras en archivos de texto en línea, pero debe manejarse adecuadamente para evitar errores como los mostrados.


## 8.Análisis,Ejecución y Resultados del código :  request_headers.py
Código:
```
#7request_headers.py
#!/usr/bin/env python3

import requests, json


domain = input("Ingresa el hostname http://")

response = requests.get("http://"+domain)

print(response.json)

print("Status codigo: "+str(response.status_code))

print("Headers respuesta: ")
for header, value in response.headers.items():
  print(header, '-->', value)
  
print("Solicitud headers  : ")
for header, value in response.request.headers.items():
  print(header, '-->', value)
```

Resultado:
```
Ingresa el hostname: s1
---------------------------------------------------------------------------
gaierror                                  Traceback (most recent call last)
/usr/local/lib/python3.10/dist-packages/urllib3/connection.py in _new_conn(self)
    202         try:
--> 203             sock = connection.create_connection(
    204                 (self._dns_host, self.port),

18 frames
gaierror: [Errno -2] Name or service not known

The above exception was the direct cause of the following exception:

NameResolutionError                       Traceback (most recent call last)
NameResolutionError: <urllib3.connection.HTTPConnection object at 0x7c1a26372830>: Failed to resolve 's1' ([Errno -2] Name or service not known)


The above exception was the direct cause of the following exception:

```
Análisis:
El script `#7request_headers.py` tiene como objetivo realizar una solicitud HTTP GET a un dominio proporcionado por el usuario y luego imprimir varios detalles de la respuesta y la solicitud. Aquí está el análisis del código y del error que se produjo:

Análisis del Código:
1. **Importación de Módulos**:
   - `import requests`: Importa la biblioteca `requests` para realizar solicitudes HTTP.
   - `import json`: Importa la biblioteca `json` para trabajar con datos en formato JSON.
   - 
2. Solicitud de Hostname:
   - `domain = input("Ingresa el hostname http://")`: Pide al usuario que ingrese un hostname, pero la instrucción es confusa porque sugiere que se debe incluir "http://", lo cual no es necesario.

3. Ralización de la Solicitud GET:
   - `response = requests.get("http://" + domain)`: Concatena "http://" con el hostname ingresado y realiza una solicitud GET.

4. Impresión de la Respuesta JSON**:
   - `print(response.json)`: Intenta imprimir la función `json` del objeto `response`. Debería ser `response.json()` para obtener el contenido JSON de la respuesta.

5. Impresión del Código de Estado:
   - `print("Status codigo: " + str(response.status_code))`: Imprime el código de estado de la respuesta HTTP.

6. Impresión de Headers de la Respuesta:
   - `for header, value in response.headers.items()`: Itera e imprime los headers de la respuesta HTTP.

7. Impresión de Headers de la Solicitud:
   - `for header, value in response.request.headers.items()`: Itera e imprime los headers de la solicitud HTTP.

Análisis del Error:
- El error `gaierror: [Errno -2] Name or service not known` indica que el hostname 's1' no se pudo resolver. Esto significa que el sistema no pudo encontrar la dirección IP asociada con el hostname 's1'.
- La excepción `NameResolutionError` es consecuencia directa del error anterior y confirma que hubo un problema al resolver el nombre del servicio o hostname.

Resultado:
- Dado que el hostname 's1' no se pudo resolver, el script no pudo realizar la solicitud HTTP y, por lo tanto, no pudo imprimir los detalles de la respuesta ni de la solicitud.

Recomendaciones:
- Asegurar de que el hostname ingresado sea correcto y accesible.
- Corregir la instrucción de entrada para que no sugiera incluir "http://".
- Cambiar `print(response.json)` a `print(response.json())` para obtener el contenido JSON de la respuesta.
- Implementar manejo de excepciones para capturar y manejar errores como este de manera más elegante.

## 9.Análisis,Ejecución y Resultados del código : archivo get_images_links_url.py 
Código
````
#archivo get_images_links_url.py 
#!/usr/bin/env python3
    
import requests
import re

url = input("Ingresa URL > ")
var = requests.get(url).text

print("Imagenes:")
print("#########################")
for image in re.findall("<img (.*)>",var):
    for images in image.split():
        if re.findall("src=(.*)",images):
            image = images[:-1].replace("src=\"","")
            if(image.startswith("http")):
                print(image)
            else:
                print(url+image)

print("#########################")
print("Links:")
print("#########################")
for link,name in re.findall("<a (.*)>(.*)</a>",var):
    for a in link.split():
        if re.findall("href=(.*)",a):
            url_image = a[0:-1].replace("href=\"","")
            if(url_image.startswith("http")):
                print(url_image)
            else:
                print(url+url_image)
````
Resultado:
```

#archivo testing_api_rest_get_method.py
import requests, json

response = requests.get("http://httpbin.org/get",timeout=5)

print("HTTP Status Code: " + str(response.status_code))
print(response.headers)

if response.status_code == 200:


HTTP Status Code: 200
{'Date': 'Sun, 21 Apr 2024 21:27:52 GMT', 'Content-Type': 'application/json', 'Content-Length': '305', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}
('args', {})
('headers', {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.31.0', 'X-Amzn-Trace-Id': 'Root=1-662584d8-2549d8660ce8a71f1d6875f3'})
('origin', '34.82.183.36')
('url', 'http://httpbin.org/get')
Headers response: 
Date --> Sun, 21 Apr 2024 21:27:52 GMT
Content-Type --> application/json
Content-Length --> 305
Connection --> keep-alive
Server --> gunicorn/19.9.0
Access-Control-Allow-Origin --> *
Access-Control-Allow-Credentials --> true
Headers request : 
User-Agent --> python-requests/2.31.0
Accept-Encoding --> gzip, deflate
Accept --> */*
Connection --> keep-alive
Server:gunicorn/19.9.0
```

Análisis:
El código proporcionado en el archivo `get_images_links_url.py` realiza una solicitud HTTP GET a una URL proporcionada por el usuario y luego extrae e imprime las imágenes y los enlaces encontrados en la página. Aquí está el análisis del código y los resultados:

Análisis del Código:
1. Se solicita al usuario que ingrese una URL.
2. Se realiza una solicitud GET a la URL proporcionada.
3. Se utiliza expresiones regulares para buscar imágenes (`<img>`) y enlaces (`<a>`).
4. Las imágenes se imprimen directamente si comienzan con "http". De lo contrario, se completa la URL base con la ruta de la imagen.
5. Los enlaces se imprimen de manera similar.

Resultados:
- Dado que la URL proporcionada es una imagen (`https://i2.wp.com/www.itgrarte.org/wp-content/uploads/2019/05/Redes-de-Internet.jpg?fit=1120%2C581&ssl=1`), no se encontraron imágenes ni enlaces en la página.
- Por lo tanto, las secciones "Imagenes" y "Links" están vacías.

Recomendaciones:
- Probar el código con una página web que contenga imágenes y enlaces para obtener resultados más significativos.
- Asegurarnos de manejar excepciones en caso de que la solicitud falle o la URL sea incorrecta.
- Considerar agregar comentarios o documentación para explicar el propósito y el funcionamiento del código.


## 10.Ejecución y Resultados del código : archivo testing_api_rest_get_method.py 

Código:
```
#archivo testing_api_rest_get_method.py
import requests, json

response = requests.get("http://httpbin.org/get",timeout=5)

print("HTTP Status Code: " + str(response.status_code))
print(response.headers)

if response.status_code == 200:

	results = response.json()
	for result in results.items():
		print(result)

	print("Headers response: ")
	for header, value in response.headers.items():
		print(header, '-->', value)

	print("Headers request : ")
	for header, value in response.request.headers.items():
		print(header, '-->', value)

	print("Server:" + response.headers['server'])
else:
	print("Error code %s" % response.status_code)
```
Resultado:
````
HTTP Status Code: 200
{'Date': 'Sun, 21 Apr 2024 21:27:52 GMT', 'Content-Type': 'application/json', 'Content-Length': '305', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}
('args', {})
('headers', {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.31.0', 'X-Amzn-Trace-Id': 'Root=1-662584d8-2549d8660ce8a71f1d6875f3'})
('origin', '34.82.183.36')
('url', 'http://httpbin.org/get')
Headers response: 
Date --> Sun, 21 Apr 2024 21:27:52 GMT
Content-Type --> application/json
Content-Length --> 305
Connection --> keep-alive
Server --> gunicorn/19.9.0
Access-Control-Allow-Origin --> *
Access-Control-Allow-Credentials --> true
Headers request : 
User-Agent --> python-requests/2.31.0
Accept-Encoding --> gzip, deflate
Accept --> */*
Connection --> keep-alive
Server:gunicorn/19.9.0****
````
Análisis:
El código en el archivo `testing_api_rest_get_method.py` realiza una solicitud HTTP GET a la URL `http://httpbin.org/get` utilizando la biblioteca `requests`. Aquí está el análisis del código y los resultados obtenidos:

Análisis del Código:
1. Se realiza una solicitud GET a la URL `http://httpbin.org/get`.
2. Se verifica el código de estado de la respuesta:
   - Si es 200, se procesa la respuesta.
   - Si no es 200, se imprime un mensaje de error.

3. Se extraen y se imprimen los siguientes detalles de la respuesta:
   - Código de estado HTTP.
   - Headers de la respuesta.
   - Datos JSON de la respuesta (si existen).

Resultados:
- El código de estado HTTP es 200, lo que indica una respuesta exitosa.
- Los headers de la respuesta incluyen información como el tipo de contenido, la longitud del contenido, etc.
- No hay datos JSON en la respuesta (el campo "args" está vacío).
- El servidor utilizado es "gunicorn/19.9.0".

## 11.Análisis,Ejecución  Resultados del código :testing_api_rest_post_method.py.
Código:
````
#10testing_api_rest_post_method.py.
#!/usr/bin/env python3

import requests,json
data_dictionary = {"id": "0123456789"}
headers = {"Content-Type" : "application/json","Accept":"application/json"}
response = requests.post("http://httpbin.org/post",data=data_dictionary,headers=headers,json=data_dictionary)
print("HTTP Status Code: " + str(response.status_code))

print(response.headers)

if response.status_code == 200:

	results = response.json()
	for result in results.items():
		print(result)

	print("Headers response: ")
	for header, value in response.headers.items():
		print(header, '-->', value)

	print("Headers request : ")
	for header, value in response.request.headers.items():
		print(header, '-->', value)

	print("Server:" + response.headers['server'])
else:
	print("Error code %s" % response.status_code)
`````
Resultado:
```

HTTP Status Code: 200
{'Date': 'Sun, 21 Apr 2024 21:42:20 GMT', 'Content-Type': 'application/json', 'Content-Length': '465', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}
('args', {})
('data', 'id=0123456789')
('files', {})
('form', {})
('headers', {'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '13', 'Content-Type': 'application/json', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.31.0', 'X-Amzn-Trace-Id': 'Root=1-6625883c-4989c5065834efd617d07f23'})
('json', None)
('origin', '34.82.183.36')
('url', 'http://httpbin.org/post')
Headers response: 
Date --> Sun, 21 Apr 2024 21:42:20 GMT
Content-Type --> application/json
Content-Length --> 465
Connection --> keep-alive
Server --> gunicorn/19.9.0
Access-Control-Allow-Origin --> *
Access-Control-Allow-Credentials --> true
Headers request : 
User-Agent --> python-requests/2.31.0
Accept-Encoding --> gzip, deflate
Accept --> application/json
Connection --> keep-alive
Content-Type --> application/json
Content-Length --> 13
Server:gunicorn/19.9.0
```
Análisis:
El código en `#10testing_api_rest_post_method.py` es un script de Python que utiliza la biblioteca `requests` para realizar una solicitud POST a la URL `http://httpbin.org/post`. Aquí está el análisis del código y los resultados obtenidos:

Análisis del Código:
- Se importan los módulos `requests` y `json`.
- Se define un diccionario `data_dictionary` con un solo par clave-valor.
- Se establecen los headers de la solicitud para indicar que se enviará y aceptará JSON.
- Se realiza una solicitud POST a `http://httpbin.org/post` con el diccionario de datos como cuerpo de la solicitud y los headers definidos.
- Se imprime el código de estado HTTP de la respuesta.
- Se imprimen los headers de la respuesta.
- Si el código de estado es 200, se procesa la respuesta:
  - Se convierte la respuesta en JSON y se imprimen sus elementos.
  - Se imprimen los headers de la respuesta y de la solicitud.
  - Se imprime el servidor de la respuesta.
- Si el código de estado no es 200, se imprime un mensaje de error.

Resultados Obtenidos:
- El código de estado HTTP es 200, lo que indica una respuesta exitosa.
- Los headers de la respuesta muestran información como la fecha, el tipo de contenido, la longitud del contenido, la conexión y el servidor.
- La respuesta JSON contiene:
  - `args`: Vacío, ya que no se enviaron argumentos en la URL.
  - `data`: La cadena 'id=0123456789', que parece ser una interpretación incorrecta del cuerpo JSON enviado.
  - `files`: Vacío, ya que no se enviaron archivos.
  - `form`: Vacío, ya que los datos se enviaron como JSON, no como datos de formulario.
  - `headers`: Los headers de la solicitud, que incluyen el tipo de contenido, la longitud del contenido y el agente de usuario.
  - `json`: `None`, lo cual es inesperado ya que se envió un JSON. Esto podría indicar un problema con cómo se envían los datos en la solicitud.
  - `origin`: La dirección IP desde la que se hizo la solicitud.
  - `url`: La URL a la que se hizo la solicitud.

Observaciones:
- Parece haber un problema con la forma en que se envían los datos JSON en la solicitud. Normalmente, se debe usar el argumento `json` o `data`, pero no ambos.
- El script intenta imprimir el servidor utilizando `response.headers['server']`, lo cual es redundante ya que ya se imprimieron todos los headers de la respuesta en pasos anteriores.
- El script podría beneficiarse de un manejo de errores más robusto para manejar diferentes códigos de estado y posibles excepciones durante la solicitud.

En resumen, el script realiza correctamente una solicitud POST y procesa la respuesta, pero hay un problema con la forma en que se envía el cuerpo JSON y algunos aspectos del código podrían mejorarse para la claridad y la robustez.


## 12.Análisis,Ejecución y Resultados del código: httpx_basic.py 
Código
```
#11httpx_basic.py 
import httpx

client = httpx.Client(timeout=10.0)
response = client.get("http://www.google.es")
print(response)
print(response.status_code)
print(response.text)
```
Resultado:
```
<Response [200 OK]>
200
[...]
```
Análisis:
El resultado del script es el siguiente:

Response [200 OK]: Indica que la solicitud fue exitosa y que el servidor respondió con el código de estado HTTP 200.
200: Es el código de estado HTTP que confirma que la solicitud fue exitosa.
El texto de la respuesta es el HTML de la página principal de Google, que incluye metadatos y scripts.
El HTML devuelto es el contenido estándar de la página de inicio de Google, con etiquetas <meta> que describen la página y <script> que contiene JavaScript para la funcionalidad de la página.

Es importante destacar que el script utiliza httpx, una biblioteca de terceros para solicitudes HTTP en Python, que es conocida por su API sencilla y su soporte para HTTP/2. Además, el script establece un tiempo de espera para la solicitud, lo cual es una buena práctica para evitar que el cliente espere indefinidamente por una respuesta.

En resumen, el script es un ejemplo simple de cómo realizar solicitudes HTTP en Python y cómo manejar la respuesta del servidor.

## 13.Análisis,Ejecución y Resultados del código : digo httpx_asyncio.py
Código
```
#12httpx_asyncio.py
import httpx
import asyncio # Se define una función asincrónica para realizar una solicitud HTTP.
# Se crea un cliente asincrónico que se cierra automáticamente al final del bloque 'with'.
async def request_http1():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://www.google.es")# Se espera la respuesta del cliente asincrónico. # Se imprimen el objeto de respuesta, el texto de la respuesta y la versión HTTP.

        print(response)
        print(response.text)
        print(response.http_version)
		
asyncio.run(request_http1())# Se ejecuta la función asincrónica utilizando asyncio.run().
```
Resultado:
```
-------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-57-0a1ec7e086be> in <cell line: 12>()
     10         print(response.http_version)
     11 
---> 12 asyncio.run(request_http2())

NameError: name 'request'

```
Análisis:


Resultado Esperado:

Se espera que el script imprima el objeto de respuesta, que incluiría el código de estado HTTP (por ejemplo, <Response [200 OK]>).
Luego, se imprimiría el contenido HTML de la página principal de Google España.
Finalmente, se imprimiría la versión HTTP utilizada en la respuesta (por ejemplo, HTTP/1.1 o HTTP/2).

Error Producido:

El error NameError indica que se intentó llamar a una función request_http2() que no está definida en el script.
El nombre correcto de la función es request_http1(), por lo que el error se debe a un error tipográfico o a una confusión en el nombre de la función.
Corrección:

Para corregir el error, asegurar , primero de que la llamada a asyncio.run() utilice el nombre correcto de la función, que es request_http1().
```
import httpx
import asyncio

async def request_http1():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://www.google.es")
        print(response)
        print(response.text)
        print(response.http_version)
		
asyncio.run(request_http1())  # Asegúrate de que el nombre de la función sea correcto.

```

## 14.Análisis,Ejecución y Resultados del crear un código : archivo httpx_asyncio_http2.py


Código:
```
!pip3 install httpx[http2]

import httpx
import asyncio

async def request_http2():
    # Se habilita HTTP/2 pasando http2=True al cliente asincrónico.
    async with httpx.AsyncClient(http2=True) as client:
        response = await client.get("http://www.google.es")
        print(response)
        print(response.text)
        print(response.http_version)

# Ejecuta la función asincrónica.
asyncio.run(request_http2())
```


Resultado:
```
Requirement already satisfied: httpx[http2] in /usr/local/lib/python3.10/dist-packages (0.27.0)
Requirement already satisfied: anyio in /usr/local/lib/python3.10/dist-packages (from httpx[http2]) (3.7.1)
Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from httpx[http2]) (2024.2.2)
Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.10/dist-packages (from httpx[http2]) (1.0.5)
Requirement already satisfied: idna in /usr/local/lib/python3.10/dist-packages (from httpx[http2]) (3.7)
Requirement already satisfied: sniffio in /usr/local/lib/python3.10/dist-packages (from httpx[http2]) (1.3.1)
Collecting h2<5,>=3 (from httpx[http2])
RuntimeError: asyncio.run() cannot be called from a running event loop

```
Análisis:

El código proporcionado es un script de Python que utiliza la biblioteca httpx para realizar solicitudes HTTP asincrónicas, específicamente habilitando el soporte para HTTP/2. El resultado muestra varios puntos importantes:

Instalación de Dependencias:
La salida del comando !pip3 install httpx[http2] indica que httpx y sus dependencias relacionadas con HTTP/2 ya están instaladas en el entorno de ejecución.
Código Asincrónico:
El script define una función asincrónica request_http2() que realiza una solicitud GET a http://www.google.es utilizando un cliente asincrónico con HTTP/2 habilitado.
La función imprime el objeto de respuesta, el contenido de la respuesta y la versión HTTP de la respuesta.
Ejecución de la Función Asincrónica:
Se utiliza asyncio.run(request_http2()) para ejecutar la función asincrónica desde fuera de cualquier otro evento asincrónico en ejecución.
Error de Ejecución:
El error RuntimeError: asyncio.run() cannot be called from a running event loop sugiere que el script se está ejecutando en un entorno donde ya hay un bucle de eventos en ejecución.
Esto puede ocurrir si se ejecuta el script en un entorno interactivo como Jupyter Notebook o IPython, donde asyncio.run() no es compatible porque estos entornos ya operan dentro de un bucle de eventos.
Análisis:

Para corregir el error, se debe modificar la forma en que se inicia la función asincrónica. Si se está ejecutando en un entorno interactivo, se puede utilizar await directamente si el entorno lo permite, o se puede acceder al bucle de eventos existente y ejecutar la función asincrónica con métodos como loop.run_until_complete().

## 15.Análisis,Ejecución y Resultados del código : archivo httpx_http2_trio.py. 

Código:
```
#14 archivo httpx_http2_trio.py. 
import httpx
import trio

results={}

async def fetch_result(client,url,results):
    print(url)
    results[url] = await client.get(url)
	
async def main_parallel_requests():
	async with httpx.AsyncClient(http2=True) as client:
		async with trio.open_nursery() as nursey:
			for i in range(2000,2020):
				url = f"https://en.wikipedia.org/wiki/{i}"
				nursey.start_soon(fetch_result,client,url,results)
		
trio.run(main_parallel_requests)
print(results)

```
Resultado:
```
https://en.wikipedia.org/wiki/2019
https://en.wikipedia.org/wiki/2018
https://en.wikipedia.org/wiki/2017
https://en.wikipedia.org/wiki/2016
https://en.wikipedia.org/wiki/2015 [...]
```
Análisis:

Este código es un script en Python que utiliza las bibliotecas httpx y trio para realizar solicitudes HTTP de manera asíncrona. Vamos a analizarlo:

Importación de módulos: El código comienza importando los módulos necesarios: httpx y trio.
Definición de funciones:
fetch_result(client, url, results): Esta función asincrónica recibe un cliente HTTP (client), una URL (url) y un diccionario de resultados (results). Realiza una solicitud GET a la URL proporcionada utilizando el cliente y almacena la respuesta en el diccionario de resultados.
main_parallel_requests(): Esta función asincrónica es la función principal. Crea un cliente HTTP asincrónico con soporte para HTTP/2 (http2=True). Luego, utiliza un contexto trio.open_nursery() para ejecutar en paralelo una serie de solicitudes GET a URLs de Wikipedia correspondientes a los años entre 2000 y 2019. Cada solicitud se maneja en una tarea separada utilizando nursey.start_soon().
Al final, se ejecuta trio.run(main_parallel_requests) para iniciar la ejecución de las solicitudes.
Resultados:
El resultado muestra una lista de URLs de Wikipedia correspondientes a los años desde 2000 hasta 2019. Estas URLs representan las páginas de Wikipedia para esos años.
En resumen, el código realiza solicitudes HTTP asincrónicas a las páginas de Wikipedia para los años mencionados y almacena las respuestas en un diccionario de resultados. El resultado impreso muestra las URLs de Wikipedia para los años 2000 a 201912. Es una forma interesante de explorar datos históricos en Wikipedia. 

## 16.Análisis,Ejecución y Resultados del código :archivo basic_authentication.py
Código:
```
#15archivo basic_authentication.py
#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

username=input("Ingresa el nombre de usuario:")
password = getpass()

response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth(username,password))
print('Response.status_code:'+ str(response.status_code))

if response.status_code == 200:
    print('Login exitoso :'+response.text)
```
Resultado:
````
Ingresa el nombre de usuario:S1
··········
Response.status_code:401

````
Análisis:

Se imporan los módulos: requests, HTTTPBasicAuth, y getpass.
Solicitud de credenciales: Pide al usuario así como un registro de su user y una contraseña.
Luego se realiza una solicitud GET a ‘https://api.github.com/user’, que es la URL de la API de GitHub para obtener información del usuario autenticado.

Se utiliza HTTPBasicAuth para pasar las credenciales ingresadas.

Luego, se imprime el código de estado  de respuesta HTTP.

Para terminar con el código de  200, que significa que la autenticación fue exitosa y se imprime la respuesta de la API.
 Para lo cual, la respuesta es 401, lo que indica que la autenticación ha fallado. Esto puede deberse a varias razones, como:

El nombre de usuario o la contraseña son incorrectos.
La cuenta de GitHub puede tener la autenticación en dos pasos activada, y el script no está manejando este caso.
La API de GitHub puede requerir tokens de acceso personal en lugar de nombres de usuario y contraseñas para la autenticación.


## 17.Análisis,Ejecución y Resultados del código : archivo digest_authentication.py
Código:
```
#16archivo digest_authentication.py
#!/usr/bin/env python3

import requests
from requests.auth import HTTPDigestAuth
from getpass import getpass

user=input("Ingresa el usuario:")
password = getpass()

url = 'http://httpbin.org/digest-auth/auth/user/pass'
response = requests.get(url, auth=HTTPDigestAuth(user, password))

print("Headers request : ")
for header, value in response.request.headers.items():
  print(header, '-->', value)

print('Response.status_code:'+ str(response.status_code))
if response.status_code == 200:
    print('Login successful :'+str(response.json()))

    print("Headers response: ")
    for header, value in response.headers.items():
        print(header, '-->', value)
```

Resultado:
````
Ingresa el usuario:S1
··········
Headers request : 
User-Agent --> python-requests/2.31.0
Accept-Encoding --> gzip, deflate
Accept --> */*
Connection --> keep-alive
Cookie --> stale_after=never; fake=fake_value
Authorization --> Digest username="S1", realm="me@kennethreitz.com", nonce="ecccf54c23801769cf91c30dd4f4cdd3", uri="/digest-auth/auth/user/pass", response="96d2cad7e995ddabf56290fb9bf9bde1", opaque="e638f9b9a314262c7dfb48bd0aa122bc", algorithm="MD5", qop="auth", nc=00000001, cnonce="5f4af38aed379192"
Response.status_code:401
````
Análisis:

Este código es un ejemplo de cómo realizar una solicitud HTTP utilizando autenticación de resumen de mensajes (digest authentication) en Python. Veamos el análisis paso a paso:

Importación de módulos:
Se importan los módulos necesarios: requests para realizar la solicitud HTTP, HTTPDigestAuth para la autenticación de resumen de mensajes y getpass para obtener la contraseña de forma segura.

Solicitud de credenciales al usuario:
El usuario ingresa su nombre de usuario y contraseña mediante la función input() y getpass.getpass() respectivamente.

Definición de la URL:
La variable url contiene la dirección a la que se enviará la solicitud. En este caso, es ‘http://httpbin.org/digest-auth/auth/user/pass’.

Realización de la solicitud GET con autenticación digest:

Se utiliza requests.get(url, auth=HTTPDigestAuth(user, password)) para realizar la solicitud HTTP.

La autenticación digest se configura con el nombre de usuario (user) y la contraseña (password).

Impresión de los encabezados de la solicitud:
Se imprimen los encabezados de la solicitud utilizando response.request.headers.

Verificación del estado de la respuesta:
Si el estado de la respuesta es 200 (éxito), se imprime “Inicio de sesión exitoso” y se muestra el contenido JSON de la respuesta.

También se imprimen los encabezados de la respuesta utilizando response.headers.

En resumen, este código realiza una solicitud HTTP con autenticación digest y muestra los encabezados de la solicitud y la respuesta. La respuesta actual tiene un estado de 401 (no autorizado), lo que significa que la autenticación falló. Puede deberse a un nombre de usuario o contraseña incorrectos o a un problema con el servidor.





# Preguntas:
## 1. ¿Cómo podemos realizar una solicitud POST con el módulo requests pasando una estructura dedatos de tipo diccionario que se enviaría al cuerpo de la solicitud?

Es aplicable en estos casos, utilizar json como parámetro del  método requests.post(). En camino a ello, veamos un modelo:
```
import requests

url = 'https://api.example.com/data'
data= {'name': 'Isadora', 'age': 16}

answer = requests.post(url, json=data)
```
En la actividad anterior, el diccionario data se enviará automáticamente como el cuerpo de la solicitud POST en formato JSON.



## 2.  ¿Cuál es la forma correcta de realizar una solicitud POST a través de un servidor proxy y modificar 
la información de los encabezados al mismo tiempo?


```
import requests

url = 'https://api.example.com/datos'
datos = {'nombre': 'Juan', 'edad': 30}
headers = {'User-Agent': 'Mozilla/5.0'}
proxy = {'http': 'http://proxy.example.com:8080'}

respuesta = requests.post(url, json=datos, headers=headers, proxies=proxy)
```
En este ejemplo, se utiliza un servidor proxy especificado en el diccionario proxy, y se modifica el encabezado User-Agent a través del diccionario headers.

## 3.  ¿Cómo podemos obtener el código de una solicitud HTTP devuelta por el servidor si, en el objeto 
de respuesta, tenemos la respuesta del servidor?

```
import requests

url = 'https://api.example.com/data'
naswer = requests.get(url)

status_code = naswer.status_code
print(status_code)
```
En este ejemplo, codigo_estado contendrá el código de estado HTTP devuelto por el servidor.
 
## 4. ¿Qué mecanismo se utiliza para mejorar el proceso de autenticación básico mediante el uso de un 
algoritmo criptográfico hash unidireccional? 


El mecanismo utilizado para mejorar el proceso de autenticación básico conocido como el "Digest Authentication" es útil mediante el uso de un algoritmo criptográfico hash unidireccional no solo porque  envía las credenciales (nombre de usuario y contraseña) en texto plano, sino que además se envía un hash de las credenciales junto con algunos datos adicionales. El servidor puede entonces hallar el mismo hash y compararlo con el hash recepcionado para autenticar al cliente.

## 5. ¿Qué encabezado se utiliza para identificar el navegador y el sistema operativo que usamos para 
enviar solicitudes a una URL?. 

El encabezado HTTP User-Agent guarda información sobre el software cliente (navegador web, aplicación, etc.) y el sistema operativo en el que se ejecuta. Por ejemplo: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3

