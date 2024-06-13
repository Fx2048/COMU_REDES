# Clase para el servidor
class Server:
    def __init__(self, cpu_capacity, memory_capacity):
        self.cpu_capacity = cpu_capacity
        self.memory_capacity = memory_capacity

# Clase para el clúster
class ServerCluster:
    def __init__(self):
        self.servers = []

    def add_server(self, server):
        self.servers.append(server)

    def distribute_load(self, load):
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

