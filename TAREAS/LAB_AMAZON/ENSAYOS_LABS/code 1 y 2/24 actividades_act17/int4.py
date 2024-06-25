Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Client(self, id, nombre):
    def enviar_syn(self, funciones, contexto):
        return client.enviar_syn= "Enviado"
    
SyntaxError: invalid syntax

= RESTART: C:/Users/PROPIETARIO/Desktop/Comu/24 actividades_act17/intento1.py
Traceback (most recent call last):
  File "C:/Users/PROPIETARIO/Desktop/Comu/24 actividades_act17/intento1.py", line 1, in <module>
    class Client(self, id, nombre):
NameError: name 'self' is not defined

= RESTART: C:/Users/PROPIETARIO/Desktop/Comu/24 actividades_act17/intento1.py
Traceback (most recent call last):
  File "C:/Users/PROPIETARIO/Desktop/Comu/24 actividades_act17/intento1.py", line 15, in <module>
    datos_eviados,checksum=enviar_datos("holamudno",metodo='checksum')
  File "C:/Users/PROPIETARIO/Desktop/Comu/24 actividades_act17/intento1.py", line 9, in enviar_datos
    checksum=calcular_checksum_simple(datos)
NameError: name 'calcular_checksum_simple' is not defined. Did you mean: 'calcular_checksum_sumple'?
>>> 
= RESTART: C:/Users/PROPIETARIO/Desktop/Comu/24 actividades_act17/intento1.py
mensaje cifrado l
Mensaje descifrado h
>>> def capa_aplicacion(datos):
...     datos_encapsulados=f"APLICACION({datos})"
...     print("Aplicacion envía",datos_encapsulados)
...     return capa_presentacion(datos_encapsulados)
... def capa_presentacion(datos):
...     
SyntaxError: invalid syntax
>>> 
= RESTART: C:/Users/PROPIETARIO/Desktop/Comu/24 actividades_act17/intento3.py
>>> 
= RESTART: C:/Users/PROPIETARIO/Desktop/Comu/24 actividades_act17/intento3.py
mensaje original Hola mundo
Aplicacion envía APLICACION(Hola mundo)
Traceback (most recent call last):
  File "C:/Users/PROPIETARIO/Desktop/Comu/24 actividades_act17/intento3.py", line 51, in <module>
    demostracion()
  File "C:/Users/PROPIETARIO/Desktop/Comu/24 actividades_act17/intento3.py", line 46, in demostracion
    datos_encapsulados=capa_aplicacion(mensaje_original)
  File "C:/Users/PROPIETARIO/Desktop/Comu/24 actividades_act17/intento3.py", line 4, in capa_aplicacion
    return capa_presentacion(datos_encapsulados)
  File "C:/Users/PROPIETARIO/Desktop/Comu/24 actividades_act17/intento3.py", line 7, in capa_presentacion
    print("presentacion envia:",datos_encapsualdos)
NameError: name 'datos_encapsualdos' is not defined. Did you mean: 'datos_encapsulados'?
