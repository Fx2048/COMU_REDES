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
## 1. Análisis,Ejecución y Resultados del código 
: request_http_client.py 

## 2.Análisis,Ejecución y Resultados del código 
: json_response.py
## 3.Análisis,Ejecución y Resultados del código 
: get_headers_response_request.py
## 4.Análisis,Ejecución y Resultados del código 
: get_emails_url_request.py 
## 5.Análisis,Ejecución y Resultados del código 
:  download_file.py 
## 6.Análisis,Ejecución y Resultados del código 
: count_words_file.py
## 7.Análisis,Ejecución y Resultados del código 
:  request_headers.py

## 8.Análisis,Ejecución y Resultados del código 
: archivo get_images_links_url.py 

## 9.Ejecución y Resultados del código 
: archivo testing_api_rest_get_method.py 
## 10.Análisis,Ejecución y Resultados del código 
: testing_api_rest_post_method.py. 
## 11.Análisis,Ejecución y Resultados del código 
: httpx_basic.py 
## 12.Análisis,Ejecución y Resultados del código 
: digo httpx_asyncio.py
## 13.Análisis,Ejecución y Resultados del código 
: archivo httpx_asyncio_http2.py
## 14.Análisis,Ejecución y Resultados del código 
: archivo httpx_http2_trio.py. 

## 15.Análisis,Ejecución y Resultados del código 
: archivo basic_authentication.py

## 16.Análisis,Ejecución y Resultados del código 
: archivo digest_authentication.py

# Preguntas:
1. ¿Cómo podemos realizar una solicitud POST con el módulo requests pasando una estructura dedatos de tipo diccionario que se enviaría al cuerpo de la solicitud?
   
3. ¿Cuál es la forma correcta de realizar una solicitud POST a través de un servidor proxy y modificarla información de los encabezados al mismo tiempo?
4. ¿Cómo podemos obtener el código de una solicitud HTTP devuelta por el servidor si, en el objetode respuesta, tenemos la respuesta del servidor?
5. ¿Qué mecanismo se utiliza para mejorar el proceso de autenticación básico mediante el uso de unalgoritmo criptográfico hash unidireccional?5. ¿Qué encabezado se utiliza para identificar el navegador y el sistema operativo que usamos paraenviar solicitudes a una URL?
