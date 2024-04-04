![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/88e47c37-c083-4d41-ab5d-5a24ea21c336)
¿Cómo se llama esto? 

-Se llama un multiplizacion ,es transmitir diferentes datos por un mismo medio pero no simultaneamente, 

Aparece una variedad de PDU en la lista de eventos en el Panel de simulación. ¿Cuál es el significado de los diferentes colores? 
-Significa los protocolos que se usa en cada PDU 
¿Por qué tardó tanto en aparecer la PDU HTTP? 

 

Es debido que primero debe establecerse una conexión tcp entre cliente y servidor para que el tráfico pueda comenzar. 
¿Cómo se rotula la sección? Es TCP 

¿Se consideran confiables estas comunicaciones? Sí, el tcp es un protocolo confiable a diferenca del udp que no lo es. 

¿Qué indicadores TCP se establecen en esta PDU? 
Se establecen ACK y PSH donde tiene el (1)
Cierra el sobre de PDU y seleccione Inbound PDU Details.  

¿En qué cambiaron los números de puerto y de secuencia? Tanto el puerto de origen como el puerto de destino han cambiado de posición. Y el seq number sigue igual, y el flag están en la misma posición. Pero el ack ha cambiado(numero de reconocimiento) 
¿Qué información aparece ahora en la sección TCP? ¿En qué se diferencian los números de puerto y de secuencia con respecto a las dos PDU anteriores? 

Ahora se ha invertido el puerto de origen y de destino, y el ack ha aumentado a 234, el de seq number a 103, y el flag tiene los indicadores en ack y fin. 

¿Se consideran confiables estas comunicaciones 

Sí, se considera que son confiables. 

Registra los valores de SRC PORT (PUERTO DE ORIGEN), DEST PORT (PUERTO DE DESTINO), SEQUENCE NUM (NÚMERO DE SECUENCIA) y ACK NUM (NÚMERO DE RECONOCIMIENTO). 

El valor es de indicador  SYN

¿En qué cambiaron los números de puerto y de secuencia? 

Se diferencian en se ha invertido el puerto de destino y de origen, y ,también permanece el seq number y ,ha cambiado el ack number  y el flag de SYN, adicionó a ACK .

 ¿En qué se diferencian los números de puerto y secuencia de los resultados anteriores? 

-Se diferencian a los nros anteriores dado que ha cmbiado el número de puerto de origen, el puerto de destino,(invertidos) y el ack se mantuvo, y el seq number se cambió , y el flag se cambió su indicador a ACK.


¿Cuál es el mensaje del servidor? 

-El mensaje del servidor es WELCOME TO PT FTP SERVER

¿Qué es el protocolo de capa 4? 
El protocolo de capa 4 es udp ,  

¿Se consideran confiables estas comunicaciones? 

-No son confiables 


¿Por qué no hay números de secuencia y reconocimiento? 

Porque udp no necesita ser una conexi´n confiable, por eso no tiene todos los valores que tcp tiene .  




¿En qué cambiaron los números de puerto y de secuencia? 

-Se han invertido 

¿Cómo se llama la última sección de la PDU? 

-La ultima seccins e llama dns, , 

¿Cuál es la dirección IP para el nombre multiserver.pt.ptu? 

-192 .168. 1.254 


¿Qué protocolo de la capa de transporte utiliza el tráfico de correo electrónico? 

-TCP 

 ¿Se consideran confiables estas comunicaciones? 

-SI 

¿En qué cambiaron los números de puerto y de secuencia? 

-tTIENE UN ACK Y UN  SYN a diferencia del anterior, , se inviriteron los puertos y el ack nnumber cambió, el seq number permanece.



 ¿En qué se diferencian los números de puerto y de secuencia con respecto a los dos resultados anteriores? ¿En qué se diferencian los números de puerto y de secuencia con respecto a las dos PDU anteriores? 


Se ha invertido con respecto al anterior, los puertos, y el ack number se ha mantenido, y el seq number subió a 1, y e, flag cambió a ACK su indicador , y ya no tiene



SYN,Se ha mantenido el puerto de origen, pero cambió el flag quitandole el ACK 


¿Qué protocolo de correo electrónico se relaciona con el puerto TCP 25?  

-SMTP 

 

¿Qué protocolo se relaciona con el puerto TCP 110? 

-POP 3 
