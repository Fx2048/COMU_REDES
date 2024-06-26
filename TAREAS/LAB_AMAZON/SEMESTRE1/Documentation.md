# A. AuroraAlto rendimiento inigualable y disponibilidad a escala global, con compatibilidad total con MySQL y PostgreSQL

Rendimiento Superior: Aurora ofrece un rendimiento hasta 5 veces superior al de MySQL y 3 veces al de PostgreSQL, a una fracción del costo de las bases de datos comerciales1.

Alta Disponibilidad: Proporciona una disponibilidad de hasta el 99,99% y resiliencia de almacenamiento en 3 zonas de disponibilidad.

Escalabilidad sin Servidor: Utiliza tecnología sin servidor para escalar hasta cientos de miles de transacciones en segundos2.

Seguridad y Gestión: Incluye seguridad integrada, copias de seguridad continuas y es completamente administrada, lo que reduce el costo total de propiedad.

# A. EBS Store

Almacenamiento en bloque de alto rendimiento y con facilidad de uso a cualquier escala


Complete el registro

Beneficios de Amazon EBS

Escale rápido

Escale rápidamente sus cargas de trabajo más demandantes y de alto rendimiento, incluidas las aplicaciones esenciales, como SAP, Oracle y los productos de Microsoft.
Alto rendimiento


Evite los fallos gracias a una alta disponibilidad, incluida la replicación dentro de las zonas de disponibilidad (AZ), y una durabilidad del 99,999 % con los volúmenes de io2 Block Express.

Optimice el almacenamiento y los costos

Seleccione el almacenamiento que mejor se adapte a su carga de trabajo. Los volúmenes van desde los más rentables por dólar por GB hasta los de alto rendimiento con las más rápidas IOPS y rendimiento.

Seguridad

Cifre los recursos de almacenamiento en bloque sin necesidad de crear, mantener ni proteger una infraestructura propia de administración de claves. Evite el acceso no autorizado a los datos al restringir el acceso público y configurar bloqueos en las copias de seguridad de los datos.

Protección de datos sencilla

Proteja los datos almacenados en bloque en la nube, así como los datos en bloque locales mediante las instantáneas de Amazon EBS, una copia de un momento dado que se puede utilizar para permitir la recuperación de desastres, migrar datos entre regiones y cuentas, y mejorar el cumplimiento de las copias de seguridad. AWS simplifica aún más la administración del ciclo de vida de las instantáneas mediante la integración con Amazon Data Lifecycle Manager, que permite crear políticas para automatizar varias tareas, como la creación, la eliminación, la retención y el uso compartido de instantáneas.


# A. EC2
EC2 y Virtualización: EC2 permite lanzar y configurar servidores virtuales en la nube, similares a las máquinas virtuales en un entorno local. Utiliza la virtualización para dividir un host físico en múltiples VMs (máquinas virtuales), cada una ofreciendo diferentes servicios.

Familias y Tipos de Instancias: AWS ofrece una amplia selección de familias y tipos de instancias EC2, cada una diseñada para casos de uso específicos como equilibrio de recursos, computación de alto rendimiento, o aplicaciones intensivas en memoria.

Almacenamiento EBS: Las instancias EC2 requieren un volumen de almacenamiento en bloque, como EBS (Elastic Block Store) o volúmenes de almacenamiento de instancias, para alojar el sistema operativo y las aplicaciones.

Imágenes AMI: Las AMIs (Amazon Machine Images) son instantáneas que contienen sistemas operativos y aplicaciones para configurar instancias EC2. Son específicas de la región y pueden copiarse entre regiones si es necesario.



# A. S3Almacenamiento de objetos creado para recuperar cualquier volumen de datos desde cualquier ubicación

Almacenamiento en la Nube: Amazon S3 es una solución de almacenamiento de objetos que ofrece alta disponibilidad, durabilidad y escalabilidad12. Es ideal para convertirse en nativo de la nube a largo plazo.


Tipos de Almacenamiento: AWS proporciona almacenamiento en bloque (EBS), almacenamiento de archivos (EFS, FSx) y almacenamiento de objetos (S3), cada uno adecuado para diferentes casos de uso y requisitos de acceso.

Gestión de Datos: Amazon S3 permite la gestión inteligente de datos con políticas de ciclo de vida, versionado y cifrado, optimizando costos y seguridad.

Clases de Almacenamiento: AWS ofrece diversas clases de almacenamiento, como Glacier para archivado a largo plazo y S3 estándar para acceso instantáneo, adecuadas para diferentes patrones de acceso y requisitos de durabilidad.
# A.DynamoBase de datos NoSQL, totalmente administrada y sin servidor con un rendimiento de milisegundos de un solo dígito a cualquier escala

Servicio sin servidor: DynamoDB es una base de datos NoSQL que escala automáticamente y solo cobra por el uso real1.

Rendimiento y seguridad: Ofrece tiempos de respuesta rápidos, almacenamiento ilimitado y un conjunto completo de controles de seguridad.

Tablas globales: Soporta tablas multirregionales para aplicaciones distribuidas con un SLA de disponibilidad del 99,999%2.

Integración con AWS: Se integra con otros servicios de AWS para análisis y procesamiento de eventos en tiempo real.

# VPC

VPC y Subredes: Una VPC es una red virtual en la nube que permite aislamiento de recursos y configuración de parámetros de red1. Las subredes son subconjuntos de la VPC que se definen en bloques de direcciones IP y están restringidas a una zona de disponibilidad2.

Acceso a Internet: Para que las instancias EC2 en una VPC tengan acceso a Internet, se debe implementar una puerta de enlace a Internet y configurar las tablas de rutas3. Las direcciones IP públicas son necesarias para el tráfico entrante y saliente.

Seguridad VPC: AWS ofrece grupos de seguridad y listas de control de acceso a la red (NACL) para gestionar el acceso a los recursos dentro de la VPC. Los grupos de seguridad actúan a nivel de instancia y las NACL a nivel de subred4.

Conectividad y VPN: Se pueden establecer conexiones seguras entre VPCs mediante interconexiones de VPC y conectar la VPC a redes corporativas a través de VPNs o Direct Connect para una conexión más dedicada y privada.

# Amazon Comprehend 

utiliza el procesamiento de lenguaje natural (NLP) para extraer información sobre el contenido de los documentos. Genera información a partir del reconocimiento de entidades, frases clave, lenguaje, opiniones y otros elementos comunes en un documento. 

aprendizaje por refuerzo,

ai learn to walk deep reinforcement learning, 

que es amazon pcomprehend, 

servicios de inteloigencia artiifcial en aws  machine learning en aws 

sdk kit de desarrollo y blueprint

autoscaling y funciones lambdas | 

video:aws cloud trail simply security analysis resource change tracking and troubleshooting | 

mateiral de certificacion de aws |

amazon web service |

video aws global cloud infraestructure 

why use aws industry blueprints for data & ai | 

estructura global  de aws|  

lecture nivel gratuito de aws |

adminstracion de acceso e identidad  | 

sobre s3 | 

sobre vpc 

| redes y nube| 

route53 y cloudFront|


Registro de Dominio: Explica cómo registrar un nombre de dominio con Amazon Route53, eligiendo entre varios TLDs y la importancia de renovar el arrendamiento del dominio.

Zonas Alojadas: Detalla cómo crear zonas alojadas públicas y privadas en Route53 para gestionar el tráfico de dominios y subdominios.

Políticas de Enrutamiento: Describe las políticas de enrutamiento de Route53, incluyendo enrutamiento simple, de conmutación por error, de geolocalización y de latencia, para optimizar la distribución del tráfico.

Health Checks: Discute las comprobaciones de estado en Route53 para monitorear la salud de los recursos y asegurar la alta disponibilidad de los servicios.


lectura sservicios ec2 y ebs |

video amazon elastic block store (ebs) overview) | 

caracterísiticas de amazon ec2|

base de datos relacionales con aws |

video what is amazon  dynamo DB | 


base de datos no relacionales en AWS  



| Aws high avalilty compute sql and storage  

| alta disponiilida d y elastiicdiad en aws |

elasiticidad con autoescaling | 

__________________________________________________________
Wordpress
an account free for Learning


SIN CUESTIONARIO, EC2, Y REDES, VPC HTTP , WORDPRESS, LAMBDA

AUTOSCALING, APPS ML, en entorno de nube


servidore de web dinamico, aligment, cores, consola, interface, project,   entender el flujo, 
````
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/3a04404f-d19c-4827-a815-e8fa27b82dec)

````

multiprpocesador  planificacion 


Plataforma de Servicios: AWS es una plataforma de servicios en la nube que ofrece soluciones flexibles, escalables y confiables para empresas y desarrolladores1.
Capacidades de AWS: Permite alojar tiendas en línea, ejecutar aplicaciones Java EE en redes privadas y crear sistemas altamente disponibles.
Beneficios de AWS: Incluye innovación constante, servicios para problemas comunes, automatización y escalabilidad flexible.
Costos y Facturación: AWS tiene un modelo de pago por uso, con un nivel gratuito para nuevos usuarios y precios competitivos basados en el consumo


Amazon EC2 (Elastic Compute Cloud): Proporciona instancias de máquinas virtuales escalables en la nube. Los usuarios pueden elegir entre diferentes tipos de instancias según sus necesidades de cómputo, memoria y almacenamiento.
Amazon S3 (Simple Storage Service): Ofrece almacenamiento de objetos altamente escalable y duradero. Es ideal para almacenar datos, archivos multimedia y copias de seguridad.
AWS Lambda: Permite ejecutar código sin aprovisionar ni administrar servidores. Es útil para implementar funciones sin servidor y eventos basados en disparadores.
Amazon RDS (Relational Database Service): Proporciona bases de datos relacionales gestionadas, como MySQL, PostgreSQL y SQL Server.
Amazon VPC (Virtual Private Cloud): Permite crear redes virtuales aisladas en la nube con control sobre la topología de red, subredes, tablas de rutas y puertas de enlace.
Amazon Route 53: Es un servicio de DNS escalable y altamente disponible que permite registrar dominios y administrar la resolución de nombres.
Amazon ECS (Elastic Container Service): Facilita la implementación y administración de contenedores Docker en la nube.
Amazon CloudFront: Es una red de entrega de contenido (CDN) que acelera la entrega de contenido web a nivel global.
Amazon DynamoDB: Es una base de datos NoSQL totalmente administrada y escalable.
AWS Elastic Beanstalk: Simplifica la implementación y administración de aplicaciones web en diferentes lenguajes de programación.
Amazon SQS (Simple Queue Service): Proporciona colas de mensajes para la comunicación entre componentes de aplicaciones distribuidas.
AWS IAM (Identity and Access Management): Controla el acceso a los recursos de AWS mediante políticas y roles.
Amazon CloudWatch: Monitorea recursos y aplicaciones en AWS, proporcionando métricas, alarmas y registros.
AWS CloudFormation: Permite definir y aprovisionar recursos de AWS como código.
Amazon Glacier: Almacena datos de archivo a largo plazo a bajo costo.
AWS Kinesis: Procesa y analiza datos en tiempo real.
Amazon EMR (Elastic MapReduce): Proporciona un entorno escalable para procesamiento de big data utilizando Apache Hadoop y Spark.
Seguridad y Buenas Prácticas:
Grupos de seguridad: Configura reglas de firewall para controlar el tráfico de red hacia y desde las instancias de EC2.
IAM Roles: Asigna permisos específicos a las instancias y servicios sin exponer credenciales.
Encriptación: Utiliza SSL/TLS para cifrar datos en tránsito y KMS (Key Management Service) para gestionar claves de cifrado.
Auditoría y Registro: Habilita CloudTrail para rastrear eventos y actividades en la cuenta de AWS.
Actualizaciones y Parches: Mantén las instancias actualizadas con las últimas correcciones de seguridad.
Respaldo y Recuperación: Realiza copias de seguridad periódicas y prueba la recuperación de datos.
Monitorización y Alarmas: Configura alertas para detectar comportamientos anómalos o problemas de rendimiento
