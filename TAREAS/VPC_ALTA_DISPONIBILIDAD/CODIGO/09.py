import logging
import random

# Configuración del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Packet:
    def __init__(self, data: str):
        self.data = data
        self.header = {}
        self.footer = {}

    def __repr__(self):
        return f"Packet(data={self.data}, header={self.header}, footer={self.footer})"

class OSIModel:
    def __init__(self, packet: Packet):
        self.packet = packet

    def application_layer(self):
        """Simula el procesamiento en la capa de Aplicación"""
        self.packet.header['Application'] = 'Application Header'
        logging.info(f'Capa de Aplicación: {self.packet}')

    def presentation_layer(self):
        """Simula el procesamiento en la capa de Presentación"""
        self.packet.data = self.packet.data.encode('utf-8').hex()
        self.packet.header['Presentation'] = 'Presentation Header'
        logging.info(f'Capa de Presentación: {self.packet}')

    def session_layer(self):
        """Simula el procesamiento en la capa de Sesión"""
        self.packet.header['Session'] = 'Session Header'
        logging.info(f'Capa de Sesión: {self.packet}')

    def transport_layer(self):
        """Simula el procesamiento en la capa de Transporte"""
        self.packet.header['Transport'] = 'Transport Header'
        self.packet.footer['Transport'] = 'Transport Footer'
        logging.info(f'Capa de Transporte: {self.packet}')

    def network_layer(self):
        """Simula el procesamiento en la capa de Red"""
        self.packet.header['Network'] = f'Network Header (Routing: {random.randint(1, 255)})'
        logging.info(f'Capa de Red: {self.packet}')

    def data_link_layer(self):
        """Simula el procesamiento en la capa de Enlace de Datos"""
        self.packet.header['Data Link'] = 'Data Link Header'
        self.packet.footer['Data Link'] = 'Data Link Footer'
        logging.info(f'Capa de Enlace de Datos: {self.packet}')

    def physical_layer(self):
        """Simula el procesamiento en la capa Física"""
        self.packet.header['Physical'] = 'Physical Header'
        logging.info(f'Capa Física: {self.packet}')

    def process_packet(self):
        """Procesa el paquete a través de todas las capas del modelo OSI"""
        self.application_layer()
        self.presentation_layer()
        self.session_layer()
        self.transport_layer()
        self.network_layer()
        self.data_link_layer()
        self.physical_layer()
        logging.info(f'Paquete finalizado: {self.packet}')

# Crear un paquete de datos
packet = Packet(data="Hello, World!")

# Crear el modelo OSI y procesar el paquete
osi_model = OSIModel(packet)
osi_model.process_packet()
