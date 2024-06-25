cache_de_red={}
def obtener_datos_desde_cache(identificador):
    if identificador in cache_de_red:
        print(f"Datos obtenidos desde cache 'para {identificador}")
        return cache_de_red[identitificador]
    else:
        print(f"No se encontraron datos en cache para {identificador}")
        return None

    
def obtener_datos_desde_servidor(identificador):
    print(f"obteninddo datos desde servidor para {identificador}")
    datos=f"Datos para {identificador}"
    cache_de_red[identificador]=datos
    return datos
def obtener_datos(identificador):
    datos=obtener_datos_desde_cache(identificador)
    if datos is None:
       datos=obtener_datos_desde_servidor(identificador)
    return datos
def demostrar_eficiencia():
    print(obtener_datos("12345"))
    print(obtener_datos("12345"))
    print(obtener_datos("12345"))
if __name__=="__main__":
   demostrar_eficiencia()
import time
cache_de_red={}
def almacenar_en_cache(identificador,datos,ttl=300):
    expiracion=time.time()+ttl
    cache_de_red[identificador]=(datos,expiracion)
def obtener_datos_desde_Cache(identificador):
    if identificador in cache_de_red:
        if time.time()<expiracion:
            print(f"Datos en caché desde cache para {identificador}")
            return datos
        else:
            print(f"Datos expirados para {identificador}")
            del cache_de_red[identificador]
    return None

class NodoCache:
      def __init__(self):
          self.cache={}
      def almacenar(self,clave,valor):
          self.cache[clave]=valor
      def recuperar(self,clave):
          return self.cache.get(clave)
nodos=[NodoCache() for _ in range (3)]
def hash_clave(clave):
    return hash(clave) %len(nodos)
def almacenar_en_cache(clave,valor):
    nodo_idx= hash_clave(clave)
    nodos[nodo_idx].almacenar(clave,valor)
def recuperar_de_cache(clave):
    nodo_idx=hash_clave(clave)
    return nodos[nodo_idx].recuperar(clave)

