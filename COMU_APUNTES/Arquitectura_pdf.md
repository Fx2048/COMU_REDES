# Para comprender y trabajar con APIsRESTful
## 1. Protocolo HTTP- Protocolo de Transferencia de Hipertexto (HTTP)
* base de pirestful
*  define métodos cruciales para Restful(
## Métodos HTTP
* get, recuperar
* post crear
* put actualizar
* delete eliminar
## 3. Códigos de Estado HTTP
* Maneja respuestas cliente , y detecta problemas de servidor
## 4.Modelo Cliente servidor
* Describe como dispositivos o programas interactuan en la red con clientes que hacen solicitudes a servidores que les responden
* Este modelo es central en el diseño APIRESTFUL, porque es dependiente de él.
## 5. TCP/IP:
Es el conjunto de protocolos 
 intercambiar datos
 robustez, eficiencia, seguridad.
 ## 6. DNS(SISTEMA DE NOMBRES DE DOMINIOS)
 DNS traduce dominios(de url) name to IP directions
## 7. Seguridad de red
Encripta datos, 0Auth, JWt(Json web tokens) en su viaje, solo los usuarios autorizados pueden verlo.
## Arquitectura

## Caching y Gestión de Estado


[...]

¿Cuál es la diferencia principal entre una API REST y una API RESTful?
La principal diferencia entre una API REST y una API RESTful es que una API RESTful sigue estrictamente todos los principios y restricciones de la arquitectura REST, mientras que una API REST solo sigue algunos de esos principios, pero no necesariamente todos.

Explica las seis restricciones arquitectónicas que debe cumplir una interfaz para ser considerada RESTful.
Las seis restricciones arquitectónicas que debe cumplir una interfaz para ser considerada RESTful son: cliente-servidor, sin estado, cache, sistema de capas, código bajo demanda (opcional) e interfaz uniforme.

¿Cuál es el propósito de utilizar una interfaz uniforme en las API RESTful?
El propósito de utilizar una interfaz uniforme en las API RESTful es identificar recursos individuales mediante URLs y utilizar métodos HTTP estándar (GET, POST, PUT, DELETE, etc.) para indicar la operación a realizar sobre esos recursos.

¿Qué tipos de solicitudes HTTP se utilizan comúnmente en las API RESTful y cuál es su función?
Los tipos de solicitudes HTTP comúnmente utilizados en API RESTful son: GET (obtener datos), POST (crear un nuevo recurso), PUT (actualizar un recurso existente), PATCH (actualizar parcialmente un recurso), DELETE (eliminar un recurso).

Explica la diferencia entre una API RESTful basada en HTTP y una API basada en HTTP que no es RESTful.
Una API RESTful basada en HTTP utiliza los diferentes verbos HTTP (GET, POST, PUT, etc.) para indicar el tipo de operación, mientras que una API basada en HTTP que no es RESTful podría usar el mismo verbo (generalmente POST) para todas las operaciones. Además, las API RESTful acceden a recursos individuales mediante URLs únicas.

¿Qué son las API de red y cuáles son sus características principales?
Las API de red son interfaces que permiten la interacción entre software y recursos de red como routers, switches, firewalls, etc. Sus características principales son manipulación de configuración, monitoreo, automatización de tareas e integración con otros sistemas.

Describe los dos tipos de API de red según el modelo de programación (RESTful y SOAP).
Según el modelo de programación, las API de red pueden ser RESTful (utilizan HTTP) o SOAP (más formales y rigurosas). Las RESTful son más simples e integradas con aplicaciones web, mientras que SOAP son adecuadas para entornos que requieren alta consistencia y fiabilidad.

Explica la diferencia entre las API síncronas y asíncronas en el contexto de las API de red.
Las API síncronas requieren que el cliente espere una respuesta inmediata del servidor después de enviar una solicitud. Las asíncronas permiten que el cliente continúe con otras operaciones sin esperar la respuesta, útil para operaciones de larga duración.

¿Por qué son importantes las API de red en la automatización y orquestación de la infraestructura de red?
Las API de red son importantes para la automatización y orquestación porque permiten configurar y controlar dispositivos de red de forma programática, reduciendo errores humanos y mejorando la eficiencia operativa.

¿Cómo contribuyen las API de red a la flexibilidad, escalabilidad e innovación en los sistemas de red?
Las API de red contribuyen a la flexibilidad y escalabilidad al permitir ajustar rápidamente la infraestructura de red según las demandas. También fomentan la innovación al habilitar áreas como IA para operaciones de red, análisis de datos avanzado y mejoras en seguridad. Finalmente, facilitan la integración de redes con aplicaciones empresariales.

