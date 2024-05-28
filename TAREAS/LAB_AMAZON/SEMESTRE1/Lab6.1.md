![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/95680ef4-ddfc-4198-b596-ab253aa25240)

Asociar un Volumen EBS a una Instancia EC2

Accede a la Consola de Administración de AWS:

Inicia sesión en tu cuenta de AWS.

Ve a la Consola de Administración de AWS.

Navega a la sección de Volumenes de EBS:

En el menú de servicios, busca “Almacenamiento” y selecciona “EC2”.

En el panel de navegación izquierdo, selecciona “Volúmenes”.

Crea un Volumen EBS:

Haz clic en “Crear volumen”.

Configura el tipo de volumen, tamaño y otras opciones según tus necesidades.

Asegúrate de que el volumen esté en la misma zona de disponibilidad que la 
instancia a la que deseas asociarlo.

Asocia el Volumen a la Instancia:

Selecciona el volumen recién creado.

En el menú “Acciones”, elige “Adjuntar volumen”.

Especifica el ID de la instancia EC2 a la que deseas adjuntar el volumen.

Asegúrate de que la instancia esté en la misma zona de disponibilidad que el volumen.

Monta el Volumen en la Instancia:

Conéctate a la instancia EC2 mediante SSH o RDP.

Utiliza comandos como lsblk o fdisk -l para identificar el dispositivo del 
volumen recién adjuntado (por ejemplo, /dev/xvdf).


Formatea el volumen con un sistema de archivos (por ejemplo, mkfs.ext4 
/dev/xvdf).

Crea un directorio de montaje (por ejemplo, sudo mkdir /mnt/myvolume).

Monta el volumen en el directorio (por ejemplo, sudo mount /dev/xvdf 
/mnt/myvolume).

Configura el Montaje Permanente (Opcional):

Edita el archivo /etc/fstab para que el volumen se monte automáticamente al reiniciar la instancia.

Agrega una línea como esta al archivo: /dev/xvdf /mnt/myvolume ext4 defaults 0 0.

Verifica el Montaje:

Ejecuta df -h para verificar que el volumen esté montado correctamente.

Asegúrate de que los datos sean accesibles en el directorio de montaje.

-----------------------------------------------
 Crearás una instancia de Amazon Elastic Compute 
 
 Cloud (Amazon EC2) y, a continuación,
 
 le adjuntarás un volumen de Amazon Elastic Block Store (Amazon EBS).

 Los primeros tasks son predeterminados, el SO, el tipo de instancia, 

````
#!/bin/bash
yum update -y
yum -y install httpd
systemctl enable httpd
systemctl start httpd
echo ' <html><h1>Hello World!</h1>
</html>' > /var/www/html/index.html

````
````
Actualiza el servidor
Instala un servidor web Apache (httpd)
Configura el servidor web para que comience
automáticamente durante el arranque
Activa el servidor web
Crea una página web sencilla
````
Tarea 8: Revisar la instancia y lanzarla

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/2152cc64-4335-439e-ba9c-e490b19999ab)

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/86d4ed58-4287-48e7-b860-342c7c8707df)


Accedemos a la Dirección IP PUBLICA PV4, y no 

se puede acceder porque habíamos eliminado las

reglas del grupo de seguridad, lo cual genera 

que no se pueda  acceder a HTTP puerto 80, 

lo que solucionaremos:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/d7d1fa2c-dca5-4743-91c5-67de4f46758e)

Luego comprobamos que la página funciona correctamente al actualizarla:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/72a4a19a-11ea-43dd-b5fd-7526d52d603a)


# tarea 13: : Adjuntar un volumen de EBS a la instancia de EC2

## Debe ser el mismo volumen state country( Disponibility Zone)

# Se creó un volumen asociado

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/ae411fc0-cfd4-4129-91f0-15a6c637fed4)



![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/21946c6c-b2c0-48b3-959d-530911ef86c7)


![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/43e72e0f-b453-429f-8ec8-f9547560d708)

