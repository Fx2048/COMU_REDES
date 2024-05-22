Laboratorio del módulo 5: Uso de CloudFront como CDN para un sitio web
Información general sobre el laboratorio
En este laboratorio, utilizarás Amazon CloudFront como red de entrega de contenido (CDN) para un sitio web almacenado en Amazon Simple Storage Service (Amazon S3).

Duración
El tiempo estimado para completar este laboratorio es de 40 minutos.

Acceso a la consola de administración de AWS
Para comenzar la sesión de laboratorio, elige  Start Lab (Iniciar laboratorio) en la esquina superior derecha de la página.

Comienza la sesión del laboratorio.

En la esquina superior derecha de esta página aparece un temporizador que muestra el tiempo que queda de la sesión.

Consejo: Para actualizar la duración de la sesión en cualquier momento, vuelve a seleccionar Start Lab (Iniciar laboratorio) antes de que el temporizador llegue a 0:00.

Antes de continuar, espera hasta que el entorno de laboratorio esté listo. El entorno está listo cuando aparecen los detalles del laboratorio en el lado derecho de la página y el icono del círculo junto al enlace de AWS en la esquina superior izquierda pasa a ser verde.

Para volver a estas instrucciones, elige el enlace  Readme (Léeme) en la esquina superior derecha.

Para conectarte a la consola de administración de AWS, selecciona el enlace de AWS situado en la esquina superior izquierda, sobre la ventana del terminal.

Se abre una nueva pestaña del navegador que te conecta a la consola de administración de AWS.

Consejo: Si no se abre una nueva pestaña del navegador, es posible que haya un banner o un icono en la parte superior del navegador con un mensaje que indique que el navegador está impidiendo que el sitio abra ventanas emergentes. Elige el banner o el icono y, a continuación, Allow pop-ups (Permitir elementos emergentes).

Nota: Vas a utilizar la consola en el entorno de laboratorio, por lo que no incurrirás en ningún gasto real. Sin embargo, en el mundo real, cuando se utiliza una cuenta personal o de empresa para acceder a la consola, los usuarios incurren en gastos por el uso de servicios específicos de AWS.

Tarea 1. Crear un bucket de S3 mediante AWS CLI
En esta tarea, crearás un bucket de S3 mediante la Interfaz de la línea de comandos de AWS (AWS CLI). AWS CLI es una herramienta de código abierto que puedes utilizar para interactuar con los servicios de AWS mediante comandos en tu shell de línea de comandos.

Elige Servicios y Herramientas para desarrolladores y, después, CloudShell.

Si aparece una ventana emergente de bienvenida, selecciona Cerrar.

AWS CloudShell es un shell basado en navegador que da acceso a la línea de comandos para los recursos de AWS en la región de AWS seleccionada.

Copia y pega el siguiente código en un editor de texto:

cd ~
aws s3api create-bucket --bucket (bucket-name) --region us-east-1
En el código que has copiado, reemplaza el nombre del bucket (bucket-name) por un nombre exclusivo compatible con el sistema de nombres de dominio (DNS) para el nuevo bucket.

Sigue estas pautas de nomenclatura:

El nombre debe ser único entre todos los nombres de bucket existentes en Amazon S3.
El nombre debe tener entre 3 y 63 caracteres.
El nombre solo puede contener letras minúsculas, números, puntos (.) y guiones (-).
El nombre debe empezar y terminar con una letra o un número.
El nombre no debe tener formato de dirección IP (por ejemplo, 192.168.5.4).
Después de crear el bucket, no podrás cambiar el nombre, así que elígelo bien.
Elige un nombre de bucket que refleje los objetos del bucket. Esto es así porque el nombre del bucket se ve en la dirección URL del sitio web que apunta a los objetos que vas a poner en el bucket.
Consejo: A continuación se muestra un nombre de bucket de ejemplo: mylabbucket12345

Nota: La región us-east-1 se ha introducido en el comando. Al crear un bucket, la práctica recomendada es elegir una región cercana para minimizar la latencia y los costes o para cumplir los requisitos normativos. Los objetos almacenados en una región nunca abandonan esa región a menos que los transfieras explícitamente a otra región.

Ejecuta el código actualizado en el terminal de CloudShell.

Si aparece una ventana emergente, selecciona Pegar.

El resultado debe tener un aspecto similar al siguiente:

{
   "Location": "/mylabbucket12345"
}
Nota: Al crear un bucket con este comando, el bucket está abierto al público. Te recomendamos que mantengas habilitada toda la configuración a menos que sepas que tendrás que desactivar uno o más ajustes para tu caso de uso, por ejemplo, para alojar un sitio web público.

Tarea 2. Añadir una política de bucket
En esta tarea, añadirás una política de bucket a través de AWS CLI para que el contenido esté disponible públicamente.

En la consola, selecciona el menú Servicios, localiza la sección Almacenamiento y elige S3.
Elige el nombre del bucket que acabas de crear.
Selecciona la pestaña Permisos. En Bloquear acceso público (configuración del bucket), selecciona Editar. Desactiva la casilla de Bloquear todo el acceso público. Elige Guardar cambios. Confirma los cambios.
Desplázate hasta Propiedad del objeto y selecciona Editar. Selecciona ACL habilitadas. Comprueba el reconocimiento y, selecciona Guardar cambios.
En la sección Política del bucket, selecciona Editar.
Para conceder acceso de lectura pública a tu sitio web, copia y pega la siguiente política del bucket en el editor de políticas.
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Sid":"PublicReadForGetBucketObjects",
         "Effect":"Allow",
         "Principal":"*",
         "Action":[
            "s3:GetObject"
         ],
         "Resource":[
            "arn:aws:s3:::example-bucket/*"
         ]
      }
   ]
}
En la política, reemplaza example-bucket por el nombre del bucket.
En la parte inferior de la página, selecciona Guardar cambios.
Tarea 3. Subir un documento HTML
En esta tarea, subirás el archivo index.html de tu página web en el bucket de S3.

Abre el menú contextual (haz clic con el botón derecho) del siguiente enlace y, a continuación, elige Save link as (Guardar enlace como): index.html

Guarda el archivo index.html en el equipo local.

En la consola, selecciona la pestaña Objetos.

Carga el archivo index.html en tu bucket.

Selecciona Cargar.
Arrastra y suelta el archivo index.html en la página de carga. También puedes seleccionar Añadir archivos, buscar el archivo y usar la opción Abrir.
Expande la sección Permisos.

En ACL predefinidas, selecciona Conceder acceso de lectura público.

Debajo de la configuración seleccionada aparece un mensaje parecido a este: No se recomienda otorgar acceso de lectura público.

Marca la casilla que aparece junto a Entiendo que... debajo del mensaje de advertencia.

En la parte inferior de la página, selecciona Cargar.

Selecciona Cerrar.

El archivo index.html aparece en la lista Objetos.

Tarea 4. Probar el sitio web
Selecciona la pestaña Propiedades y desplázate a la sección Alojamiento de sitios web estáticos.

Selecciona Editar.

Selecciona Habilitar.

En el cuadro de texto Documento de índice, introduce "index.html".

Selecciona Guardar cambios.

Desplázate de nuevo hacia abajo hasta la sección Alojamiento de sitios web estáticos y copia la URL del Punto de enlace de sitio web del bucket en el portapapeles.

Abre una nueva pestaña en el navegador web, pega la URL que acabas de copiar y pulsa Intro.

Debería abrirse la página web Hello World. Has alojado correctamente un sitio web estático mediante un bucket de S3.

Tarea 5. Crear una distribución de CloudFront para servir al sitio web
En esta tarea, crearás una distribución de Amazon CloudFront para servir al sitio web.

Selecciona el menú Servicios, localiza la sección Redes y entrega de contenido y selecciona CloudFront.

Selecciona Crear una distribución de CloudFront.

En la sección Origen, selecciona el cuadro de texto que aparece junto a Dominio de origen y selecciona el punto de enlace de tu bucket de S3.

Para Viewer Protocol Policy (Política de protocolo de visor), asegúrate de que HTTP y HTTPS estén seleccionados. En Web Application Firewall (WAF), selecciona Do not enable security protections (No habilitar protecciones de seguridad).

Desplázate hasta la parte inferior de la página y selecciona Crear distribución.

Se muestra una nueva distribución de CloudFront en la lista de distribuciones. El Estado será Implementando hasta que el sitio web se haya distribuido. Puede tardar hasta 20 minutos.

Cuando el Estado sea Habilitado, puedes probar la distribución.

Copia el valor de Nombre de dominio de la distribución y guárdalo en un editor de texto para utilizarlo en un paso posterior.

Crea un nuevo archivo HTML para probar la distribución.

Busca y descarga una imagen de Internet.
Navega hasta el bucket de S3 y carga el archivo de imagen en el bucket, asegurándote de otorgar acceso público tal como lo hiciste al subir el archivo HTML antes en este laboratorio.
Crea un nuevo archivo de texto con el Bloc de notas y copia en él el siguiente texto:
<html>
    <head>My CloudFront Test</head>
    <body>
        <p>My test content goes here.</p>
        <p><img src="http://domain-name/object-name" alt="my test image">
    </body>
</html>
Reemplaza domain-name por el nombre de dominio que copiaste antes para la distribución de CloudFront.
Reemplaza object-name por el nombre del archivo de imagen que cargaste en el bucket de S3.
La línea de código editada debe tener un aspecto similar al siguiente:

<p><img src="http://d2f1zrxb2zaf30.cloudfront.net/picture.jpg" alt="my test image">
Guarda el archivo de texto con extensión HTML.
Utiliza un navegador de Internet para abrir el archivo HTML que acabas de crear.
Si se muestra la imagen que cargaste, la distribución de CloudFront se realizó correctamente. Si no es así, repite el laboratorio.

Laboratorio completado
¡Enhorabuena! Has completado el laboratorio.

Cierra la sesión de la consola de administración de AWS.

En la esquina superior derecha, selecciona tu nombre de usuario, que comienza por voclabs/user.
Selecciona Cerrar sesión.
Selecciona Finalizar laboratorio en la parte superior de esta página y, a continuación, selecciona Sí para confirmar que quieres dar por concluido el laboratorio.
