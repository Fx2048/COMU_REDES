class AutoScalingGroup:
    """Clase que gestiona un grupo de servidores con Auto Scaling."""
    def __init__(self, template, min_size, max_size):
        self.template = template  # Plantilla para crear servidores
        self.min_size = min_size  # Tamaño mínimo del grupo
        self.max_size = max_size  # Tamaño máximo del grupo
        self.servers = [self.template.create_server() for _ in range(min_size)]  # Lista inicial de servidores
        self.cpu_usage_threshold = 70  # Umbral de uso de CPU para decidir escalado

    def scale_out(self):
        """Añade un servidor si el tamaño actual es menor que el máximo."""
        if len(self.servers) < self.max_size:
            self.servers.append(self.template.create_server())
            print("Scaled out: Added a server")

    def scale_in(self):
        """Elimina un servidor si el tamaño actual es mayor que el mínimo."""
        if len(self.servers) > self.min_size:
            self.servers.pop()
            print("Scaled in: Removed a server")

    def adjust_capacity(self, cpu_usages):
        """
        Ajusta dinámicamente la capacidad del grupo basado en el uso de CPU promedio.
        Se simula comparando el promedio de uso de CPU con un umbral predefinido.
        """
        if not cpu_usages:
            return
        
        average_cpu_usage = sum(cpu_usages) / len(cpu_usages)

        if average_cpu_usage > self.cpu_usage_threshold:
            self.scale_out()
        elif average_cpu_usage < self.cpu_usage_threshold:
            self.scale_in()

class ServerTemplate:
    """Clase que define la plantilla para crear servidores."""
    def create_server(self):
        """Crea y devuelve una instancia de servidor."""
        return Server()

class Server:
    """Clase que representa un servidor."""
    pass  # En esta implementación, Server no necesita métodos específicos

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de la plantilla de servidor
    template = ServerTemplate()

    # Crear un grupo de Auto Scaling con una capacidad inicial de 2 a 5 servidores
    asg = AutoScalingGroup(template=template, min_size=2, max_size=5)

    # Simular métricas de uso de CPU (en este caso, valores simulados)
    cpu_usages = [50, 60, 80]

    # Ajustar la capacidad del grupo basado en las métricas simuladas
    asg.adjust_capacity(cpu_usages)

    # Imprimir el estado actual de los servidores (por ejemplo, la cantidad actual)
    print(f"Current number of servers: {len(asg.servers)}")
