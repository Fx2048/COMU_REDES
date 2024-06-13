import time
import random
import logging
from typing import List

# Configuración del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Server:
    def __init__(self, id):
        self.id = id
        self.is_healthy = True
        self.response_time = random.uniform(0.1, 0.5)  # Tiempo de respuesta simulado
        self.cpu_usage = random.uniform(10, 50)  # Uso de CPU simulado en porcentaje
        self.memory_usage = random.uniform(30, 70)  # Uso de memoria simulado en porcentaje
        self.network_latency = random.uniform(20, 100)  # Latencia de red simulada en ms

    def simulate_activity(self):
        """Simula la actividad del servidor y actualiza sus métricas"""
        self.response_time = random.uniform(0.1, 0.5)
        self.cpu_usage = random.uniform(10, 50)
        self.memory_usage = random.uniform(30, 70)
        self.network_latency = random.uniform(20, 100)

    def simulate_failure(self):
        """Simula un fallo en el servidor"""
        self.is_healthy = False

    def recover(self):
        """Recupera el servidor a un estado saludable"""
        self.is_healthy = True

class HealthMonitor:
    def __init__(self, servers: List[Server]):
        self.servers = servers

    def check_health(self):
        """Verifica la salud de todos los servidores y devuelve los servidores no saludables"""
        unhealthy_servers = []
        for server in self.servers:
            server.simulate_activity()
            if not self.is_server_healthy(server):
                unhealthy_servers.append(server)
                logging.warning(f'Servidor {server.id} no saludable: '
                                f'Tiempo de respuesta={server.response_time}, '
                                f'CPU={server.cpu_usage}%, Memoria={server.memory_usage}%, '
                                f'Latencia de red={server.network_latency}ms')
        return unhealthy_servers

    def is_server_healthy(self, server: Server) -> bool:
        """Evalúa si un servidor es saludable en función de sus métricas"""
        return (server.response_time < 0.4 and server.cpu_usage < 80 and
                server.memory_usage < 80 and server.network_latency < 150 and server.is_healthy)

class RecoveryManager:
    def __init__(self, servers: List[Server]):
        self.servers = servers

    def recover_unhealthy_servers(self, unhealthy_servers: List[Server]):
        """Recupera servidores no saludables"""
        for server in unhealthy_servers:
            server.recover()
            logging.info(f'Servidor {server.id} recuperado')

class LoadBalancer:
    def __init__(self, servers: List[Server], health_monitor: HealthMonitor, recovery_manager: RecoveryManager):
        self.servers = servers
        self.health_monitor = health_monitor
        self.recovery_manager = recovery_manager

    def balance_load(self):
        """Balancea la carga entre los servidores, asegurando que el tráfico se dirija a servidores saludables"""
        while True:
            unhealthy_servers = self.health_monitor.check_health()
            if unhealthy_servers:
                self.recovery_manager.recover_unhealthy_servers(unhealthy_servers)
            healthy_servers = [server for server in self.servers if server.is_healthy]
            if healthy_servers:
                logging.info(f'Dirigiendo tráfico a servidores saludables: {[server.id for server in healthy_servers]}')
            else:
                logging.error('No hay servidores saludables disponibles!')
            time.sleep(5)  # Intervalo de monitoreo

class FaultSimulator:
    def __init__(self, servers: List[Server]):
        self.servers = servers

    def simulate_faults(self):
        """Simula fallos en el sistema aleatoriamente"""
        while True:
            time.sleep(random.randint(5, 15))
            faulty_server = random.choice(self.servers)
            faulty_server.simulate_failure()
            logging.warning(f'Servidor {faulty_server.id} ha fallado')

# Crear servidores
servers = [Server(id=i) for i in range(5)]

# Crear instancias de monitor de salud, gestor de recuperación y balanceador de carga
health_monitor = HealthMonitor(servers)
recovery_manager = RecoveryManager(servers)
load_balancer = LoadBalancer(servers, health_monitor, recovery_manager)

# Simular fallos en el sistema
fault_simulator = FaultSimulator(servers)

# Iniciar el balanceador de carga y el simulador de fallos en hilos separados
import threading

load_balancer_thread = threading.Thread(target=load_balancer.balance_load)
fault_simulator_thread = threading.Thread(target=fault_simulator.simulate_faults)

load_balancer_thread.start()
fault_simulator_thread.start()

load_balancer_thread.join()
fault_simulator_thread.join()
