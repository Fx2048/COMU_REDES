class Server:
    def __init__(self, cpu_capacity: int, memory_capacity: int):
        """
        Inicializa un objeto Server con la capacidad de CPU y memoria especificada.

        Args:
            cpu_capacity (int): Capacidad de CPU del servidor.
            memory_capacity (int): Capacidad de memoria del servidor.
        """
        self.cpu_capacity = cpu_capacity
        self.memory_capacity = memory_capacity
        self.current_load = 0

    def scale_up(self, additional_cpu: int, additional_memory: int):
        """
        Escala verticalmente el servidor agregando recursos adicionales de CPU y memoria.

        Args:
            additional_cpu (int): Capacidad adicional de CPU a agregar.
            additional_memory (int): Capacidad adicional de memoria a agregar.
        """
        self.cpu_capacity += additional_cpu
        self.memory_capacity += additional_memory

    def __str__(self):
        """
        Devuelve una representación en cadena del objeto Server.

        Returns:
            str: Cadena que representa el objeto Server.
        """
        return f"CPU: {self.cpu_capacity}, Memory: {self.memory_capacity}, Load: {self.current_load}"


class ServerCluster:
    def __init__(self):
        """
        Inicializa un objeto ServerCluster con una lista vacía de servidores.
        """
        self.servers = []

    def add_server(self, server: Server):
        """
        Agrega un servidor al clúster.

        Args:
            server (Server): Objeto Server a agregar al clúster.
        """
        self.servers.append(server)

    def remove_server(self):
        """
        Elimina el último servidor del clúster.
        """
        if self.servers:
            self.servers.pop()

    def distribute_load(self, load: int):
        """
        Distribuye una carga de trabajo entre los servidores del clúster.

        Args:
            load (int): Carga de trabajo a distribuir.
        """
        if not self.servers:
            print("No servers available.")
            return

        load_per_server = load / len(self.servers)
        for server in self.servers:
            server.current_load += load_per_server

    def report_cluster_status(self):
        """
        Imprime el estado actual del clúster, incluyendo la información de cada servidor.
        """
        print("Cluster Status:")
        for server in self.servers:
            print(f"Server: {server}")

    def scale_vertically(self, server_index: int, additional_cpu: int, additional_memory: int):
        """
        Escala verticalmente un servidor específico del clúster.

        Args:
            server_index (int): Índice del servidor a escalar.
            additional_cpu (int): Capacidad adicional de CPU a agregar.
            additional_memory (int): Capacidad adicional de memoria a agregar.
        """
        if 0 <= server_index < len(self.servers):
            server = self.servers[server_index]
            server.scale_up(additional_cpu, additional_memory)
            print(f"Server {server_index} has been scaled up vertically.")
        else:
            print("Invalid server index.")

    def scale_horizontally(self, cpu_capacity: int, memory_capacity: int):
        """
        Escala horizontalmente el clúster agregando un nuevo servidor.

        Args:
            cpu_capacity (int): Capacidad de CPU del nuevo servidor.
            memory_capacity (int): Capacidad de memoria del nuevo servidor.
        """
        new_server = Server(cpu_capacity, memory_capacity)
        self.add_server(new_server)
        print("New server added for horizontal scaling.")


# caso de uso 
server1 = Server(cpu_capacity=4, memory_capacity=8)
server2 = Server(cpu_capacity=4, memory_capacity=8)

cluster = ServerCluster()
cluster.add_server(server1)
cluster.add_server(server2)

cluster.distribute_load(10)
cluster.report_cluster_status()

cluster.scale_vertically(0, 2, 4)
cluster.report_cluster_status()

cluster.scale_horizontally(6, 12)
cluster.report_cluster_status()
