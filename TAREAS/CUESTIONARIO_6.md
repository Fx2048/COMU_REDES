![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/6203546a-8aa7-4e7c-a041-1d446e93db4d)

[Actividad 6 - pdf](https://github.com/Fx2048/COMU_REDES/blob/main/TAREAS/ACTIVIDADES_PDF/Actividad6-C8280.pdf)

¿Por qué los pings no fueron correctos? 


En el caso no han sdo correctos porque la maquina no ha aprendido la direccion IP  o no están conectados. 
En una ventana con el símbolo del sistema en la PC-A, haga ping a la PC-B. 


Nota: Si los pings no son correctos, es posible que debas desactivar el Firewall.

Pregunta: 

¿Fueron correctos los pings? Explia. 

No fueron correctos los pings, no hay respuesta porque el router lleva el tráfico en sus dos raíces, Giga Ethernet 0 , y gigaeternet 1, porque la configuracion no ha sido configurada del todo. 

Utiliza el comando show ip route en R1 para responder las preguntas siguientes. 

 

¿Qué código se utiliza en la tabla de enrutamiento para indicar una red conectada directamente? 
-Se usa el código loca,,conetd, static, rip and mobile bgm

¿Cuántas entradas de ruta están codificadas con un código C en la tabla de enrutamiento? 

Entradas son las de tipo C –
¿Qué tipos de interfaces están asociadas a las rutas con código C? 

-gigaethernet 000, y 001 
¿Qué tipos de interfaces están asociadas a las rutas con código C? 

-gigaethernet 000, y 001 
¿Cuál es el estado operativo de la interfaz G0/0/1? 

-conectado de momento 

¿Cuál es la dirección de control de acceso a los medios (MAC) de la interfaz G0/0/1? 
¿Cómo se muestra la dirección de Internet en este comando? 
Preguntas 

Si la interfaz G0/0/1 se mostrará administratively down, ¿qué comando de configuración de interfaz usaría para activar la interfaz? 

-La configuración de las interfaces se realiza desde submodo de configuración de interfaces, tecleamos interface estando en modo de configuracion global y cambiaria a  config if, y alli cambiamos al  comando no shut o not shutdown , porque este se habilita para cambiar interfaces, si ejecutamos, la interface debe activarse, 

¿Qué ocurriría si hubiera configurado incorrectamente la interfaz G0/0/1 en el router con una dirección IP 192.168.1.2? 

-La PCA no podría hacer pin a PCB esto se debe a que la pcb está en una red diferente a la de PCA que requiere del router del waterwall determinado para dirigir estos paquetes , la PCA está configurada para dirigir estos paquetes y utilizar solamente la dirección IP 162 .168 .1.1 , para el ruoter del waterwall predeterminado pero esta dirección noe sta asignada a ningún dsipositivo en la LAN, asi que cualquier paquete que vaya  a ser enviado para su enrutamiento nunca llegará al destino. 
