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



