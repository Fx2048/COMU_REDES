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
A. Shield Servicio de protecion contra DDOS en AWS

WAF , Protege las cuentas mediante reglas de seguridad web-trafico web específico

DDOS)DENEGACIÓN de servicio distribuído(Intento malicioso de que un sistea no esté disponible para usuarios finales

Ispector Seguridad automátizada, notifica pero no resuelve

Artifact Acceso a informes de seguridad y conformidad de AWS.


# Módulo 9
CloudWatch-Monitoreo recursos AWS

CloudTrail - Registro y monitoreo de cada acción llevado a cabo en cuenta AWS para seguridad

Config Service for analysis, auditar, evaluar config. from AWS resources

SimpleNotification Service -Notificar a otros servicios en la nube

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/e74b2362-efb1-40a0-b625-5235dcb7e800)

Cloudwatch confugurar alarma,y sns para enviar mensjaes

cloud watch monitorea, y aws trail registra,

para crear una alarma, suscribes a un tema el user  

# Módulo 10
Base de datos relacional-Coleccion de conjuntos de datos organizados como registros y columnas en tablas

Amazon Relational Database Service (Amazon RDS) Crear y administrar DB relacionals cloud MSQL

Amazon Dynamo DB Pares valor-no relacional

Base de datos no relacional-(No SQL) , par valor -diferentres

Amazon Redshift Service Storage AWS BIGDATA-Bussiness

Procesamiento de transacciones En Línea OLTP -Category process data Transacciones, Edita,suprime little datos from BD.Online Transaction Processing (OLTP) no relacional

OLAP (procesameinto analítico en Línea -Mtdo. extraer consultar datos de forma eficiente y selectiva para analizar desde diferentes puntos de vista.Online analytical processing(OLAP) relacional

Amazon Aurora -Motor de DB relacional compatible con MYSQL, y postgreSQL, for cloud(rentable simple)

MySQL:Administra BDRelational OpenCode


![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/fa20ccee-357b-4898-8443-c4689836951c)



# Módulo 11
Amazon Elastic Cache Escalado y funcionamiento de memoria caché.Mejor rendimeinto ,permiitiendo recuperar dese caché

Caché:capa de storage de datos de alta velocidad  transitorios, y rápidos

Escalado vertical(storage for ec2) and horizontal (ec2)
Almacenamiento de datos en caché:reutiliza eficiently datos recuperados o calculados , los datos se pueden utilizar con (STORAGE)Ram, componente de software.

Elastic Load Balancing dirige a EC2,IP, y LAmbda (storage) dada la sobrecarga .
Memoria de Acceso Aleatorio (RAM).No almacena cerrada la sesión, y al no haber disponibildiad,usa ROM(Lecture)

# Módulo 12
A. Elastick BeansTALK: administra detalles de aprovisionamiento,balanceo,escalado,monitoreo

CloudFormation: crear conjunto de recursos de aws erelacionados

pila Conjunto de recursos de AWS administrados con una sola unidad.

# Módulo 13

Machine Learning (ML): Es un campo de la inteligencia artificial que se enfoca 
en desarrollar algoritmos y modelos que permiten a las computadoras aprender a partir de datos y mejorar su rendimiento con la experiencia. Se utiliza para tareas como clasificación, regresión, agrupamiento y recomendación.

Inteligencia Artificial (IA): La IA se refiere a la capacidad de las máquinas para realizar tareas que normalmente requieren inteligencia humana. Esto incluye el procesamiento del lenguaje natural, la visión por computadora, la toma de decisiones y más.

Amazon SageMaker: Es un servicio de AWS que facilita la construcción, el entrenamiento y la implementación de modelos de machine learning. Proporciona un entorno integrado para experimentar con algoritmos y datos.

Deep Learning: Es una subárea del machine learning que utiliza redes neuronales profundas para resolver problemas complejos. Estas redes están compuestas por múltiples capas y se utilizan para tareas como reconocimiento de imágenes, procesamiento del lenguaje natural y más.

DeepRacer: Es un programa de AWS que combina machine learning y carreras de autos. Los participantes entrenan modelos de RL (reinforcement learning) para conducir un auto de carreras autónomo en una pista virtual.

DeepLens: Es una cámara inteligente desarrollada por AWS que procesa información en tiempo real utilizando redes neuronales. Puede utilizarse para aplicaciones como reconocimiento de objetos, seguimiento de personas y más.

# Módulo 14

Calculadora de costo mensual de AWS: Es una herramienta que permite estimar el costo de los servicios de AWS que se utilizan en función de los recursos y la configuración seleccionada.

AWS Support: Es un servicio de soporte técnico proporcionado por AWS. Ofrece diferentes niveles de soporte para ayudar a los clientes a resolver problemas y obtener asistencia técnica.

Organizaciones: Es un servicio que permite administrar múltiples cuentas de AWS como una sola entidad. Se utiliza para centralizar la facturación, la administración de políticas y la organización de recursos.

Facturación unificada: Es un enfoque que permite consolidar la facturación de múltiples cuentas de AWS en una sola factura. Esto facilita la gestión financiera y la visibilidad de los costos.

Gerente de cuenta TAM (Technical Account Manager): Es un profesional de AWS que trabaja directamente con los clientes para ayudarlos a optimizar su infraestructura, resolver problemas técnicos y planificar estratégicamente

# Módulo 15

Cadena de bloques: Una cadena de bloques (o blockchain en inglés) es una estructura de datos descentralizada y distribuida que registra transacciones de manera segura y transparente. Cada bloque contiene un conjunto de transacciones y está vinculado al bloque anterior mediante criptografía, formando una cadena inmutable.

Transacción: Una transacción es una acción o evento que involucra la transferencia de valor o información. En el contexto de las cadenas de bloques, una transacción representa el intercambio de activos digitales (como criptomonedas) o la actualización de registros.

Libro de contabilidad: También conocido como ledger, es un registro que almacena todas las transacciones realizadas en una cadena de bloques. Es transparente, inmutable y accesible para todos los participantes de la red.

Bloque: Un bloque es una unidad básica de datos en una cadena de bloques. Contiene un conjunto de transacciones y un sello de tiempo. Los bloques se enlazan entre sí para formar la cadena.

Inmutable: Significa que una vez que se registra una transacción en la cadena de bloques, no se puede modificar ni eliminar. La inmutabilidad garantiza la integridad y la confianza en los datos almacenados.

Confianza: En el contexto de las cadenas de bloques, la confianza se refiere a la seguridad y la fiabilidad del sistema. La tecnología de cadena de bloques permite confiar en los datos y las transacciones sin depender de intermediarios.

Transparencia: La transparencia en una cadena de bloques se refiere a la visibilidad de todas las transacciones y registros para todos los participantes. Cada cambio es visible y auditable.


# Módulo 16
El Kit de Desarrollo en la Nube de AWS (AWS CDK) es un marco de desarrollo de software de código abierto que permite a los desarrolladores definir y gestionar su infraestructura de nube mediante código
