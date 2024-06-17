# VPC route 53 and CloudFront
# Pregunta 6: 
Pregunta: Explica cómo Amazon CloudFront mejora la entrega de contenido. 
# Mediante: 
* Red Global de Servidores Edge
* Caché
* Optimización de rutas
* Seguridad
  
¿Qué es una
distribución de CloudFront y cuáles son sus componentes?
Es una configuración que define la entrega de contenido mediante CloudFrontNet.
## Componentes:

1. Origen
2. Cofiguración de Caché
3. Configuración de distribución
4. Clases de precios



• Ejercicio: Diseña una configuración de CloudFront para una aplicación web global.

Elección de clase de Precio:
        Clase de precio general.Beneficia latencia.
Configuración de políticas de caché
        TTL #Tiempo de vida
        Políticas de caché personalizado

Explica cómo manejarías las actualizaciones de contenido y la invalidación de caché

Manejo de actualizaciones de contenido (objects) e invalidación de caché
        Invalidación de caché
        Cloud front_invalidation (delete)
        Solicitudes_invalidation to CF(enroutment) from cache
        
        Versionado de objetos( S3)
        paramethers from URLs Version > content updates {without frequent_invalidations}


# 7. Introducción a Amazon API Gateway
• Pregunta: Describe las principales características de Amazon API Gateway. 
         * Escalabilidad
         * Gestión de tráfico
         * Seguridad
         * Monitoreo,alertas y registro
         * Transformación de solicitudes y respuestas
# ¿Cómo facilita la gestión de APIs RESTful?
      * Interoperabilidad
      * Escalabildiad
      * Flexibilidad y desacoplamiento
      * Acceso a funcionalidades de terceros
      * Seguridad
      *  Manejo de errores
      * Control de versiones y almacenamiento en caché
  
 # Configuración en Api Gateway
 * Crear una nueva API, en api gateway
 * Definir recursos y métodos (Post,GET,PUT,DELETE) bajo el nombre de ``Users``
 * Configurar integraciones de método con lamda functions
 * Configurar modelos y validaciones de entrada/salida según sea necesario.

• Ejercicio: Diseña una API simple utilizando Amazon API Gateway que gestione las operaciones CRUD (Crear, Leer, Actualizar, Borrar) para una base de datos de usuarios.

Explica cómo integrarías esta API con AWS Lambda para manejar las solicitudes.

````

import json
import sqlite3
from pathlib import Path
# definir database
class Database:
    _instance = None
# 
    @staticmethod
    def get_instance():
        if Database._instance is None:
            Database()
        return Database._instance
#Definir la cualidad de irrepetibilidad de instancias de DB
    def __init__(self):
        if Database._instance is not None:
            raise Exception("Esta clase es un singleton!")
        else:
            Database._instance = self
            self.db_file = Path("users.db")
            self._initialize_database()
# inicializandodatabase
    def _initialize_database(self):
        if not self.db_file.exists():
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE Users (
                    id TEXT PRIMARY KEY,
                    info TEXT
                )
            ''')
            conn.commit()
            conn.close()
# devuelve conexion con base datos de sqlite
    def get_connection(self):
        conn = sqlite3.connect(self.db_file)
        conn.row_factory = sqlite3.Row
        return conn
# métodos para interactuar con la DB:
class UserService:
    def __init__(self):
        self.db = Database.get_instance()

    def create_user(self, event):
        """Creates a new user in the database."""
        try:
            body = json.loads(event['body'])
            user_id = body.get('id')
            info = json.dumps(body.get('info', {}))

            if not user_id:
                raise ValueError("User ID is required")

            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Users (id, info) VALUES (?, ?)', (user_id, info))
            conn.commit()
            conn.close()

            return {
                'statusCode': 201,
                'body': json.dumps({'message': 'User created successfully'})
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'message': str(e)})
            }

    def get_user(self, event):
        """Recuperar un usuario del database por el ID"""
        try:
            user_id = event['pathParameters']['id']

            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Users WHERE id = ?', (user_id,))
            user = cursor.fetchone()
            conn.close()

            if user is None:
                return {
                    'statusCode': 404,
                    'body': json.dumps({'message': 'User not found'})
                }

            return {
                'statusCode': 200,
                'body': json.dumps(dict(user))
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'message': str(e)})
            }

    def update_user(self, event):
        """Actualiza la información de Users."""
        try:
            user_id = event['pathParameters']['id']
            body = json.loads(event['body'])
            info = json.dumps(body.get('info', {}))

            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute('UPDATE Users SET info = ? WHERE id = ?', (info, user_id))
            conn.commit()
            conn.close()

            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'User updated successfully'})
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'message': str(e)})
            }

    def delete_user(self, event):
        """Borrar desde el parametro id del usuario """
        try:
            user_id = event['pathParameters']['id']
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM Users WHERE id = ?', (user_id,))
            conn.commit()
            conn.close()

            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'User deleted successfully'})
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'message': str(e)})
            }

# Simulaciones de pruebas
def simulate_event(method, body=None, path_params=None):
    return {
        'body': json.dumps(body) if body else None,
        'pathParameters': path_params
    }

# Inicialización de servicios
user_service = UserService()

# Crear usuario
create_event = simulate_event(
    method='POST',
    body={'id': '1', 'info': {'name': 'Brigitte Bernal', 'email': 'Brigitte.bernal@upch.pe'}}
)
create_response = user_service.create_user(create_event)
print(f"Create User Response: {create_response}")

# Obtener usuario
get_event = simulate_event(
    method='GET',
    path_params={'id': '1'}
)
get_response = user_service.get_user(get_event)
print(f"Get User Response: {get_response}")

# Actualizar usuario
update_event = simulate_event(
    method='PUT',
    body={'info': {'name': 'Brigitte Bernal', 'email': 'Brigitte.bernal@upch.pe'}},
    path_params={'id': '1'}
)
update_response = user_service.update_user(update_event)
print(f"Update User Response: {update_response}")

# Obtener usuario después de actualizar
get_response_after_update = user_service.get_user(get_event)
print(f"Get User After Update Response: {get_response_after_update}")

# Eliminar usuario
delete_event = simulate_event(
    method='DELETE',
    path_params={'id': '1'}
)
delete_response = user_service.delete_user(delete_event)
print(f"Delete User Response: {delete_response}")

# Obtener usuario después de eliminar
get_response_after_delete = user_service.get_user(get_event)
print(f"Get User After Delete Response: {get_response_after_delete}")


````

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/bc09c5c7-6705-4462-a237-e5c650d359af)


# Código 6.py


````


###simular una red corporativa completa utilizando Python. La red debe incluir 

import networkx as nx
import matplotlib.pyplot as plt
from ipaddress import ip_network, ip_address

# Clase para representar la red
class Network:
    # lista de dispositivos en la red
    def __init__(self):
        self.devices = []
        self.connections = []
        self.G = nx.Graph()
# Agregar dispositivo al grafo
    def add_device(self, device):
        self.devices.append(device)
        self.G.add_node(device.name, type=device.device_type)
#lista de conexiones en la red
    def connect(self, device1, device2):
        self.connections.append((device1, device2))
        self.G.add_edge(device1.name, device2.name)
#grafo para representar la red
    def assign_ip_addresses(self, cidr):
        network = ip_network(cidr)
        hosts = network.hosts()
        for device in self.devices:
            if device.device_type in ['PC', 'Server']:
                device.ip_address = next(hosts)
                print(f"Assigned IP {device.ip_address} to {device.name}")
#visualizar la red networkx para crear un grafo y la biblioteca matplotlib, para dibujar tal grafo, con dispositivos 
    def visualize(self):
        pos = nx.spring_layout(self.G)
        labels = nx.get_node_attributes(self.G, 'type')
        nx.draw(self.G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=10)
        nx.draw_networkx_edge_labels(self.G, pos)
        plt.show()
# simular el tráfico de red enviando paquetes de datos desde un dispositivo de origen (src) a un dispositivo de destino)usando el camino más corto de dst
#src (origen) y dst(destino)
    def simulate_traffic(self, src,dst):                 
        try:
            path = nx.shortest_path(self.G, source=src.name, target=dst.name)
            print(f"Data packet path from {src.name} to {dst.name}: {' -> '.join(path)}")
        except nx.NetworkXNoPath:
            print(f"No path found between {src.name} and {dst.name}")
# Clase padre Device(cualquier dispositivo conectado puede ser identificado):
class Device:
    def __init__(self, name, device_type):
        self.name = name
        self.device_type = device_type
        self.ip_address = None
#class router 
class Router(Device):
    #crea un diccionario tabla de enrutamiento,donde las claves son las redes y los valores: las métricas de las rutas
    def __init__(self, name):
        super().__init__(name, 'Router')
        self.routing_table = {}
#agrega routers e identifica el sgte salto para encntrar la ruta de destino
    def add_route(self, network, next_hop):
        self.routing_table[network] = next_hop
# obtener ruta de una dirección IP
    def get_route(self, ip):
        for network, next_hop in self.routing_table.items():
            if ip in ip_network(network):
                return next_hop
        return None
#definición de Un switch
class Switch(Device):
    def __init__(self, name):
        super().__init__(name, 'Switch')
# Definamos una PC
class PC(Device):
    def __init__(self, name):
        super().__init__(name, 'PC')
# definamos un server:
class Server(Device):
    def __init__(self, name):
        super().__init__(name, 'Server')

# Create network
network = Network()

# Create devices
router1 = Router("Router1")
router2 = Router("Router2")
switch1 = Switch("Switch1")
switch2 = Switch("Switch2")
pc1 = PC("PC1")
pc2 = PC("PC2")
pc3 = PC("PC3")
pc4 = PC("PC4")

# Add devices to the network
network.add_device(router1)
network.add_device(router2)
network.add_device(switch1)
network.add_device(switch2)
network.add_device(pc1)
network.add_device(pc2)
network.add_device(pc3)
network.add_device(pc4)

# Connect devices
network.connect(router1, switch1)
network.connect(router1, switch2)
network.connect(switch1, pc1)
network.connect(switch1, pc2)
network.connect(switch2, pc3)
network.connect(switch2, pc4)
network.connect(router1, router2)

# Assign IP addresses
network.assign_ip_addresses('192.168.1.0/24')

# Add static routes
router1.add_route('192.168.1.0/24', 'Router1')
router1.add_route('192.168.2.0/24', 'Router2')
router2.add_route('192.168.1.0/24', 'Router1')
router2.add_route('192.168.2.0/24', 'Router2')

# Visualize the network
network.visualize()

# Simulate traffic
network.simulate_traffic(pc1, pc3)

````

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/59efa1c1-945a-493b-bc16-b3ca73feb836)
