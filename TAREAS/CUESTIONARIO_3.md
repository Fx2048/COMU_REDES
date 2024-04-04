![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/c26c0fc0-ebf0-48a6-8315-bd767103b205)
Pregunta:

¿Qué dispositivo tiene el MAC de destino que se muestra?

El dispositivo con la dirección MAC de destino 00D0:BA8E:741A es el router

Responde las siguientes preguntas relacionadas con los datos capturados:

¿Se utilizaron diferentes tipos de cables / medios para conectar dispositivos?

Sí, tenemos 3 tipos, un medio inalámbrico, otro directo de cobre, y otro de fibra.

¿Los cables cambiaron el manejo de la PDU de alguna manera?

No, ya que solo los cables trabajan a nivel capa 1

¿El Hub perdió parte de la información que recibió?

No.

¿Qué hace el hub con las direcciones MAC y las direcciones IP?

El hub no hace nada,solo reenvia a todos sus puertos la trama o el paquete que se envía-

¿El punto de acceso inalámbrico hizo algo con la información que se le entregó?

Sí,este punto de acceso vuelve a empatqeutar la trama en una forma inalámcbrica para que viaje por el aire.

¿Se perdió alguna dirección MAC o IP durante la transferencia inalámbrica?

No.

¿Cuál fue la capa OSI más alta que utilizaron el hub y el punto de acceso?

El access point solo trabajan a nivel capa 1.

¿El hub o el punto de acceso reprodujeron en algún momento una PDU rechazada con una “X” de color rojo? Sí ya que al reenviar a todos los puertos, solo una es el destino, los demás rechaza ,porque no son el destino

Al examinar la ficha PDU Details (Detalles de PDU), ¿qué dirección MAC aparecía primero, la de origen o la de destino?

Aparece la de destino

¿Por qué las direcciones MAC aparecen en este orden?

Ya que si se conoce primero el destino, se enviará rapidamente

¿Había un patrón para el direccionamiento MAC en la simulación?

No

¿Los switches reprodujeron en algún momento una PDU rechazada con una “X” de color rojo?

No, ya que el swtich soloreenvia al destino que se requiera y no a todas las pcs

Cada vez que se enviaba la PDU entre las redes 10 y 172, había un punto donde las direcciones MAC cambiaban repentinamente. ¿Dónde ocurrió eso?

Sí, cambió en el router.

¿Qué dispositivo usa direcciones MAC que comienzan con 00D0: BA?

Era la del router

¿A qué dispositivos pertenecían las otras direcciones MAC?

.Petenecnía a direcciones emisores, receptores,que podía n ser acces point, switchers,

¿Las direcciones IPv4 de envío y recepción cambiaron los campos en alguna de las PDU?

No.

Cuando sigue la respuesta a un ping, a veces llamado pong, ¿ve el cambio de envío y recepción de direcciones IPv4?

Sí

¿Cuál es el patrón para el direccionamiento IPv4 utilizado en esta simulación?

Cada pueto debe manejar una direccion ip diferente, y cada sispositivo dentro de la red, debe no solaparse.

¿Por qué es necesario asignar diferentes redes IP a los diferentes puertos de un router?

Para interconectar dos redes.

Si esta simulación se configura con IPv6 en lugar de IPv4, ¿cuál sería la diferencia?

Todo sería igual,solo el formato donde se manejan las direcciones IP, ya que la IP V6 manejan una versión sexagesimal.
