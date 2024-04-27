# ACTIVIDAD 15 : DNS

# Problema 1: Diseño de un sistema de distribución de contenidos (CDN)

#Código:
````
from flask import Flask, request
app = Flask(__name__)
# Diccionario para almacenar el contenido distribuido en el CDN
content_cache = {}

@app.route('/<path:path>', methods=['GET'])
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

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/2a6f3ff2-a7d0-4347-b604-c54a0e234963)

# Codificación Análisis
````

Inicialización de Flask: app = Flask(__name__) crea una nueva aplicación Flask.
Creación de un diccionario para almacenar contenido: content_cache = {} es un diccionario que se utiliza para almacenar el contenido que se distribuye a través del CDN.
Definición de una ruta y una función de vista: @app.route('/<path:path>', methods=['GET']) define una ruta en la aplicación Flask. Cuando se realiza una solicitud GET a esta ruta, se llama a la función get_content(path).
Función de vista get_content(path): Esta función verifica si el contenido solicitado ya está en caché (if path in content_cache). Si es así, devuelve el contenido desde la caché. Si no, obtiene el contenido del servidor de origen (fetch_from_origin(path)), lo almacena en la caché y luego lo devuelve.
Función fetch_from_origin(path): Esta función simula la obtención de contenido del servidor de origen. En una implementación real de un CDN, aquí es donde se descargaría el contenido de la base de datos, sistema de archivos, o servidor remoto.
Ejecución de la aplicación Flask: if __name__ == '__main__': app.run(debug=True) inicia la aplicación Flask en modo de depuración cuando se ejecuta el script directamente.
````
# Resultado análisis:
````
Se describirá acontinuación el significado de lo que vimos en los resultados:

Serving Flask app '__main__': Esto indica que estás sirviendo tu aplicación Flask y '__main__' es el nombre del módulo donde se está ejecutando tu aplicación.
Debug mode: on: Esto significa que has activado el modo de depuración de Flask. En este modo, Flask te proporcionará información adicional sobre cualquier error que ocurra mientras se ejecuta tu aplicación.
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.: Esta es una advertencia que te indica que estás utilizando el servidor de desarrollo incorporado de Flask. Este servidor no está diseñado para su uso en un entorno de producción.
Running on http://127.0.0.1:5000: Esto te indica la dirección en la que se está ejecutando tu aplicación. En este caso, se está ejecutando en tu máquina local (127.0.0.1) en el puerto 5000.
Press CTRL+C to quit: Esta es una indicación de cómo puedes detener el servidor. Puedes hacerlo presionando las teclas CTRL+C en tu teclado.
Restarting with stat: Esto significa que el servidor se reiniciará automáticamente si detecta cambios en tus archivos de código fuente.
````
#  Problema 2: Implementación de un servidor autoritario de DNS

````
 import dns.message
 import dns.rdatatype
 import dns.rdataclass
 import dns.flags
 import dns.query
 def process_dns_query(query_message):
 # Lógica para procesar la consulta DNS y generar una respuesta
 # Aquí deberías buscar en tu base de datos de registros de recursos y construir la
 respuesta DNS apropiada
 return response_message
 def main():
 server_address = '127.0.0.1'
 server_port = 53
 while True:
 # Recibir y procesar solicitudes DNS entrantes
 query_data, _ = server_socket.recvfrom(1024)
 query_message = dns.message.from_wire(query_data)
 response_message = process_dns_query(query_message)
 # Enviar respuesta al cliente DNS
 server_socket.sendto(response_message.to_wire(), client_address)
 if __name__ == "__main__":
 main()
````
#  Problema 3: Diseño de un sistema de gestión de dominios (DNS)

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
