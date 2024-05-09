# Problema 23: Simulación de load balancing con DNS
Conceptos involucrados: Geolocation-based load-balancing policy, Latency-based load-balancing policy, Round-robin load-balancing policy, Weighted round-robin load-balancing policy.

Crea una función que simule cómo un sistema DNS podría dirigir tráfico a diferentes servidores utilizando diversas políticas de balanceo de carga.

Define una función select_server que acepte una lista de servidores y una política de balanceo de carga.

Implementa diferentes estrategias de balanceo de carga como funciones que seleccionen un servidor basado en la política especificada.


````
import random

# Lista de servidores de ejemplo
servers = ['Server1', 'Server2', 'Server3', 'Server4']

# Estado para mantener el índice para round-robin
current_index = 0

def select_server(servers, policy):
    """
    Selecciona un servidor de una lista basado en la política de balanceo de carga especificada.
    """
    if policy == 'round-robin':
        return round_robin(servers)
    elif policy == 'weighted-round-robin':
        return weighted_round_robin(servers)
    elif policy == 'latency-based':
        return latency_based(servers)
    elif policy == 'geolocation-based':
        return geolocation_based(servers)
    else:
        raise ValueError("Política de balanceo de carga no reconocida.")

def round_robin(servers):
    global current_index
    server = servers[current_index]
    current_index = (current_index + 1) % len(servers)
    return server

def weighted_round_robin(servers):
    # Suponiendo que los servidores tienen pesos asignados
    weights = [5, 1, 1, 3]  # Los pesos deben ser proporcionales a la capacidad del servidor
    server = random.choices(servers, weights)[0]
    return server

def latency_based(servers):
    # Simulación: elegir el servidor con 'menor latencia'
    # En un escenario real, se mediría la latencia a cada servidor
    latencies = {
        'Server1': 50,
        'Server2': 20,
        'Server3': 60,
        'Server4': 10
    }
    server = min(servers, key=lambda x: latencies[x])
    return server

def geolocation_based(servers):
    # Simulación: elegir el servidor más cercano geográficamente al usuario
    # En un escenario real, se utilizaría la ubicación del usuario
    user_location = 'Lima, Perú'
    locations = {
        'Server1': 'São Paulo, Brasil',
        'Server2': 'Bogotá, Colombia',
        'Server3': 'Ciudad de México, México',
        'Server4': 'Buenos Aires, Argentina'
    }
    # Simulación de distancia geográfica
    distances = {
        'Server1': 3000,
        'Server2': 1800,
        'Server3': 4200,
        'Server4': 3200
    }
    server = min(servers, key=lambda x: distances[x])
    return server

# Ejemplo de uso
policy = 'round-robin'  # Cambiar por la política deseada
selected_server = select_server(servers, policy)
print(f"El servidor seleccionado usando la política {policy} es: {selected_server}")

````
# Problema 24: Simulación de un registrador de dominios

Conceptos involucrados: Domain name registrar, Domain parking, Whois, Zone file.

Escribe una función que simule un registrador de dominios capaz de registrar, estacionar y proporcionar información WHOIS de dominios.

Implementa una función register_domain que permita registrar un nuevo dominio y guardarlo en un "archivo de zona".


Crea una función park_domain que marque un dominio como estacionado.
Desarrolla una función query_whois que proporcione información WHOIS del dominio.

````
# Simulación de un registrador de dominios

# Base de datos simulada para los dominios
domain_database = {}

def register_domain(domain_name, owner_details):
    """
    Registra un nuevo dominio y lo guarda en la base de datos.
    """
    if domain_name in domain_database:
        return f"Error: El dominio {domain_name} ya está registrado."
    else:
        domain_database[domain_name] = {
            'owner': owner_details,
            'zone_file': None,
            'parked': False
        }
        return f"El dominio {domain_name} ha sido registrado exitosamente."

def park_domain(domain_name):
    """
    Marca un dominio como estacionado.
    """
    if domain_name in domain_database:
        domain_database[domain_name]['parked'] = True
        return f"El dominio {domain_name} ha sido estacionado."
    else:
        return f"Error: El dominio {domain_name} no está registrado."

def query_whois(domain_name):
    """
    Proporciona información WHOIS del dominio.
    """
    if domain_name in domain_database:
        owner_info = domain_database[domain_name]['owner']
        return f"Información WHOIS para {domain_name}: {owner_info}"
    else:
        return f"Error: No hay información WHOIS disponible para {domain_name}."

# Ejemplo de uso
print(register_domain('example.com', 'John Doe'))
print(park_domain('example.com'))
print(query_whois('example.com'))

````

