import time
print("")
arp_table={
    '192.168.1.1':'00:1A:2B:3C:4D:5E',
    '192.168.1.2':'00:1A:2B:3C:4D:5F',
    '192.168.1.3':'00:1A:2B:3C:4D:60',
}
def print_arp_table():
    print("Tabla ARP")
    for ip,mac in arp_table.items():
        print(f"IP:{ip} -> MAC:{mac}")
    print()
def arp_lookup(ip):
    mac=arp_table.get(ip)
    if mac:
        print(f"Direccion mac para {ip} es {mac}")
    else:
        print(f"Solicitando ARP para {ip}...")
        simulate_arp_request(ip)
def simulate_arp_request(ip):
    print(f"Enviando solicitud ARP para {ip}...")
    mac =f"00:1A:2B:3C:4D:{ip.split('.')[-1].zfill(2)}"
    print(f"Respuesta ARP recibida:{ip} -> {mac}")
    arp_table[ip]=mac
    print_arp_table()
def add_arp_entry(ip,mac):
    print(f"Agregando entrada ARP:{ip} -> {mac}")
    arp_table[ip]=mac
    print_arp_table()
def remove_arp_entry(ip):
    if ip in arp_table:
        print (f"eliminando entrada ARO para {ip}")
        del arp_table[ip]
        print_arp_table()
    else:
        print(f"No se encontró una entrada ARP para {ip}")
def age_arp_entries():
    print("Envejeciendo entradas ARP...")
    arp_table.clear()
    print_arp_table()
if __name__=="__main__":
    print_arp_table()
    arp_lookup('192.168.1.1')
    arp_lookup('192.168.1.4')
    add_arp_entry('192.168.1.5','00:1A:2B:3C:4D:61')
    remove_arp_entry('192.168.1.2')
    time.sleep(2)
    age_arp_entries()
    arp_lookup('192.168.1.3')
    arp_lookup('192.168.1.5')
    

