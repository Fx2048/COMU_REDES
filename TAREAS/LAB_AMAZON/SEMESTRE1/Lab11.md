![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/46c2ec5c-5de9-4dc7-9ea6-1599006f1f84)

# Instructions from the Charge Equilibrium 
Configuración Inicial: Crea una VPC con un bloque CIDR y adjunta una puerta de enlace a internet.

Subredes y EC2: Establece dos subredes públicas en zonas de disponibilidad diferentes y lanza dos instancias EC2.

Grupo de Destino: Crea un grupo de destino y registra las instancias EC2 como objetivos.

ALB: Configura un Balanceador de Carga de Aplicaciones (ALB), define sus propiedades y enlázalo con el grupo de destino.

Pruebas: Accede a la URL pública del ALB para verificar que las solicitudes se distribuyen entre las dos instancias.

________________________________________________________________________________
________________________________________________________________________________
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/1b0d7f03-b721-4cb7-ab28-face88dbdaf0)
`````
# user data script ------
#!/bin/bash
yum update -y
yum -y install httpd
systemctl enable httpd
systemctl start httpd
echo '<html><h1>Hello World! This is server 2.</h1></html>' > /var/www/html/index.html
`````
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/4dbb20fe-7161-48d1-9f58-d1c52fab9553)


![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/25463264-7968-460f-b02d-8832b7526c2f)

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/240b9411-649e-4530-bceb-0f9aa42915e8)

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/4841e342-8141-43cb-8af3-3686765afeee)


![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/b6d7cab7-525c-40cd-9649-e8c9a310d581)

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/2c5d70eb-94c9-4205-8a14-895afd466323)

