import logging

# Configuración del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WebApplicationFirewall:
    """Clase que representa un firewall para aplicaciones web."""
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        """Añade una regla de protección al WAF."""
        self.rules.append(rule)
        logging.info(f'Regla añadida: {rule.__name__}')

    def apply_rules(self, request):
        """Aplica todas las reglas al request proporcionado.
        
        Args:
            request (dict): Diccionario que representa una solicitud web con claves 'ip', 'query' y 'content'.
        
        Returns:
            bool: True si la solicitud pasa todas las reglas, False si alguna regla la bloquea.
        """
        for rule in self.rules:
            if not rule(request):
                logging.warning(f'Solicitud bloqueada por la regla: {rule.__name__}')
                return False
        logging.info('Solicitud aprobada por el WAF')
        return True

def block_ip_rule(request):
    """Regla para bloquear solicitudes basadas en la IP."""
    blocked_ips = {"192.168.0.1"}
    return request["ip"] not in blocked_ips

def sql_injection_rule(request):
    """Regla para prevenir ataques de SQL injection."""
    sql_keywords = {"select", "drop", "insert", "delete"}
    return not any(keyword in request["query"].lower() for keyword in sql_keywords)

def xss_rule(request):
    """Regla para prevenir ataques de Cross-Site Scripting (XSS)."""
    return "<script>" not in request["content"].lower()

class LoadBalancer:
    """Clase que representa un balanceador de carga para distribuir tráfico a múltiples servidores."""
    def __init__(self, waf):
        self.waf = waf
        self.servers = []

    def add_server(self, server):
        """Añade un servidor al balanceador de carga."""
        self.servers.append(server)
        logging.info(f'Servidor añadido: {server}')

    def handle_request(self, request):
        """Maneja una solicitud aplicando el WAF antes de distribuirla a un servidor."""
        if self.waf.apply_rules(request):
            server = self.servers[0]  # Simulación de elección de servidor
            logging.info(f'Solicitud enviada al servidor: {server}')
            return server.handle_request(request)
        else:
            logging.warning('Solicitud bloqueada por el WAF')
            return "Request blocked by WAF"

class Server:
    """Clase que representa un servidor web."""
    def __init__(self, id):
        self.id = id

    def handle_request(self, request):
        """Simula el manejo de una solicitud en el servidor."""
        logging.info(f'Servidor {self.id} manejando solicitud con contenido: {request["content"]}')
        return f"Request handled by server {self.id}"

# Ejemplo de uso
if __name__ == "__main__":
    # Crear y configurar el WAF
    waf = WebApplicationFirewall()
    waf.add_rule(block_ip_rule)
    waf.add_rule(sql_injection_rule)
    waf.add_rule(xss_rule)

    # Crear un balanceador de carga y añadir servidores
    lb = LoadBalancer(waf=waf)
    server1 = Server(id=1)
    server2 = Server(id=2)
    lb.add_server(server1)
    lb.add_server(server2)

    # Simular una solicitud web
    request = {
        "ip": "192.168.0.2",
        "query": "SELECT * FROM users",
        "content": "Hello World"
    }
    response = lb.handle_request(request)
    logging.info(f'Respuesta: {response}')
