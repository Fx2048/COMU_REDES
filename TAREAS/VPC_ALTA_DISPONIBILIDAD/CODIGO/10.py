import random
import time
import logging
from typing import List, Dict

# Configuración del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Server:
    def __init__(self, id: int):
        self.id = id
        self.active_connections = 0

    def handle_request(self):
        """Simula el manejo de una solicitud en el servidor"""
        self.active_connections += 1
        logging.info(f'Servidor {self.id} manejando solicitud. Conexiones activas: {self.active_connections}')

    def release_connection(self):
        """Simula la liberación de una conexión"""
        if self.active_connections > 0:
            self.active_connections -= 1
        logging.info(f'Servidor {self.id} liberó una conexión. Conexiones activas: {self.active_connections}')

    def __repr__(self):
        return f"Server(id={self.id}, active_connections={self.active_connections})"

class LoadBalancer:
    def __init__(self):
        self.servers = []
        self.policy = None

    def add_server(self, server: Server):
        """Añade un servidor al balanceador"""
        self.servers.append(server)
        logging.info(f'Servidor añadido: {server.id}')

    def remove_server(self, server: Server):
        """Elimina un servidor del balanceador"""
        self.servers.remove(server)
        logging.info(f'Servidor eliminado: {server.id}')

    def set_policy(self, policy_function):
        """Configura una política de distribución de carga"""
        self.policy = policy_function

    def distribute_request(self):
        """Distribuye una solicitud a un servidor según la política"""
        if self.policy:
            server = self.policy(self.servers)
            server.handle_request()
        else:
            logging.error('No se ha configurado una política de distribución de carga')

class ApplicationLoadBalancer(LoadBalancer):
    """Balanceador de carga de aplicación"""
    pass

class NetworkLoadBalancer(LoadBalancer):
    """Balanceador de carga de red"""
    pass

class ClassicLoadBalancer(LoadBalancer):
    """Balanceador de carga clásico"""
    pass

# Políticas de distribución de carga
def round_robin_policy(servers: List[Server]):
    """Política de distribución round-robin"""
    round_robin_policy.counter = (round_robin_policy.counter + 1) % len(servers)
    return servers[round_robin_policy.counter]
round_robin_policy.counter = -1

def least_connections_policy(servers: List[Server]):
    """Política de distribución de menos conexiones"""
    return min(servers, key=lambda s: s.active_connections)

def ip_hash_policy(servers: List[Server], ip: str):
    """Política de distribución basada en IP hash"""
    index = hash(ip) % len(servers)
    return servers[index]

class LoadBalancerMonitor:
    def __init__(self, load_balancer: LoadBalancer):
        self.load_balancer = load_balancer

    def log_metrics(self):
        """Registra métricas de rendimiento y estadísticas de distribución de carga"""
        total_connections = sum(server.active_connections for server in self.load_balancer.servers)
        logging.info(f'Total de conexiones activas: {total_connections}')
        for server in self.load_balancer.servers:
            logging.info(f'Servidor {server.id} - Conexiones activas: {server.active_connections}')

class TrafficSimulator:
    def __init__(self, load_balancers: List[LoadBalancer]):
        self.load_balancers = load_balancers

    def simulate_traffic(self, duration: int):
        """Simula tráfico de red durante un periodo de tiempo"""
        start_time = time.time()
        while time.time() - start_time < duration:
            for load_balancer in self.load_balancers:
                load_balancer.distribute_request()
            time.sleep(1)

        # Liberar conexiones
        for load_balancer in self.load_balancers:
            for server in load_balancer.servers:
                server.release_connection()

# Crear instancias de servidores
servers = [Server(id=i) for i in range(5)]

# Crear instancias de balanceadores de carga
alb = ApplicationLoadBalancer()
nlb = NetworkLoadBalancer()
clb = ClassicLoadBalancer()

# Añadir servidores a los balanceadores de carga
for server in servers:
    alb.add_server(server)
    nlb.add_server(server)
    clb.add_server(server)

# Configurar políticas de distribución de carga
alb.set_policy(round_robin_policy)
nlb.set_policy(least_connections_policy)
clb.set_policy(lambda servers: ip_hash_policy(servers, ip="192.168.0.1"))

# Crear monitores de balanceadores de carga
alb_monitor = LoadBalancerMonitor(alb)
nlb_monitor = LoadBalancerMonitor(nlb)
clb_monitor = LoadBalancerMonitor(clb)

# Crear simulador de tráfico
traffic_simulator = TrafficSimulator([alb, nlb, clb])

# Simular tráfico de red durante 30 segundos
traffic_simulator.simulate_traffic(duration=30)

# Registrar métricas de rendimiento
alb_monitor.log_metrics()
nlb_monitor.log_metrics()
clb_monitor.log_metrics()
