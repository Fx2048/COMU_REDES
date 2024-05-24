# Laboratorio del módulo 6: Asociar un volumen de EBS

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

# Final

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/bb7cba37-21ac-4dad-9188-54f878c4b9ea)

