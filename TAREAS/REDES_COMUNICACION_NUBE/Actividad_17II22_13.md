#### Problema 13: Cálculo de interferencia de Canal
Conceptos: Co-channel Interference, CSMA/CA

Escribe una función que calcule la probabilidad de interferencia en un canal compartido, basada en el número de dispositivos activos y el método de acceso CSMA/CA para evitar colisiones.

- Implementa una función que evalúe la interferencia potencial en un entorno con múltiples dispositivos inalámbricos.
1. Supongamos que hay 20 dispositivos activos en un canal con una probabilidad de colisión de 0.05. ¿Cuál es la probabilidad de interferencia?
2. ¿Cómo cambiaría la probabilidad de interferencia si el número de dispositivos activos aumenta a 30?
3. - ¿Qué pasaría con la probabilidad de interferencia si la probabilidad de colisión aumenta a 0.1?
-4. ¿Cómo afectaría una mayor distancia entre dispositivos a la probabilidad de interferencia?
-5. Escribe una función que genere un número aleatorio de dispositivos activos en un canal, y luego calcule y muestre la probabilidad de interferencia en el canal.
-6. Escribe una función que simule cómo cambia la probabilidad de interferencia a medida que la probabilidad de colisión varía en un rango específico.


````
```python
# Problema 13: Cálculo de interferencia de Canal

def calcular_probabilidad_interferencia(num_dispositivos):
    """
    Calculoe la probabilidad de interferencia en un canal compartido utilizando CSMA/CA.

    Args:
    - num_dispositivos: Número total de dispositivos activos en el canal.
    
    Returns:
    - prob_interferencia: Probabilidad de interferencia en el canal.
    """
    # Probabilidad base de interferencia con un solo dispositivo
    probabilidad_base = 0.1
    # Asumiendo que cada dispositivo adicional añade la misma probabilidad base
    probabilidad_interferencia = 1 - (1 - probabilidad_base) ** num_dispositivos
    return probabilidad_interferencia

# Ejemplo de uso
num_dispositivos = 20
probabilidad_colision = 0.05
probabilidad_interferencia = calcular_probabilidad_interferencia(num_dispositivos)
print(f"La probabilidad de interferencia con {num_dispositivos} dispositivos es: {probabilidad_interferencia:.4f}")




````

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/7a71ca99-ff65-47da-9ec8-64598c1bea4f)









#### Problema 22: Gestión de caché en un servidor DNS
Conceptos involucrados: Caching DNS name server, TTL, Expiration time, Refresh rate.

Desarrolla una función que simule un servidor DNS que utiliza caché para almacenar respuestas DNS. La caché debe expirar las entradas basadas en su TTL.

- Crea una función query_dns que consulte una caché antes de simular una consulta externa.
- Implementa una función update_cache para añadir o actualizar entradas en la caché, incluyendo manejo del TTL.
- Añade una función clean_expired_entries que limpie las entradas expiradas de la caché periódicamente

  - Modifica las funciones update_cache y query_dns para soportar diferentes tipos de registros DNS. Asegúrate de que tu caché pueda almacenar múltiples tipos de registros para un mismo dominio y que la función query_dns busque correctamente según el tipo de registro solicitado.

- Implementa una función external_dns_query que simule de manera más realista una consulta DNS externa. Por ejemplo, podría seleccionar de un conjunto predefinido de respuestas basadas en el dominio y el tipo de registro.

- Implementa una manera de que esta función se ejecute automáticamente en intervalos regulares. Considera el uso de threading o programación asíncrona para manejar esta tarea en el fondo sin bloquear las consultas principales.
