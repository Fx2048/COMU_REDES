class Server:# Atributos de server
    def __init__(self, cpu_capacity, memory_capacity):
        """
        Clase que representa un servidor con atributos de capacidad de CPU, capacidad de memoria y carga actual.

        Args:
            cpu_capacity (float): Capacidad de CPU del servidor.
            memory_capacity (float): Capacidad de memoria del servidor.
        """
        self.cpu_capacity = cpu_capacity
        self.memory_capacity = memory_capacity
        self.current_load = 0
#Aumentar capacidad de server
    def scale_up(self, additional_cpu, additional_memory):
        """
        Simula la escalabilidad vertical aumentando la capacidad del servidor.

        Args:
            additional_cpu (float): Capacidad de CPU adicional a agregar.
            additional_memory (float): Capacidad de memoria adicional a agregar.
        """
        self.cpu_capacity += additional_cpu
        self.memory_capacity += additional_memory

#funciones en el cluster

class ServerCluster:
    def __init__(self):
        """
        Clase que simula un clúster de servidores.
        """
        self.servers = []

    def add_server(self, server):
        """
        Agrega un servidor al clúster.

        Args:
            server (Server): Instancia de la clase Server a agregar.
        """
        self.servers.append(server)

    def remove_server(self):
        """
        Elimina el último servidor agregado al clúster (si hay servidores disponibles).
        """
        if self.servers:
            self.servers.pop()

    def distribute_load(self, load):
        """
        Distribuye la carga entre los servidores del clúster.

        Args:
            load (float): Carga total a distribuir entre los servidores.
        """
        if not self.servers:
            print("No hay servidores disponibles.")
            return

        load_per_server = load / len(self.servers)
        for server in self.servers:
            server.current_load += load_per_server


# Ejemplo de uso
server1 = Server(cpu_capacity=4, memory_capacity=8)
server2 = Server(cpu_capacity=4, memory_capacity=8)
cluster = ServerCluster()
cluster.add_server(server1)
cluster.add_server(server2)
cluster.distribute_load(10)
