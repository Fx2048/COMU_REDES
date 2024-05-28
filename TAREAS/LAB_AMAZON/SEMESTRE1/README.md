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


# Módulo 5
CDN Servicio de entrega de contenido rápida, demultimedia, 

AWS DIRECT Connect, solucion de servicio de nube dedicada desde su entorno en instalaciones a AWS, 

Almacenamiento en caché, almacen de datos que recupera rápidamente información

Red de entrega de contenido CDN: Sistema de servidores distribuídos que entrega páginas y otro contenido web a un usuario, segun , localidad, origen,  y servidor de entrega 

Distribución : indica donde obtener información almacenando al caché  en ub. de brode, con seguimiento y administración de entrega

Ubicación de borde: Almacenar datos para reducir latencia 

Origen HTTP Protocol bucket de Amazon s3

CloudFront funciona con las ubicaciones de borde que forman parte de la infraestructura global de AWS.almacenamiento en caché de los datos solicitados con frecuencia en las ubicaciones de borde. Aunque la solicitud inicial pide a CloudFront que cargue el archivo en la memoria caché, las solicitudes posteriores se pueden satisfacer mucho más rápido y parte del trabajo se puede descargar desde el servidor de origen.


# Módulo 6
(A. EBS) A.elastic Block Store Alm. para instancias EC2

A. Elastic COmpute CLoud .Escalable service web 

Unidad de Disco Duro(HDD) Almacena datos , disco giratorio- Hard Dsik Drive

Operaciones de entrada y salida por segundo(IOPS), Medida de rendimiento frecuente para comparar dispositivos de almacenamiento HDD y SSD

Unidad de estado Sólido(SSD) memoria flash en disk giratorio. solid state drive

# Módulo 7
IAM Impplies applied controls for access informatic resources

Rol IAM identity for create your account and have speccified policies.

User Components: Name and credentials

Security Group:firewall

Policy Define Permissions.

Amazon Inspector Help to the client identify vulnerabilities  while a production environment goes run.

Group,Speccified permissions for lot of users, facilitate the  permissions by users administration 

Rooter User-for sign-up in the website

Credential-
multiFactor Authentication Enability(MFA)-Independents data

JavaScript Object notation(Json) Sintaxis to save data

Multifactor Authentication-indenpendent categories
Block Access clave from users rooter from account AWS, 

Create individual users from IAM, 

Create user groups for assign policies to users from IAM

Give less priviledges

JSON policies, 

and Applied managed Policies by the client 


Applied access level for review the policies from IAM

Configure a safe passwords policy for users


Enable MFA

Applied Rols for applications executed in A. EC2 instances
Divide policies


Don't share access clave

Change the credentials  regularly

Suprime innecesary credentials

Suppervise the activity from your account AWS


# Módulo 8
# Módulo 9
# Módulo 10
# Módulo 11
# Módulo 12
# Módulo 13
# Módulo 14
# Módulo 15
# Módulo 16
