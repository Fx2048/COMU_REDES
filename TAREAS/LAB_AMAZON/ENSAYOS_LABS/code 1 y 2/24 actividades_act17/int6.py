suscripciones_multicast={}
def suscribir_a_grupo(grupo,nodo):
    if grupo  not in suscripciones_multicast:
        suscripciones_multicast[grupo]=[]
    suscripciones_multicast[grupo].append(nodo)
def desuscribir_de_grupo(grupo,nodo):
    if grupo in suscripciones_multicast:
        suscripciones_multicast[grupo].remove(nodo)
        if not suscripciones_multicast[grupo]:
            del suscripciones_multicast[grupo]

def enviar_mensaje_multicast(grupo,mensaje):
    nodos=suscripciones_multicast.get(grupo,[])
    for nodo in nodos:
        nodo(mensaje)
        
def nodo_a(mensaje):
    print(f"nodo a recibio mensaje {mensaje}")
def nodo_b(mensaje):
    print(f"nodo b recibió mensajev {mensaje}")
def nodo_c(mensaje):
    print (f" nodo c recibió mensaje {mensaje}")
def demostracion():
    suscribir_a_grupo("grupo1",nodo_a)
    suscribir_a_grupo("grupo1",nodo_b)
    suscribir_a_grupo("grupo1",nodo_c)
    print("enviar mensaje al grupo 1")
    enviar_mensaje_multicast("Grupo1","hola grupo 1")
    print("enviar mensaje al grupo 2")
    enviar_mensaje_multicast("grupo 2","hola grupo2"
                             )


edenciales_nodos={'NodoA':{'token':'token_a','roles':['editor']},
                    'NodoB':{'token':'token_b','roles':['lector']},
                    'ndooc':{'token':'token_c','roles':['editor','administrador']
                                                        }}
                    
                             
def suscribir_a_grupo(grupo,nodo,token):
    credencial=credenciales_nodos.get(nodo)
    if credencial and credencial['token']==token and 'lector' in credencial["roles"]:
        if grupo not in suscripciones_multicast:
            suscripciones:multicast[grupo]=[]
        suscripciones_multicast[grupo].append(nodo)
    else:
        print(f"Acceso denegado para {nodo} en {grupo}")
def enviar_mensaje_multicas(grupo,mensaje,nodo):
    credencial=credenciales_nodos.get(nodo)
    if credencial and 'editor' in credencial['roles']:
        nodos =suscripciones_multicast.get(grupo,[])
        for n in nodos:
            n(mensaje)
    else:
        print(f"acceso denegado para publicar en {grupo} para {nodo}")
    

if __name__=="__main__":
   demostracion()

