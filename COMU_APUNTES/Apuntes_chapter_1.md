1. Internet se implementa utilizando TCP/IP (Protocolo de Control de Transmisión/Protocolo de Internet) en lugar del modelo OSI (Interconexión de Sistemas Abiertos) por varias razones:


- TCP/IP se desarrolló antes y ganó adopción generalizada antes de que se estandarizara el modelo OSI.
- TCP/IP es más flexible y permite el desarrollo e implementación independiente de diferentes capas, mientras que el modelo OSI es un diseño más rígido y monolítico.
- TCP/IP es más simple y fácil de implementar, lo que lo hace más práctico para aplicaciones de redes del mundo real.
- TCP/IP se diseñó con un enfoque en la interconexión y la conexión de diferentes tipos de redes, que era un requisito clave para Internet.

2. SMTP (Protocolo Simple de Transferencia de Correo), POP (Protocolo de Oficina de Correos) e IMAP (Protocolo de Acceso a Mensajes de Internet) son protocolos utilizados para la comunicación por correo electrónico.

- SMTP se utiliza para enviar y transferir mensajes de correo electrónico entre servidores.
- POP es utilizado por los clientes de correo electrónico para recuperar mensajes de correo electrónico de un servidor de correo.
- IMAP también es utilizado por los clientes de correo electrónico, pero permite características más avanzadas como acceder y administrar correos electrónicos en el servidor mismo.

Los clientes de correo electrónico suelen utilizar una combinación de estos protocolos. Por ejemplo, pueden utilizar SMTP para enviar correos electrónicos y POP o IMAP para recibir y administrar correos electrónicos.

3. En TCP (Protocolo de Control de Transmisión), los siguientes paquetes desempeñan roles importantes en el establecimiento, mantenimiento y terminación de conexiones:

- Paquete SYN (Sincronizar): Inicia una nueva solicitud de conexión.
- Paquete SYN-ACK (Sincronizar-Reconocer): Respuesta del receptor, reconociendo la solicitud de conexión.
- Paquete ACK (Reconocer): Enviado por el iniciador para confirmar el establecimiento de la conexión.
- Paquete FIN (Finalizar): Enviado por cualquiera de los extremos para iniciar la terminación de una conexión.
- Paquete FIN-ACK (Finalizar-Reconocer): Respuesta al paquete FIN, reconociendo la solicitud de terminación.

4. La multiplexación se refiere a la capacidad de transmitir múltiples flujos de datos a través de un solo canal o recurso de comunicación. En el contexto de la capa de transporte TCP/IP, la multiplexación permite que múltiples aplicaciones en un solo host utilicen la misma conexión de red subyacente simultáneamente.

Por ejemplo, en una sola computadora, múltiples aplicaciones (por ejemplo, navegador web, cliente de correo electrónico, cliente de transferencia de archivos) pueden establecer conexiones TCP separadas con diferentes hosts remotos, aunque todas comparten la misma interfaz de red física y dirección IP. Esto se logra a través de la multiplexación de puertos, donde a cada aplicación se le asigna un número de puerto único, permitiendo que la capa de transporte distinga y enrute los flujos de datos de manera apropiada.

5. Varias razones contribuyen al agotamiento de las direcciones IPv4:

- Espacio de direcciones limitado: IPv4 utiliza direcciones de 32 bits, proporcionando solo alrededor de 4.3 mil millones de direcciones únicas, lo cual es insuficiente para el creciente número de dispositivos y usuarios que se conectan a Internet.
- Asignación ineficiente: Las direcciones IPv4 se asignaron inicialmente en grandes bloques, lo que llevó al desperdicio y a la distribución desigual.
- Crecimiento de Internet: El rápido crecimiento de Internet, especialmente con la proliferación de dispositivos móviles y el Internet de las Cosas (IoT), ha acelerado la disminución de las direcciones IPv4 disponibles.
- Falta de incentivos para el uso eficiente: En los primeros días de Internet, no había incentivos ni mecanismos para fomentar el uso eficiente de las direcciones IPv4.

6. La afirmación "IPv4 e IPv6 no son interoperables" significa que los dispositivos que utilizan IPv4 y los dispositivos que utilizan IPv6 no pueden comunicarse directamente entre sí de forma nativa. Esto se debe a que las dos versiones del protocolo tienen diferentes estructuras de paquetes y esquemas de direccionamiento.

Para habilitar la comunicación entre las redes IPv4 e IPv6, se requieren varios mecanismos de transición y técnicas de traducción, tales como:

- Implementación de doble pila: Dispositivos y routers capaces de soportar simultáneamente IPv4 e IPv6.
- Traducción de direcciones de red (NAT64): Traduce entre direcciones IPv6 e IPv4, permitiendo que los clientes solo IPv6 se comuniquen con servidores IPv4.
- Tunelización: Encapsulación de paquetes IPv6 dentro de paquetes IPv4 (o viceversa) para atravesar redes que no soportan la otra versión del protocolo.

La carga de habilitar la interoperabilidad recae principalmente en los dispositivos y routers que pueden soportar tanto IPv4 como IPv6 (doble pila). Estos dispositivos son responsables de traducir o tunelizar entre las dos versiones del protocolo para facilitar la comunicación entre dispositivos o redes solo IPv4 y solo IPv6.

7. Cuando tienes una dirección IP estática para un dispositivo y planeas cambiarla, necesitas actualizar el(los) servidor(es) de nombres DNS (Sistema de Nombres de Dominio) autoritativo(s) de tu organización por la siguiente razón:

El DNS es responsable de mapear los nombres de dominio a las direcciones IP. Si cambias la dirección IP de un dispositivo sin actualizar el registro DNS correspondiente, el nombre de dominio seguirá apuntando a la antigua dirección IP, lo que provocará problemas de conectividad. Al actualizar el(los) servidor(es) DNS autoritativo(s), te aseguras de que la nueva dirección IP esté asociada con el nombre de dominio, permitiendo a los clientes resolver la dirección IP correcta al acceder al dispositivo o servicio.

8. En un escenario de NAT (Traducción de Direcciones de Red), donde una organización utiliza direcciones IP privadas internamente y las traduce a una dirección IP pública para la comunicación a través de Internet, los checksums pueden volverse incorrectos al pasar de la red interna a Internet debido al proceso de traducción de direcciones.

Los checksums se calculan en base a las direcciones IP y otros campos en el encabezado del paquete. Cuando NAT traduce la dirección IP privada a una dirección IP pública, modifica el encabezado del paquete, haciendo que el checksum se vuelva inválido. Los dispositivos o routers NAT necesitan recalcular el checksum para asegurar la integridad de los datos después de la traducción de direcciones.

9. En NAT de uno a muchos (también conocido como PAT o Traducción de Direcciones de Puerto), donde múltiples dispositivos internos se mapean a una sola dirección IP pública, la tabla de traducción de direcciones necesita almacenar la siguiente información:

- Dirección IP privada interna: La dirección IP privada del dispositivo en la red interna.
- Número de puerto interno: El número de puerto utilizado por la aplicación o servicio en el dispositivo interno.
- Dirección IP pública externa: La única dirección IP pública utilizada para la traducción.
- Número de puerto externo: El número de puerto único asignado por el dispositivo NAT para identificar el dispositivo interno y la aplicación específicos.

Esta información es necesaria para que el dispositivo NAT pueda enrutar correctamente el tráfico entrante y saliente entre los dispositivos internos y la red externa, asegurando que los paquetes se envíen y se reciban del dispositivo y la aplicación internos correctos.
