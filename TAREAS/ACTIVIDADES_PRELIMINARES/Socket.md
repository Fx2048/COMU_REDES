# Programando sockets

# Introducción

Para esta actividad utiliza: pip3 install python-socketio, pip3 install aiohttp y el conjunto decódigos alojados en:

https://github.com/kapumota/Actividades-CC8280/tree/main/SocketsWebSockets es una tecnología que proporciona comunicación en tiempo real entre un cliente y unservidor a través de una conexión TCP, eliminando la necesidad de que los clientes verifiquencontinuamente si los puntos finales API tienen actualizaciones o contenido nuevo.
Los clientes creanuna única conexión a un servidor WebSocket y esperan escuchar nuevos eventos o mensajes delservidor.

La principal ventaja de WebSockets es que son más eficientes porque reducen la carga de la red yenvían información en forma de mensajes a una gran cantidad de clientes. Entre las principalescaracterísticas de WebSockets, podemos destacar las siguientes:

• Proporcionan comunicación bidireccional (dúplex completo) a través de una únicaconexión TCP.

• Proporcionan comunicación en tiempo real entre un servidor y sus clientes conectados.

Esto permite la aparición de nuevas aplicaciones orientadas a la gestión de eventos deforma asincrónica.• Proporcionan simultaneidad y mejoran el rendimiento, optimizando los tiempos derespuesta y dando como resultado aplicaciones web más confiables.

# Metodología:

Para implementar un servidor basado en socket.io, necesitamos introducir otros módulos comoasyncio y aiohttp:
asyncio es un módulo de Python que nos ayuda a realizar la programación concurrente deun solo hilo en Python. Está disponible en Python 3.7; la documentación se puedeencontrar en https://docs.python.org/3/library/asyncio.html.• aiohttp es una biblioteca para crear aplicaciones cliente y servidor integradas en asyncio.

El módulo utiliza las ventajas de WebSockets de forma nativa para comunicarse entrediferentes partes de la aplicación de forma asincrónica.

La documentación está disponibleen http://aiohttp.readthedocs.io/en/stable.


Revisa el código web_socket_server.py donde implementamos un servidor socket.io usando elframework aiohttp, el cual, en un nivel bajo, usa asyncio.

En el código anterior, implementamos un servidor basado en socket.io que usa el módulo aiohttp.Como puedes ver en el código, hemos definido dos métodos: el método index (), que devolverá unmensaje de respuesta basado en la solicitud del punto final raíz "/", y el método print message (),que imprime el identificador del socket y los datos emitidos por el evento. 

# Análisis de los códigos:

## 0. Revisa el código web_socket_server.py donde implementamos un servidor socket.io usando el 
framework aiohttp, el cual, en un nivel bajo, usa asyncio. 


## 1. Escribimos el siguiente código para el cliente en web_socket_client.py. 
Si revisamos el código anterior, estamos usando el método connect() del socketio. La clase Client () 
para conectarse al servidor que está escuchando en el puerto 8080. Definimos dos métodos, uno 
para conectar y otro para desconectar.

## 2. Los tipos y funciones necesarios para trabajar con sockets se pueden encontrar en Python en el 
módulo socket. El módulo de socket proporciona todas las funcionalidades necesarias para escribir 
rápidamente clientes y servidores TCP y UDP. 
Revisa los métodos de cliente y servidor,

## 3. Si queremos probar el servidor HTTP, podríamos crear otro script que nos permita obtener la 
respuesta enviada por el servidor que hemos creado. Puede encontrar el siguiente código en el 
archivo testing_http_server.py. 
¿Qué sucede?. 


## 4.Hacemos esto con el código reverse_shell.py.

## 5. Ejercicio: ejecuta la aplicación llamada netcat con el comando ncat -l -v -p 45679, indicando el puerto 
que declaramos en el script, para obtener un shell inverso en la dirección localhost usando el puerto 
45679. 

## 6. Utilizamos el siguiente código en el archivo check_ports_socket.py. 
Si ejecutamos el script anterior, podemos ver cómo comprueba cada puerto en localhost y devuelve 
una dirección IP o dominio específico, independientemente de si está abierto o cerrado. El primer 
parámetro puede ser una dirección IP o un nombre de dominio, porque el módulo de socket puede 
resolver una dirección IP de un dominio y un dominio de una dirección IP. 
Ejercicios: ¿Qué sucede si ejecutamos la función con una dirección IP o nombre de dominio que no 
existe? . 


## 7. Explica el funcionamiento de sock.settimeout().

## 8. Si revisas el código anterior, la instrucción s.connect ((host, puerto)) conecta al cliente con el 
servidor, y el método s.recv (1024) recibe los mensajes enviados por el servidor


## 9. Revisa el código udp_server.py.
En el código anterior, vemos que socket.SOCK_DGRAM crea un socket UDP, y la instrucción data, 
addr = s.recvfrom (buffer) devuelve los datos y la dirección de la fuente.

## 10. Revisa el código udp_client.py. 

En el código anterior, estamos creando una aplicación cliente basada en el protocolo UDP. 
Para enviar un mensaje a una dirección específica, usamos el método sendto () y para recibir un 
mensaje de la aplicación del servidor, usamos el método recvfrom ().  
Finalmente, es importante considerar que si intentamos usar SOCK_STREAM con el socket UDP, 
probablemente tenemos un error: socket.error. Por lo tanto, es importante recordar que 
tenemos que usar el mismo tipo de socket para el cliente y el servidor cuando estamos 
construyendo aplicaciones orientadas a pasar mensajes con sockets.
