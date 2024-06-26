# LOAD BALANCING SIMULATION: 
## PREGUNTA:
 Simulación de balanceadores de carga
Objetivo: Simular la distribución de tráfico web utilizando balanceadores de carga.
Instrucciones:
• Implementa una clase LoadBalancer que distribuya las solicitudes entre varios servidores.
• Crea métodos para simular la configuración de un Application Load Balancer (ALB) y un
Network Load Balancer (NLB).
• Implementa una función que distribuya solicitudes HTTP y TCP entre los servidores
configurados.

# CÓDIGO
````
#definimos balanceador de carga desde el inicio:clase servidor para enlazar con funciones de LB:
class Servidor:
    """
    Recibe el nombre del servidor y maneja sus solicitudes

    """
    def __init__(self, nombre):
        self.nombre = nombre

    def manejar_solicitud(self, solicitud):
        print(f"Servidor {self.nombre} está manejando la solicitud {solicitud}")

class BalanceadorCarga:#Defino LB(Load Balancing)
    """
    Defino un diccionario de servidores y el tipo de LB:
    """
    def __init__(self, type):
        """
        type: "ALB" o "NLB"
        """
        self.servidores = []
        self.type = type

    def anadir_servidor(self, servidor): # AÑADO SERVIDORES:
        self.servidores.append(servidor)

    def distribuir_solicitudes_http(self, solicitudes):#dISTRIBUYO SOLICITUDES HTTP:
        if self.tipo == "ALB":
            print("Distribuyendo solicitudes HTTP usando ALB")
        else:# EN CASO NO FUNCIONE estrategia ALB, pasamos a la Estrategia standar
            print("Distribuyendo solicitudes HTTP usando estrategia estándar")
        
        for i, solicitud in enumerate(solicitudes):
            """
            Repartimos las solicitdes entre ls servidores:
            """
            servidor = self.servidores[i % len(self.servidores)]
            servidor.manejar_solicitud(solicitud)

    def distribuir_solicitudes_tcp(self, solicitudes):
        """
            Distribuimos solicitudes en tcp a cargo de NLB, en caso contrario, recurrios a standar operaciones
        """
        if self.tipo == "NLB":
            print("Distribuyendo solicitudes TCP usando NLB...")
        else:
            print("Distribuyendo solicitudes TCP usando estrategia estándar...")
        
        for i, solicitud in enumerate(solicitudes):
            servidor = self.servidores[i % len(self.servidores)]
            servidor.manejar_solicitud(solicitud)

# Ejemplo de uso
servidor1 = Servidor("Servidor 1")
servidor2 = Servidor("Servidor 2")

# Simular Application Load Balancer (ALB)
alb = BalanceadorCarga("ALB")
alb.anadir_servidor(servidor1)
alb.anadir_servidor(servidor2)
alb.distribuir_solicitudes_http(["Solicitud 1", "Solicitud 2", "Solicitud 3"])

# Simular Network Load Balancer (NLB)
nlb = BalanceadorCarga("NLB")
nlb.anadir_servidor(servidor1)
nlb.anadir_servidor(servidor2)
nlb.distribuir_solicitudes_tcp(["Solicitud TCP 1", "Solicitud TCP 2"])

````
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/fccce969-9c41-4d67-9130-e17c8714e33f)



