import random
import time
import logging
from typing import List

# Configuración del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ServerTemplate:
    def __init__(self, cpu_capacity: int, memory_capacity: int):
        self.cpu_capacity = cpu_capacity
        self.memory_capacity = memory_capacity

    def create_server(self, id: int):
        """Crea una instancia de servidor basada en la plantilla"""
        return Server(id, self.cpu_capacity, self.memory_capacity)

class Server:
    def __init__(self, id: int, cpu_capacity: int, memory_capacity: int):
        self.id = id
        self.cpu_capacity = cpu_capacity
        self.memory_capacity = memory_capacity
        self.cpu_usage = 0
        self.memory_usage = 0

    def simulate_load(self):
        """Simula la carga en el servidor"""
        self.cpu_usage = random.uniform(0, self.cpu_capacity)
        self.memory_usage = random.uniform(0, self.memory_capacity)

    def __repr__(self):
        return f"Server(id={self.id}, cpu_usage={self.cpu_usage:.2f}/{self.cpu_capacity}, memory_usage={self.memory_usage:.2f}/{self.memory_capacity})"

class AutoScalingGroup:
    def __init__(self, server_template: ServerTemplate, min_size: int, max_size: int):
        self.server_template = server_template
        self.min_size = min_size
        self.max_size = max_size
        self.servers = [server_template.create_server(i) for i in range(min_size)]
        self.scaling_policy = self.default_scaling_policy

    def add_server(self):
        """Añade un nuevo servidor al grupo"""
        if len(self.servers) < self.max_size:
            new_server = self.server_template.create_server(len(self.servers))
            self.servers.append(new_server)
            logging.info(f'Servidor añadido: {new_server.id}')
        else:
            logging.info('El grupo ha alcanzado el tamaño máximo. No se pueden añadir más servidores.')

    def remove_server(self):
        """Elimina el servidor menos ocupado del grupo"""
        if len(self.servers) > self.min_size:
            server_to_remove = min(self.servers, key=lambda s: s.cpu_usage + s.memory_usage)
            self.servers.remove(server_to_remove)
            logging.info(f'Servidor eliminado: {server_to_remove.id}')
        else:
            logging.info('El grupo ha alcanzado el tamaño mínimo. No se pueden eliminar más servidores.')

    def default_scaling_policy(self):
        """Política de escalado basada en uso de CPU y memoria"""
        avg_cpu_usage = sum(server.cpu_usage for server in self.servers) / len(self.servers)
        avg_memory_usage = sum(server.memory_usage for server in self.servers) / len(self.servers)
        logging.info(f'Métricas promedio - CPU: {avg_cpu_usage:.2f}%, Memoria: {avg_memory_usage:.2f}%')

        if avg_cpu_usage > 70 or avg_memory_usage > 70:
            self.add_server()
        elif avg_cpu_usage < 30 and avg_memory_usage < 30:
            self.remove_server()

    def set_scaling_policy(self, policy_function):
        """Define una política de escalado personalizada"""
        self.scaling_policy = policy_function

    def simulate_load(self):
        """Simula la carga en el grupo de servidores"""
        for server in self.servers:
            server.simulate_load()

    def adjust_capacity(self):
        """Ajusta la capacidad del grupo de servidores según la política de escalado"""
        self.simulate_load()
        self.scaling_policy()

class LoadSimulator:
    def __init__(self, auto_scaling_group: AutoScalingGroup):
        self.auto_scaling_group = auto_scaling_group

    def simulate_traffic(self, duration: int):
        """Simula tráfico variable durante un periodo de tiempo"""
        start_time = time.time()
        while time.time() - start_time < duration:
            self.auto_scaling_group.adjust_capacity()
            logging.info(f'Estado del grupo de servidores: {self.auto_scaling_group.servers}')
            time.sleep(1)

# Definir una plantilla de servidor
server_template = ServerTemplate(cpu_capacity=100, memory_capacity=100)

# Crear un grupo de autoescalado con la plantilla de servidor
auto_scaling_group = AutoScalingGroup(server_template, min_size=2, max_size=5)

# Crear simulador de carga
load_simulator = LoadSimulator(auto_scaling_group)

# Simular tráfico variable durante 30 segundos
load_simulator.simulate_traffic(duration=30)
