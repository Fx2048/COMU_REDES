Ejercicio 3: Sistema de mensajería completo con Amazon MQ
Descripción: Implementar un sistema de mensajería completo que soporte la publicación y 
suscripción de mensajes entre múltiples servicios.
Requisitos:
• Crea una clase MessageBroker para manejar la publicación y suscripción de mensajes.
• Implementa la capacidad de agregar y eliminar suscripciones.
• Simula la comunicación entre múltiples servicios utilizando threads para representar 
servicios concurrentes.
Código inicial:
import threading
class MessageBroker:
 def __init__(self):
 self.topics = {}
 def create_topic(self, name):
 self.topics[name] = []
 return name
 def subscribe(self, topic, endpoint):
 if topic in self.topics:
 self.topics[topic].append(endpoint)
 else:
 raise Exception("Topic does not exist")
 def unsubscribe(self, topic, endpoint):
 if topic in self.topics:
 self.topics[topic].remove(endpoint)
 else:
 raise Exception("Topic does not exist")
 def publish(self, topic, message):
 if topic in self.topics:
 for endpoint in self.topics[topic]:
 threading.Thread(target=endpoint.notify, args=(message,)).start()

 else:
 raise Exception("Topic does not exist")
class Endpoint:
 def __init__(self, name):
 self.name = name
 def notify(self, message):
 print(f"Message to {self.name}: {message}")
# Implementación adicional requerida...
