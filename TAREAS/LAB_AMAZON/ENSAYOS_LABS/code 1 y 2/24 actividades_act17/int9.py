import random
class ARPARouter:
      def __init__(self,name):
          self.name=name
          self.neighbors=[]
      def add_neighbor(self,neighbor):
              self.neighbors.append(neighbor)
      def route_message(self,message):
          if self.neighbors:
             neighbor= random.choice(self.neighbors)
             print(f" Mensaje enviado desde {self.name} a {neighbor.name}:{message}")
             neighbor.receive_message(message)
          else:
             print(f"No hay vecios disponibles para {self.name}. mensaje perdido")
      def receive_message(self,message):
          print(f"mesnaje recibido en {self.name}: {message}")
def simulate_ARPANET(nodes, num_messages):
    print("Inciiando simulacion en arpanet")
    for i in range (num_messages):
        sender=random.choice(nodes)
        message=f"Mensaje{i+1}"
        sender.route_message(message)
        print()
node_A=ARPARouter("Node A")
node_B=ARPARouter("Node B")
node_C=ARPARouter("Node C")
node_A.add_neighbor(node_B)
node_B.add_neighbor(node_A)
node_B.add_neighbor(node_C)
node_C.add_neighbor(node_B)
nodes=[node_A, node_B, node_C]
simulate_ARPANET(nodes,5)
              
                    
