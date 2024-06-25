import random
def interference_probability(num_devices,collision_prob):
    p_transmit=1-(1-collision_prob)**num_devices
    prob_interference=p_transmit
num_devices=10
collision_prob=0.1
interference_prob=interference_probability(num_devices,collision_prob)
print("Probabilidad inteferencia ", interference_prob)


class Switch:
      def __init__(self,name):
          self.name=name
          self.vlans={}
          self.trunk=set()
      def configure_vlan(self,vlan_id,ports):
          self.vlans[vlan_id]=set(ports)
      def configure_trunk(self,other_switch):
          self.trunks.add(other_switch)
          other_switch.trunks.add(self)
      def send_message(self,vlan_id,message):
          for port in self.vlans.get(vlan_id,[]):
              print(f"Switch{self.name} sending message'{message}' on vlan {vlan_id} to port {port}")
          for trunk in self.trunks:
              print(f"Switch {self.name} sending message '{message}' on vlan {vlan_id} to trunk with {trunk.name}")
switch1=Switch("Switch1")
switch2=Switch("Switch2")
switch1.configure_vlan(10,[1,2,3])
switch1.configure_vlan(20,[4,5])

switch2.configure_vlan(10,[1,3])
switch2.configure_vlan(30,[2,4])
switch1.configure_trunk(switch2)
switch1.send_message(10,"Hello VLAN 10!")


