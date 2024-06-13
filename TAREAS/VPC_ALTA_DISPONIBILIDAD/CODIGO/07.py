import logging

# Configuración del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Server:
    """Clase que representa un servidor."""
    def __init__(self):
        self.load = 0

    def __repr__(self):
        return f"Server(load={self.load})"

class ServerTemplate:
    """Clase que define la plantilla para crear nuevos servidores."""
    def create_server(self):
        """Crea y retorna una nueva instancia de Server."""
        return Server()

class CustomAutoScalingGroup:
    """Clase que gestiona un grupo de servidores con escalado automático."""
    def __init__(self, template: ServerTemplate, min_size: int, max_size: int, scaling_policy):
        self.template = template
        self.min_size = min_size
        self.max_size = max_size
        self.scaling_policy = scaling_policy
        self.servers = [self.template.create_server() for _ in range(min_size)]
        logging.info(f"Inicializado Auto Scaling Group con {len(self.servers)} servidores")

    def scale_out(self):
        """Añade un servidor al grupo si no se ha alcanzado el tamaño máximo."""
        if len(self.servers) < self.max_size:
            self.servers.append(self.template.create_server())
            logging.info("Scaled out: Añadido un servidor")
        else:
            logging.warning("No se puede escalar más: Se alcanzó el tamaño máximo del grupo")

    def scale_in(self):
        """Elimina un servidor del grupo si no se ha alcanzado el tamaño mínimo."""
        if len(self.servers) > self.min_size:
            self.servers.pop()
            logging.info("Scaled in: Eliminado un servidor")
        else:
            logging.warning("No se puede reducir más: Se alcanzó el tamaño mínimo del grupo")

    def adjust_capacity(self, metric_values):
        """Ajusta dinámicamente la capacidad del grupo basado en las métricas proporcionadas."""
        if self.scaling_policy(metric_values):
            self.scale_out()
        else:
            self.scale_in()
        logging.info(f"Estado actual del grupo: {self.servers}")

def custom_scaling_policy(metric_values):
    """Política de escalado personalizada basada en el promedio de las métricas."""
    return sum(metric_values) / len(metric_values) > 70

# Ejemplo de uso del sistema de Auto Scaling
if __name__ == "__main__":
    template = ServerTemplate()
    asg = CustomAutoScalingGroup(template=template, min_size=2, max_size=5, scaling_policy=custom_scaling_policy)
    
    # Simulación de métricas de carga y ajuste de capacidad
    simulated_metrics = [50, 60, 80]
    logging.info(f"Métricas simuladas: {simulated_metrics}")
    asg.adjust_capacity(simulated_metrics)
