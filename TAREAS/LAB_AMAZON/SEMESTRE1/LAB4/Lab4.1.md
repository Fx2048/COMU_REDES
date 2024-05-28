![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/b5faff18-7042-4bde-a6db-e6cd1aa5d8e5)

# EC2 simulation on the laboratory experience



# Lab 4 :Laboratorio 1 del módulo 4: Lanzamiento de una instancia de EC2Instructions
 Acceso a la consola de administración de AWS

Tarea 1. Comenzar a crear la instancia y asignarle un nombre

Selecciona el menú Servicios, localiza los servicios de Computación y selecciona EC2.

 

1. Selecciona el botón Lanzar instancia en medio de la página y luego selecciona Lanzar instancia en el menú desplegable.
Pon un nombre a la instancia: Web Server 1

# Tarea 2. Imágenes de aplicación y SO

Selecciona una AMI:Amazon Linux 2023,

#Tarea 3 Elegir el tipo de instancia

Tipo de instancia:t2.micro---Tipos de recursos asignados a la instancia

# Tarea 4 Seleccionar un par de claves

Menú : nombre de par de claves: vockey(conexión  a instancia por SSH)

# Tarea 5. Configuración de red


Editar en configuración de red

ajusted predeterminados en VPC, y subred, 

Manten ajuste de Asignar automáticamente la IP pública como habilitar

En firewall ,selecciona Crear grupo de seguridad,  y configura el grupo de seguridad

Manten Crear un nuevo grupo de seguridad, 

En nombre introduce Web Server

Description: Security for my server

Eliminar la regla de entrada SSH predeterminada

# Tarea 6. Configurar el almacenamiento

Confirugrar alamacenamiento configuracion predetemrinada, (volumen de arranque)

# Tarea 7: Detalles avanzados
En detallles avanzados de datos de usuario: Programa:
#!/bin/bash
yum update -y
yum -y install httpd
systemctl enable httpd
systemctl start httpd
echo '<html><h1>Hello World!</h1></html>' > /var/www/html/index.html

# Tarea 8: Revisar la instancia y lanzarla

En resumen, lanza la instancia

y visualiza un mensaje de éxito
 
En ver todas las instancias, arrancará la instancia, y selecciona Web Server 1, y revisa a detalles de la parte inferior,actualiza la instancia, y ...

# Tarea 9. Acceder a la instancia de EC2
En detalles copia el valor de DIrección IPV4 pública y visualiza en navegador, Ow no! La página no se carga porque debes primero, actualizar el grupo de seguridad!

Así que , 

# Tarea 10 Actualizar el grupo de seguridad
Ve a consola de administración de EC2, 
Revisa la consola de administración de Ec2, 
Ve a Red y seguridad, y selecciona grupos de seguridad, accede a  Web Server de tu instancia EC2,  y click en Reglas de Entrada

# Tarea 11: Crear una regla de entrada

Selecciona Editar reglas de entradas  y Añade una regla 
Configura lo siguiente:

Tipo: HTTP
Fuente: Cualquier lugar-IPv4
Selecciona Guardar reglas
La nueva regla HTTP de entrada crea una entrada para las direcciones IP IPv4 IP (0.0.0.0/0) y IPv6 (::/0).

 # Tarea 12. Probar la regla
Actualiza la página que contenía al IP direction Public
y dice Hello World!



![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/5aebe8df-c23d-4562-9b16-fc44c268bcdd)

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/9bc4ff76-aec6-4d4e-b817-91fe94befe9a)

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/f07b5f1d-fb91-4363-badb-50ce4e962bc5)

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/4e29ab09-7e50-4d74-b7b4-dbe29b0a4d73)

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/27a8d043-408d-40c1-b853-87a79473d903)

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/33111535-1146-481b-9738-01e1d9d6c677)


![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/f6cad6d0-1112-4618-bf5b-3b0f23900da0)

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/a915c000-b486-4c29-bb45-635d71a63b73)
