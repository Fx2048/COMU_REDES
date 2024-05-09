#### Problema 13: Cálculo de interferencia de Canal
Conceptos: Co-channel Interference, CSMA/CA

Escribe una función que calcule la probabilidad de interferencia en un canal compartido, basada en el número de dispositivos activos y el método de acceso CSMA/CA para evitar colisiones.

- Implementa una función que evalúe la interferencia potencial en un entorno con múltiples dispositivos inalámbricos.



````

import random

def interference_probability(num_devices, collision_prob):
    """
    Calcula la probabilidad de interferencia en un canal compartido utilizando CSMA/CA.

    Args:
    - num_devices: Número total de dispositivos activos en el canal.
    - collision_prob: Probabilidad de colisión en el canal.

    Returns:
    - prob_interference: Probabilidad de interferencia en el canal.
    """
    # Calcula la probabilidad de que al menos un dispositivo transmita durante un tiempo determinado
    p_transmit = 1 - (1 - collision_prob) ** num_devices

    # Probabilidad de interferencia
    prob_interference = p_transmit

    return prob_interference

# Ejemplo de uso
num_devices = 10
collision_prob = 0.1
interference_prob = interference_probability(num_devices, collision_prob)
print("Probabilidad de interferencia:", interference_prob)


````

Supongamos que hay 20 dispositivos activos en un canal con una probabilidad de colisión de 0.05. ¿Cuál es la probabilidad de interferencia?

- ¿Cómo cambiaría la probabilidad de interferencia si el número de dispositivos activos aumenta a 30?
- ¿Qué pasaría con la probabilidad de interferencia si la probabilidad de colisión aumenta a 0.1?
- ¿Cómo afectaría una mayor distancia entre dispositivos a la probabilidad de interferencia?
- Escribe una función que genere un número aleatorio de dispositivos activos en un canal, y luego calcule y muestre la probabilidad de interferencia en el canal.
- Escribe una función que simule cómo cambia la probabilidad de interferencia a medida que la probabilidad de colisión varía en un rango específico.






#### Problema 22: Gestión de caché en un servidor DNS
Conceptos involucrados: Caching DNS name server, TTL, Expiration time, Refresh rate.

Desarrolla una función que simule un servidor DNS que utiliza caché para almacenar respuestas DNS. La caché debe expirar las entradas basadas en su TTL.

- Crea una función query_dns que consulte una caché antes de simular una consulta externa.
- Implementa una función update_cache para añadir o actualizar entradas en la caché, incluyendo manejo del TTL.
- Añade una función clean_expired_entries que limpie las entradas expiradas de la caché periódicamente

  
