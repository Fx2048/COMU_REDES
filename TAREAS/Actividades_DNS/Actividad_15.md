# ACTIVIDAD 15 : DNS

# Problema 1: Diseño de un sistema de distribución de contenidos (CDN)

## Código:
````
from flask import Flask, request
from functools import lru_cache

app = Flask(__name__)

# Diccionario para almacenar el contenido distribuido en el CDN
content_cache = {}

# Simulación de contenido en el servidor de origen
origin_content = {
    '/index.html': '<html><body><h1>Bienvenido a mi sitio web!</h1></body></html>',
    '/about.html': '<html><body><h1>Acerca de nosotros</h1><p>Somos una empresa dedicada a...</p></body></html>',
    # Agrega más contenido simulado según sea necesario
}

# Simulación de la ubicación geográfica de los usuarios
user_locations = {
    'user1': 'USA',
    'user2': 'EUROPE',
    'user3': 'ASIA',
    # Agrega más ubicaciones de usuarios según sea necesario
}

# Simulación de latencias entre los usuarios y los servidores de borde
latency_map = {
    ('USA', 'EdgeServer1'): 20,
    ('EUROPE', 'EdgeServer1'): 100,
    ('ASIA', 'EdgeServer1'): 200,
    # Agrega más asignaciones de latencia según sea necesario
}

# Función para obtener la latencia entre un usuario y un servidor de borde
def get_latency(user_location, edge_server):
    return latency_map.get((user_location, edge_server), float('inf'))

# Función para encontrar el servidor de borde más cercano a un usuario
def find_closest_edge_server(user_location):
    return min(latency_map, key=lambda x: get_latency(user_location, x[1]))[1]

# Simulación de la función fetch_from_origin para obtener contenido del servidor de origen
def fetch_from_origin(path):
    return origin_content.get(path, None)

# Ruta para manejar las solicitudes GET
@app.route('/``', methods=['GET'])
def get_content(path):
    # Verificar si el contenido está en caché
    if path in content_cache:
        return content_cache[path]
    else:
        # Obtener el contenido del servidor de origen
        origin_content = fetch_from_origin(path)
        # Almacenar el contenido en caché
        content_cache[path] = origin_content
        return origin_content
````
# Resultado
````
C:\Users\PROPIETARIO\PycharmProjects\pythonProject\venv\Scripts\python.exe C:\Users\PROPIETARIO\PycharmProjects\pythonProject\main.py 

Process finished with exit code 0
````

# Codificación Análisis
````
Simulación de datos:
Se agregaron diccionarios para simular el contenido en el servidor de origen, la ubicación geográfica de los usuarios y las latencias entre los usuarios y los servidores de borde.
Función para obtener la latencia:
Se agregó una función get_latency para obtener la latencia entre un usuario y un servidor de borde.
Función para encontrar el servidor de borde más cercano:
Se agregó una función find_closest_edge_server para encontrar el servidor de borde más cercano a un usuario basado en la latencia.
Implementación de la función fetch_from_origin:
Se agregó una simulación de la función fetch_from_origin para obtener contenido del servidor de origen.
Actualización de la ruta para manejar solicitudes GET:
La ruta ahora incluye el patrón /<path:path> para manejar cualquier ruta de contenido solicitada.
Se implementó la función get_content para manejar las solicitudes GET. Verifica si el contenido está en caché y, si no lo está, lo obtiene del servidor de origen y lo almacena en caché antes de devolverlo.
````
# Resultado análisis:
````
C:\Users\PROPIETARIO\PycharmProjects\pythonProject\venv\Scripts\python.exe: Esta es la ruta al intérprete de Python que se utilizó para ejecutar tu script. En este caso, estás utilizando un intérprete de Python que está dentro de un entorno virtual (venv), que es una práctica común para aislar las dependencias de tu proyecto.
C:\Users\PROPIETARIO\PycharmProjects\pythonProject\main.py: Esta es la ruta al script de Python que se ejecutó.
Process finished with exit code 0: Esta es una notificación del sistema que indica que tu script ha terminado de ejecutarse. Un código de salida de 0 generalmente significa que el programa se ejecutó con éxito sin errores.

````
#  Problema 2: Implementación de un servidor autoritario de DNS
## Código:
````
import dns.message
import dns.rdatatype
import dns.rdataclass
import dns.flags
import dns.query
import socket

# Diccionario para almacenar los registros de recursos (RR)
resource_records = {
    # Aquí deberías agregar tus registros de recursos
    # Por ejemplo: 'example.com': {'A': '192.0.2.1'}
}

def process_dns_query(query_message):
    # Lógica para procesar la consulta DNS y generar una respuesta
    # Aquí deberías buscar en tu base de datos de registros de recursos y construir la respuesta DNS apropiada
    response_message = dns.message.make_response(query_message)
    for question in query_message.question:
        records = resource_records.get(question.name.to_text(), {})
        record_type = dns.rdatatype.to_text(question.rdtype)
        record_data = records.get(record_type)
        if record_data:
            rrset = dns.rrset.from_text(question.name, 3600, dns.rdataclass.IN, question.rdtype, record_data)
            response_message.answer.append(rrset)
    return response_message

def main():
    server_address = '127.0.0.1'
    server_port = 53
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((server_address, server_port))

    while True:
        # Recibir y procesar solicitudes DNS entrantes
        query_data, client_address = server_socket.recvfrom(512)
        query_message = dns.message.from_wire(query_data)
        response_message = process_dns_query(query_message)
        # Enviar respuesta al cliente DNS
        server_socket.sendto(response_message.to_wire(), client_address)

if __name__ == "__main__":
    main()

````
# Resultados:
````
C:\Users\PROPIETARIO\PycharmProjects\pythonProject\venv\Scripts\python.exe C:\Users\PROPIETARIO\PycharmProjects\pythonProject\main.py 
Traceback (most recent call last):
  File "C:\Users\PROPIETARIO\PycharmProjects\pythonProject\main.py", line 101, in <module>
    main()
  File "C:\Users\PROPIETARIO\PycharmProjects\pythonProject\main.py", line 89, in main
    server_socket.bind((server_address, server_port))
PermissionError: [WinError 10013] Intento de acceso a un socket no permitido por sus permisos de acceso

Process finished with exit code 1

````

# Análisis de código :
````
Este código crea un servidor DNS básico que escucha en el puerto 53 UDP y responde a las consultas DNS entrantes. Las respuestas se generan en función de los registros de recursos almacenados en el diccionario resource_records. Por favor, ten en cuenta que este es un ejemplo muy básico y no maneja muchos aspectos de un servidor DNS real, como la autenticación, el manejo de errores, la escalabilidad, entre otros. Te recomendaría investigar más sobre estos temas si estás interesado en implementar un servidor DNS real
````
# Análisis de resultado:
```
El error PermissionError: [WinError 10013] Intento de acceso a un socket no permitido por sus permisos de acceso indica que el programa no tiene permisos suficientes para enlazar el socket a la dirección y puerto especificados. Esto puede ocurrir debido a restricciones de permisos en el sistema operativo o porque el puerto está siendo utilizado por otro proceso.

Para corregir este problema, hay varias opciones que puedes intentar:

Ejecutar el programa como administrador: Intenta ejecutar el programa con permisos de administrador. Los permisos de administrador pueden otorgar los privilegios necesarios para enlazar el socket al puerto especificado.
Cambiar el puerto: Si el puerto 5353 está reservado o en uso por otro proceso, intenta cambiar el puerto a uno diferente que esté disponible. Puedes cambiar server_port = 5353 a un puerto diferente, como server_port = 5354.
Cerrar el programa que utiliza el puerto: Si sabes qué programa está utilizando el puerto 5353, puedes cerrarlo temporalmente para liberar el puerto y permitir que tu programa se ejecute.
Verificar el firewall: Asegúrate de que tu firewall no esté bloqueando el acceso al puerto especificado. Puedes intentar desactivar temporalmente el firewall para ver si eso resuelve el problema.
```
#  Problema 3: Diseño de un sistema de gestión de dominios (DNS)
## Código:
````
 from flask import Flask, request, jsonify
 app = Flask(__name__)
 # Base de datos ficticia para almacenar los dominios y registros de recursos
 domain_database = {}
 @app.route('/register', methods=['POST'])
 def register_domain():
 domain_name = request.json.get('domain_name')
 ip_address = request.json.get('ip_address')
 # Verificar si el dominio ya está registrado
 if domain_name in domain_database:
 return jsonify({'message': 'Domain already registered'}), 400
 # Registrar el nuevo dominio
 domain_database[domain_name] = ip_address
 return jsonify({'message': 'Domain registered successfully'}), 200
 @app.route('/resolve/<domain_name>', methods=['GET'])
 def resolve_domain(domain_name):
 # Verificar si el dominio está registrado
 if domain_name not in domain_database:
 return jsonify({'message': 'Domain not found'}), 404
 # Obtener la dirección IP asociada con el dominio
 ip_address = domain_database[domain_name]
 return jsonify({'domain': domain_name, 'ip_address': ip_address}), 200
 if __name__ == '__main__':
 app.run(debug=True)
````
# Análisis de código:

1.Importaciones de bibliotecas:
Se importan las clases necesarias de la biblioteca Flask para crear la aplicación web, manejar las solicitudes HTTP y generar respuestas JSON.
2. Creación de la aplicación Flask:

Se crea una instancia de la clase Flask para crear la aplicación web.

3. Base de datos ficticia:
Se define una estructura de datos, en este caso un diccionario, para simular una base de datos donde se almacenarán los nombres de dominio y sus direcciones IP asociadas.
4. Ruta para registrar dominios:
 Se define una ruta /register que acepta solicitudes POST para registrar nuevos dominios.
La función register_domain() extrae el nombre de dominio y la dirección IP de la solicitud JSON.
Verifica si el dominio ya está registrado en la base de datos.
Si el dominio no está registrado, lo agrega a la base de datos y devuelve un mensaje de éxito
5. Ruta para resolver dominios:
Se define una ruta /resolve/<domain_name> que acepta solicitudes GET para resolver nombres de dominio.
La función resolve_domain() toma el nombre de dominio como parámetro de la URL.
Verifica si el dominio está registrado en la base de datos.
Si el dominio está registrado, devuelve el nombre de dominio y su dirección IP asociada.
6. Inicio de la aplicación:
Se asegura de que el servidor Flask se ejecute solo si el script se ejecuta directamente (no cuando se importa como un módulo).
Ejecuta la aplicación Flask en modo de depuración para facilitar la detección y corrección de errores durante el desarrollo.

# Resultado
# Análisis de resultado:
#  Problema 4: Optimización de la resolución de nombres de dominio (DNS)

````
# (utilizando dnspython)
 import dns.resolver
 def dns_lookup(domain_name):
 try:
 # Realizar una consulta DNS para el nombre de dominio dado
 result = dns.resolver.resolve(domain_name, 'A')
 for ip_address in result:
 print('IP Address:', ip_address.to_text())
 except dns.resolver.NoAnswer:
 print('No se encontraron registros de recursos para el dominio:', domain_name)
 except dns.resolver.NXDOMAIN:
 print('El dominio no existe:', domain_name)
 except dns.exception.Timeout:
 print('La consulta DNS ha excedido el tiempo de espera:', domain_name)
 if __name__ == "__main__":
 domain_name = 'example.com'
 dns_lookup(domain_name)
````

#  Problema 5: Implementación de un sistema de registro de dominios

````
#Ejemplo de código en Python (con Flask)
 @app.route('/register', methods=['POST'])
 def register_domain():
 domain_name = request.json.get('domain_name')
 owner_info = request.json.get('owner_info')
 # Verificar si el dominio ya está registrado
 if domain_name in domain_database:
 return jsonify({'message': 'Domain already registered'}), 400
 # Registrar el nuevo dominio
 domain_database[domain_name] = owner_info
 return jsonify({'message': 'Domain registered successfully'}), 200
 if __name__ == '__main__':
 app.run(debug=True)
 from flask import Flask, request, jsonify
 app = Flask(__name__)
 # Base de datos ficticia para almacenar los dominios registrados
 domain_database = {}
````
