![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/add62f63-fcd2-4223-99d2-56f8ca0efb55)

# LABORATORY FROM 4.2 AMAZON WEB SERVICES: CREATE A BUCKET
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
## Policy Permissions for Bucket
####  for the policy version  and edit intructions

````
{
    "Version":"2012-10-17",
    "Statement":[
        {
            "Sid":"PublicReadGetObject",
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

````
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


Description Notes about the Session:
# Tasks:
## Properties
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/545c0702-1fc4-47ea-b01a-ec404e7a5512)

## OBject table
![OBJECT INDEX](https://github.com/Fx2048/COMU_REDES/assets/131219987/3ab04894-dcee-4977-8582-19eac3976265)

##  Information table from bucket
(Link to oso bucket ip public)[http://oso1.s3-website-us-east-1.amazonaws.com]
![properties to oso ](https://github.com/Fx2048/COMU_REDES/assets/131219987/aad12038-c080-45eb-8b94-73928a955a07)

![OSO CREATION GNEERAL BUCKET](https://github.com/Fx2048/COMU_REDES/assets/131219987/6c5a387a-265f-4376-a7b4-df3b16aba374)




![permissions](https://github.com/Fx2048/COMU_REDES/assets/131219987/889c26f9-460b-416c-9ca1-cc1e0fd4a922)




# output index.html into bucket page
![OUTPUT FOLLOW LEADER](https://github.com/Fx2048/COMU_REDES/assets/131219987/1a6a4b0c-bca0-4054-bbae-75f234d19631)

Glossary:

````
Puntos de acceso
Los puntos de acceso de Amazon S3 son puntos de enlace de red denominados con políticas de acceso dedicadas que describen cómo se puede acceder a los datos mediante ese punto de enlace.

propiedades cifrado sc3 cs2-wordpress
punto de enlace
bucket s3
wordpress
static site
karpathy rnn https://karpathy.github.io/2015/05/21/rnn-effectiveness/
jekill https://jekyllrb.com/docs/github-pages/
grupos de seguridad
bash
json
decorador
commands
cherban
entorno propietario finalidad
capa 7 capa 2  

````

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/d79215c7-5eba-46fd-ad1a-11b958602210)


