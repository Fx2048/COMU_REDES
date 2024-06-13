class PhysicalLayer:
    def transmit(self, data):
        # Simula la transmisión física de bits
        print(f"Transmitiendo bits: {data}")

class DataLinkLayer:
    def __init__(self):
        self.connections = {}

    def add_connection(self, source, destination):
        # Establece una conexión lógica entre dos dispositivos
        self.connections[source] = destination

    def send_frame(self, source, data):
        # Agrega encabezados y envía el marco
        destination = self.connections.get(source)
        if destination:
            print(f"Enviando marco desde {source} a {destination}: {data}")

class NetworkLayer:
    def route_packet(self, source, destination, data):
        # Encamina el paquete a través de la red
        print(f"Encaminando paquete desde {source} a {destination}: {data}")

class TransportLayer:
    def send_segment(self, source, destination, data):
        # Divide los datos en segmentos y agrega números de secuencia
        print(f"Enviando segmento desde {source} a {destination}: {data}")

class ApplicationLayer:
    def send_request(self, data):
        # Crea una solicitud HTTP
        print(f"Enviando solicitud HTTP: {data}")

# Ejemplo de uso
physical = PhysicalLayer()
datalink = DataLinkLayer()
network = NetworkLayer()
transport = TransportLayer()
application = ApplicationLayer()

datalink.add_connection("Navegador", "Servidor")
datalink.send_frame("Navegador", "Datos del navegador")

network.route_packet("Navegador", "Servidor", "Datos de red")

transport.send_segment("Navegador", "Servidor", "Datos de transporte")

application.send_request("GET /index.html HTTP/1.1")
