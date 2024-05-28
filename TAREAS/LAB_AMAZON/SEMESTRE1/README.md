# Resumen de cada módulo:
# Módulo 1: Infraestructura Global
1. Informática en la nube

 PAAS, PLataform for code and apps

SAAS -Software,apps, WEBS

IAAS,infraestructura física o virtual que almacena datos

# Módulo 2: Estructura de la nube:

Zona de disponibilidad DataCenter Almacena servidores

Región área Almacena datos

Latencia retardo de envio y llegada de mensaje

Ubicación de borde -reduce latencia almacenando datos

Volumen de tráfico-gra mayor latencia

Región > zona de disponibilidad > ubicación de borde

## Caso :Uso de código 

````
import boto3
s3=boto3.cllient('s3',region_name='us-west-2')
bucket_name='nombre de bucket'
archivo_local='ruta/al/archivo/local.pdf'
archivo_remoto='archivo-pacientes/registro1.pdf'
s3.upload_file(archivo_local,bucket_name,archivo_remoto)
CREATE TABLE registros_medicos(
    id INT PRIMARY KEY,
    paciente VARCHAR(100),
    diagnostico TEXT
);
INSERT INTO registros_medicos (id, paciente, diagnostico)
VALUES(1,'Juan Perez', 'Gripe común');
from twilio.rest import Client
account_sid='su_account-sid'
autoh_token='su-auth-token'
client=Client(account_sid,auth_token)
mensaje='Su cita está confirmada para mañana a las 10 AM.'
destinatario='51983073205'
message=client.messages.create(
    body=mensaje,
    from_='+123456789',
    to=destinatario
)
````

Coste de AWS: Economía

Disponibilidad de los servicios: Disponibilidad

Velocidad o latencia: Rapidez

Resiliencia de los componentes de AWS: Robustez

Derechos de datos: Privacidad

Audiencia: Usuarios

# Mo´dulo 3: Consola de AWS:

RESSHIFT-EMPRESARIAL-SEARCH- big data

lambda ejecuta codigo sin servidor

cloud trail vigila users monitorea y registra

iam -verifica acceso autorizado personal

ec2= almacenamiento escalable
ebs (hermanito menor de ec2 y S3,, solo se adjunta a ec2, mentras ec2 varios pueden entrar a s3 bucket-para instancias c2 especificas 

s3 pro, lento en vez de ebs, sericio almacena datos

almacenamiento de datos

dynamo=no relacionales-clave-valor-flexible-publicidad,videojuegos

cloud watch supervisa apps y servidores-notifica de uso segun presupuesto

virtual private cloud , cuenta personal

RDS relationals = relacionales, big data, y sql.alumnos

# Módulo 4
ec2 -escalable

cs3- almace data users

bucket  contenedor de objetos multimedia

vpc nube privada virtual vpc

route 53 dns web service

vpc cloud private account

notacio objetosJavascript  json  - 

sitio web dinámico interactua con user:python, php, asp

sitio web statico no cambia en user interactions:html, css

nombre de dominio etiqueta de red de compus bajo central poder

politica:permisos enn json language solicitados por user y procesados por aws

dns sistemas de nomenclatura para disposiivos conectaods  a red

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
# 4.2 Laboratorio 2 del módulo 4: Creación de un bucket de S3
Crear un Bucket de S3:
Ve a la consola de administración de AWS y selecciona el servicio S3.
Haz clic en “Crear bucket”.
Introduce un nombre único para el bucket (siguiendo las pautas de nomenclatura).
Elige una región para el bucket.
Quita la marca de “Bloquear todo el acceso público”.
Confirma la advertencia y crea el bucket.
Añadir una Política de Bucket para Acceso Público:
En la pestaña “Permisos”, selecciona “Editar”.
Copia y pega la siguiente política de bucket (reemplazando “example-bucket” con el nombre real del bucket):
JSON
````
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": ["s3:GetObject"],
            "Resource": ["arn:aws:s3:::example-bucket/*"]
        }
    ]
}
````
Código generado por IA. Revisar y usar cuidadosamente. Más información sobre preguntas frecuentes.
Guarda los cambios.
Subir un Documento HTML:
Descarga el archivo “index.html” y guárdalo en tu equipo local.
En la consola de S3, selecciona la pestaña “Objetos”.
Carga el archivo “index.html” en el bucket.
Asegúrate de que esté seleccionada la clase de almacenamiento “Estándar”.
Probar el Sitio Web:
En la pestaña “Propiedades”, habilita el alojamiento de sitios web estáticos.
Define “index.html” como el documento de índice.
Copia la URL del punto de enlace de sitio web del bucket



# Módulo 5
CDN Servicio de entrega de contenido rápida, demultimedia, 

AWS DIRECT Connect, solucion de servicio de nube dedicada desde su entorno en instalaciones a AWS, 

Almacenamiento en caché, almacen de datos que recupera rápidamente información

Red de entrega de contenido CDN: Sistema de servidores distribuídos que entrega páginas y otro contenido web a un usuario, segun , localidad, origen,  y servidor de entrega 

Distribución : indica donde obtener información almacenando al caché  en ub. de brode, con seguimiento y administración de entrega

Ubicación de borde: Almacenar datos para reducir latencia 

Origen HTTP Protocol bucket de Amazon s3

# Módulo 6
# Módulo 7
# Módulo 8
# Módulo 9
# Módulo 10
# Módulo 11
# Módulo 12
# Módulo 13
# Módulo 14
# Módulo 15
# Módulo 16
