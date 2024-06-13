import random
import time
import logging
from typing import List

# Configuración del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Server:
    def __init__(self, id, weight=1):
        self.id = id
        self.weight = weight
        self.connections = 0
        self.cpu_usage = random.uniform(10, 50)
        self.memory_usage = random.uniform(30, 70)
        self.network_traffic = random.uniform(20, 100)

    def simulate_activity(self):
        """Simula la actividad del servidor y actualiza sus métricas"""
        self.cpu_usage = random.uniform(10, 50)
        self.memory_usage = random.uniform(30, 70)
        self.network_traffic = random.uniform(20, 100)
        self.connections = random.randint(0, 10)

    def __repr__(self):
        return f"Server(id={self.id}, weight={self.weight}, connections={self.connections}, " \
               f"cpu_usage={self.cpu_usage:.2f}, memory_usage={self.memory_usage:.2f}, " \
               f"network_traffic={self.network_traffic:.2f})"

class LoadBalancer:
    def __init__(self, servers: List[Server]):
        self.servers = servers
        self.last_server_index = -1

    def round_robin(self):
        """Distribuye las solicitudes utilizando el algoritmo round-robin"""
        self.last_server_index = (self.last_server_index + 1) % len(self.servers)
        return self.servers[self.last_server_index]

    def least_connections(self):
        """Distribuye las solicitudes al servidor con menos conexiones"""
        return min(self.servers, key=lambda s: s.connections)

    def weighted_distribution(self):
        """Distribuye las solicitudes basado en la ponderación de los servidores"""
        total_weight = sum(server.weight for server in self.servers)
        choice = random.uniform(0, total_weight)
        upto = 0
        for server in self.servers:
            if upto + server.weight >= choice:
                return server
            upto += server.weight

class AutoScalingGroup:
    def __init__(self, initial_servers: List[Server], max_servers: int):
        self.servers = initial_servers
        self.max_servers = max_servers

    def scale_up(self):
        """Escala hacia arriba agregando una nueva instancia de servidor"""
        if len(self.servers) < self.max_servers:
            new_server = Server(id=len(self.servers))
            self.servers.append(new_server)
            logging.info(f'Escalando hacia arriba: Añadido servidor {new_server.id}')
        else:
            logging.info('Máximo número de servidores alcanzado, no se puede escalar más hacia arriba')

    def scale_down(self):
        """Escala hacia abajo eliminando la instancia de servidor menos ocupada"""
        if len(self.servers) > 1:
            server_to_remove = min(self.servers, key=lambda s: s.connections)
            self.servers.remove(server_to_remove)
            logging.info(f'Escalando hacia abajo: Eliminado servidor {server_to_remove.id}')
        else:
            logging.info('Número mínimo de servidores alcanzado, no se puede escalar más hacia abajo')

    def monitor_and_scale(self):
        """Monitorea las métricas de los servidores y ajusta la escala del grupo"""
        avg_cpu = sum(server.cpu_usage for server in self.servers) / len(self.servers)
        avg_memory = sum(server.memory_usage for server in self.servers) / len(self.servers)
        avg_traffic = sum(server.network_traffic for server in self.servers) / len(self.servers)

        logging.info(f'Métricas promedio - CPU: {avg_cpu:.2f}%, Memoria: {avg_memory:.2f}%, Tráfico de red: {avg_traffic:.2f}')

        if avg_cpu > 70 or avg_memory > 70 or avg_traffic > 70:
            self.scale_up()
        elif avg_cpu < 30 and avg_memory < 30 and avg_traffic < 30:
            self.scale_down()

class TrafficSimulator:
    def __init__(self, load_balancer: LoadBalancer, auto_scaling_group: AutoScalingGroup):
        self.load_balancer = load_balancer
        self.auto_scaling_group = auto_scaling_group

    def simulate_traffic(self, duration: int):
        """Simula tráfico web durante un periodo de tiempo especificado"""
        start_time = time.time()
        while time.time() - start_time < duration:
            # Simula solicitudes entrantes utilizando diferentes algoritmos de balanceo de carga
            for algorithm in [self.load_balancer.round_robin, self.load_balancer.least_connections, self.load_balancer.weighted_distribution]:
                server = algorithm()
                server.simulate_activity()
                logging.info(f'Solicitud manejada por {server}')

            # Monitorea y ajusta la escala de los servidores
            self.auto_scaling_group.monitor_and_scale()

            time.sleep(1)

# Crear instancias de servidores iniciales
initial_servers = [Server(id=i) for i in range(3)]

# Crear instancia del grupo de autoescalado y balanceador de carga
auto_scaling_group = AutoScalingGroup(initial_servers, max_servers=5)
load_balancer = LoadBalancer(initial_servers)

# Crear simulador de tráfico
traffic_simulator = TrafficSimulator(load_balancer, auto_scaling_group)

# Simular tráfico web durante 30 segundos
traffic_simulator.simulate_traffic(duration=30)
