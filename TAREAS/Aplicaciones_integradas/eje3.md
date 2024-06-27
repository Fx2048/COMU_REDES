Ejercicio 3: 
Sistema de mensajería completo con Amazon MQ

Descripción: Implementar un sistema de mensajería completo que soporte la publicación y 

suscripción de mensajes entre múltiples servicios.

Requisitos:

• Crea una clase MessageBroker para manejar la publicación y suscripción de mensajes.

• Implementa la capacidad de agregar y eliminar suscripciones.

• Simula la comunicación entre múltiples servicios utilizando threads para representar 
servicios concurrentes.

Código inicial:
`````
import threading
import time

class Message:
    def __init__(self, topic, content):
        self.topic = topic
        self.content = content
        self.timestamp = time.time()

class Topic:
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)

    def get_subscribers(self):
        return self.subscribers

class Subscriber:
    def __init__(self, name):
        self.name = name

    def notify(self, message):
        print(f"Subscriber {self.name} received message on topic '{message.topic}': {message.content}")

class Publisher:
    def __init__(self, broker):
        self.broker = broker

    def publish(self, topic_name, content):
        message = Message(topic_name, content)
        self.broker.publish_message(topic_name, message)

class Broker:
    def __init__(self):
        self.topics = {}

    def create_topic(self, topic_name):
        if topic_name not in self.topics:
            self.topics[topic_name] = Topic(topic_name)
        else:
            raise Exception(f"Topic '{topic_name}' already exists")

    def subscribe(self, topic_name, subscriber):
        if topic_name in self.topics:
            self.topics[topic_name].add_subscriber(subscriber)
        else:
            raise Exception(f"Topic '{topic_name}' does not exist")

    def unsubscribe(self, topic_name, subscriber):
        if topic_name in self.topics:
            self.topics[topic_name].remove_subscriber(subscriber)
        else:
            raise Exception(f"Topic '{topic_name}' does not exist")

    def publish_message(self, topic_name, message):
        if topic_name in self.topics:
            subscribers = self.topics[topic_name].get_subscribers()
            for subscriber in subscribers:
                threading.Thread(target=subscriber.notify, args=(message,)).start()
        else:
            raise Exception(f"Topic '{topic_name}' does not exist")

# Caso de uso
def main():
    broker = Broker()

    # Crear tópicos
    broker.create_topic("Sports")
    broker.create_topic("News")

    # Crear suscriptores
    subscriber1 = Subscriber("Hiato")
    subscriber2 = Subscriber("Diptongo")

    # Suscribir suscriptores a tópicos
    broker.subscribe("Sports", subscriber1)
    broker.subscribe("News", subscriber1)
    broker.subscribe("News", subscriber2)

    # Crear publicador
    publisher = Publisher(broker)

    # Publicar mensajes
    publisher.publish("Sports", "Encuentro de futbol hoy a las 5AM")
    publisher.publish("News", "Noticias de momento: Nuevas ofertas de productos")

if __name__ == "__main__":
    main()

`````

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/7076d4f4-1504-4bd9-ac81-bf95d3bb95d3)

