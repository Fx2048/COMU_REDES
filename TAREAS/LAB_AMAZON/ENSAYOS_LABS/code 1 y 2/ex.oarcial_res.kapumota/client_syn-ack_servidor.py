import random
import time
class Servidor:
    def __init__(self):
        self.estado ="LISTENING"#escucha si está llegando un mensaje
    def recibir_syn(self):
        if random.choice([True,False]):
            print("Servidor:paquete syn recibido")
            self.estado="SYN_RECEIVED"
            return True
        else:
            print("Servidor = Paquete syn perdido")
            return False
    def enviar_syn_ack(self):
        if random.choice([True,False]):
            print("Servidor: paquete syn recibido")
            self.estado = " syn-ack recibido"
            return True
        else:
            print("Servidor:paquete syn no recibido :V")
            return False
    def recibir_ack(self):
        if random.choice([True,False]):
            print("Servidor:paquete ack recibido")
            self.estado="ack establecido"
            return True
        else:
            print("Servidor:paquete ack perdido")
            return False

class Cliente:
    def __init__(self):
        self.estado="Closed"
    def enviar_syn(self,servidor): # otra definicion extraña enviar
        print("Cliente:enviando syn")
        if servidor.recibir_syn():
            self.estado="Syn_sent"
            return True
        else:
            print("Ciente:Reintentando enviar SYN")
            return False
    def recibir_syn_ack(self,servidor):#otra defindion  #recibir syn ack 
        if servidor.enviar_syn_ack():
            print("Cliente:Paquete SYN-ACK recibido") # recibido 
            self.estado="SYN-RECEIVED"
            return True
        else:
            print("Cliente:Esperando SYN-ACK")#cliente esperando synack
            return False
    def enviar_ack(self,servidor):
        print("Cliente:Enviando ACK")
        if servidor.recibir_ack():
            self.estado="Established"
            print("Cliente:Conexión establecida")
            return True
        else:
            print("Cliente:Reintando enviar ACK")
            return False
def three_way_handshake(cliente,servidor):
    while not cliente.enviar_syn(servidor):
        time.sleep(1)
    while not cliente.recibir_syn_ack(servidor):
        time.sleep(1)
    while not cliente.enviar_ack(servidor):
        time.sleep(1)
cliente=Cliente()
servidor=Servidor()
three_way_handshake(cliente,servidor)

            
def multiple_client_handshake(clientes,servidor):
    for cliente in clientes:
        print(f"Iniciando handshake para el Cliente {clientes.index(cliente)+1}")
        three_way_handshake(cliente,servidor)
        print("")
clientes=[Cliente() for _ in range(3)]
multiple_client_handshake(clientes,servidor)
              
