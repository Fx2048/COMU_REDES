import logging
import random

# Configuración del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Server:
    """Clase que representa un servidor web."""
    def __init__(self, name):
        self.name = name

    def handle_request(self, request):
        """Simula el manejo de una solicitud en el servidor."""
        if random.choice([True, False]):  # Simulación de fallo aleatorio
            raise Exception(f"Server {self.name} failed to handle the request.")
        logging.info(f"{self.name} handled request: {request}")
        return f"Request handled by {self.name}"

class LoadBalancer:
    """Clase que representa un balanceador de carga."""
    def __init__(self):
        self.servers = []

    def add_server(self, server):
        """Añade un servidor al balanceador de carga."""
        self.servers.append(server)
        logging.info(f'Server {server.name} added to load balancer.')

    def distribute_http_requests(self, requests):
        """Distribuye solicitudes HTTP entre los servidores disponibles."""
        for request in requests:
            for server in self.servers:
                try:
                    return server.handle_request(request)
                except Exception as e:
                    logging.warning(f"{server.name} could not handle request: {e}")
        raise Exception("All servers failed to handle the request.")

class Region:
    """Clase que representa una región con sus propios servidores y balanceadores de carga."""
    def __init__(self, name):
        self.name = name
        self.servers = []
        self.load_balancer = LoadBalancer()

    def add_server(self, server):
        """Añade un servidor a la región y al balanceador de carga."""
        self.servers.append(server)
        self.load_balancer.add_server(server)
        logging.info(f'Server {server.name} added to region {self.name}.')

    def handle_request(self, request):
        """Maneja una solicitud utilizando el balanceador de carga de la región."""
        logging.info(f'Region {self.name} handling request: {request}')
        return self.load_balancer.distribute_http_requests([request])

class MultiRegionHA:
    """Clase que gestiona múltiples regiones para alta disponibilidad."""
    def __init__(self):
        self.regions = []

    def add_region(self, region):
        """Añade una región al sistema de alta disponibilidad."""
        self.regions.append(region)
        logging.info(f'Region {region.name} added to Multi-Region HA system.')

    def route_request(self, request):
        """Enruta una solicitud entre múltiples regiones, con conmutación por error."""
        primary_region = self.regions[0]
        secondary_region = self.regions[1]
        try:
            logging.info(f'Routing request to primary region: {primary_region.name}')
            return primary_region.handle_request(request)
        except Exception as e:
            logging.error(f"Primary region {primary_region.name} failed: {e}")
            logging.info(f'Routing request to secondary region: {secondary_region.name}')
            return secondary_region.handle_request(request)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear regiones
    region1 = Region("us-east-1")
    region2 = Region("us-west-1")

    # Crear servidores
    server1 = Server("Server 1")
    server2 = Server("Server 2")

    # Añadir servidores a las regiones
    region1.add_server(server1)
    region2.add_server(server2)

    # Crear sistema de alta disponibilidad multi-región
    ha_system = MultiRegionHA()
    ha_system.add_region(region1)
    ha_system.add_region(region2)

    # Simular la llegada de una solicitud
    request = "Request 1"
    response = ha_system.route_request(request)
    logging.info(f'Response: {response}')
