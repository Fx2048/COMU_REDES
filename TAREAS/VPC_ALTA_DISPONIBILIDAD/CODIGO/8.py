import logging
import random
import time

# Configuración del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Server:
    def __init__(self, id: int, cpu_capacity: int, memory_capacity: int):
        self.id = id
        self.cpu_capacity = cpu_capacity
        self.memory_capacity = memory_capacity
        self.current_load = 0

    def handle_request(self, load: int):
        """Simula el manejo de una solicitud en el servidor"""
        if self.current_load + load <= self.cpu_capacity:
            self.current_load += load
            logging.info(f'Servidor {self.id} manejando solicitud. Carga actual: {self.current_load}')
        else:
            logging.warning(f'Servidor {self.id} sobrecargado. Carga actual: {self.current_load}')

    def scale_up(self, additional_cpu: int, additional_memory: int):
        """Escala verticalmente el servidor agregando más capacidad de CPU y memoria"""
        self.cpu_capacity += additional_cpu
        self.memory_capacity += additional_memory
        logging.info(f'Servidor {self.id} escalado verticalmente. Nueva capacidad de CPU: {self.cpu_capacity}, Memoria: {self.memory_capacity}')

    def __repr__(self):
        return f"Server(id={self.id}, cpu_capacity={self.cpu_capacity}, memory_capacity={self.memory_capacity}, current_load={self.current_load})"

class ServerCluster:
    def __init__(self):
        self.servers = []

    def add_server(self, server: Server):
        """Añade un servidor al clúster"""
        self.servers.append(server)
        logging.info(f'Servidor añadido: {server.id}')

    def remove_server(self, server: Server):
        """Elimina un servidor del clúster"""
        self.servers.remove(server)
        logging.info(f'Servidor eliminado: {server.id}')

    def distribute_load(self, load: int):
        """Distribuye la carga entre los servidores disponibles"""
        if not self.servers:
            logging.error('No hay servidores disponibles para manejar la solicitud')
            return
        server = min(self.servers, key=lambda s: s.current_load)
        server.handle_request(load)

    def __repr__(self):
        return f"ServerCluster(servers={self.servers})"

class AutoScaler:
    def __init__(self, cluster: ServerCluster, cpu_threshold: float, memory_threshold: float):
        self.cluster = cluster
        self.cpu_threshold = cpu_threshold
        self.memory_threshold = memory_threshold

    def scale(self):
        """Ajusta automáticamente la capacidad del clúster"""
        total_cpu_capacity = sum(server.cpu_capacity for server in self.cluster.servers)
        total_memory_capacity = sum(server.memory_capacity for server in self.cluster.servers)
        total_load = sum(server.current_load for server in self.cluster.servers)

        cpu_utilization = total_load / total_cpu_capacity
        logging.info(f'Utilización de CPU: {cpu_utilization:.2f}')
        
        if cpu_utilization > self.cpu_threshold:
            new_server = Server(id=len(self.cluster.servers) + 1, cpu_capacity=100, memory_capacity=100)
            self.cluster.add_server(new_server)
            logging.info(f'Escalado horizontal: Añadido servidor {new_server.id}')
        elif cpu_utilization < (self.cpu_threshold / 2) and len(self.cluster.servers) > 1:
            server_to_remove = self.cluster.servers[-1]
            self.cluster.remove_server(server_to_remove)
            logging.info(f'Escalado horizontal: Eliminado servidor {server_to_remove.id}')

class TrafficSimulator:
    def __init__(self, cluster: ServerCluster, auto_scaler: AutoScaler):
        self.cluster = cluster
        self.auto_scaler = auto_scaler

    def simulate_traffic(self, duration: int):
        """Simula la llegada de solicitudes durante un periodo de tiempo"""
        start_time = time.time()
        while time.time() - start_time < duration:
            load = random.randint(1, 50)
            self.cluster.distribute_load(load)
            self.auto_scaler.scale()
            time.sleep(1)

# Crear un clúster de servidores y un autoescalador
cluster = ServerCluster()
initial_server = Server(id=1, cpu_capacity=100, memory_capacity=100)
cluster.add_server(initial_server)

auto_scaler = AutoScaler(cluster=cluster, cpu_threshold=0.75, memory_threshold=0.75)

# Crear el simulador de tráfico
traffic_simulator = TrafficSimulator(cluster=cluster, auto_scaler=auto_scaler)

# Simular tráfico durante 60 segundos
traffic_simulator.simulate_traffic(duration=60)

# Imprimir el estado final del clúster
logging.info(f'Estado final del clúster: {cluster}')
