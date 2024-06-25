tabla_mac={}
def agregar_a_tabla_mac(direccion_mac,puerto):
    tabla_mac[direccion_mac]=puerto
    print(f"Direcin mac {direccion_mac} asocioada al puerto {puerto}")
def flooding(frame,puerto_origen,puertos):
    for puerto in puertos:
        if puerto !=puerto_origen:
            print(f"Enviando frame desde poeurto {puerto_origen} a {puerto}")

def recibir_frame(frame,puerto_origen,puertos):
    direccion_destino=frame['destino']
    if direccion_destino in tabla_mac:
       puerto_destino=tabla_mac[direccion_destino]
       print(f"Enviando frame a {puerto_destino} desde puerto {puerto_origen} a {puerto}")
    else:
        print("Direccion de destino desconocida, realizando flooding")
        flooding(frame,puerto_origen,puertos)
    direccion_origen=frame['origen']
    agregar_a_tabla_mac(direccion_origen,puerto_origen)
def demostracion():
    puertos=[1,2,3,4]
    frames=[
        {'origen': 'AA:BB:CC:DD:EE:FF', 'destino': 'FF:EE:DD:CC:BB:AA'},
        {'origen': 'BB:CC:DD:EE:FF:AA', 'destino': 'AA:BB:CC:DD:EE:FF'},
    ]
    for frame in frames:
        recibir_frame(frame,1,puertos)
        recibir_frame(frame,2,puertos)
if __name__=="__main__":
    demostracion()
import time
tabla_mac={}
def agregar_a_tabla_mac(direccion_mac,puerto,ttl=300):
    expiracion=time.time()+ttl
    tabla_mac[direccion_mac]=(puerto,expiracion)
    print(f"Direccion MAC {direccion_mac} asociada al puerto {puerto} con TTL de {ttl} segundos")
def verificar_expiracion():
    claves_a_eliminar=[k for k, v in tabla_mac.items() if time.time() >v[1]]
    for k in claves_a_eliminar:
        del tabla_mac[k]
        print (f" Entrada expirada para direcion mac {k} eliminada")
def recibir_frame(frame,puerto_origen):
    direccion_origen=frame['origen']
    agregar_a_tabla_mac(direccion_origen,puerto_origen)
    verificar_expiracion()
recibir_frame({'origen':'AA:BB:CC:DD:EE:FF'},1)
time.sleep(10)
recibir_frame({'origen':'BB:CC:DD:EE:FF:AA'},1)

