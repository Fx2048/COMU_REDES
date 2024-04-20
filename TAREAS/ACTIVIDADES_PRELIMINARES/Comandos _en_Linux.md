# COMANDOS EN LINUX
### A continuación se presentará la realización de trabajo ejecutado, con resultados mostrados en pantalla y con explicación:

## What is the shell
Bien! Para comenzar en la terminal escribiremos cualquier idea para ver el output:
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/15dcb6e1-c922-4d5f-8877-aff19b62a7b0)
 Hemos recibido un mensaje de error quejándonos de que no puede entender el comando
 
## NAVIGATION 
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/0f1b290a-8557-4c10-8fba-2a5a64a4f645)

Cuando iniciamos sesión por primera vez en nuestro sistema Linux, el directorio de trabajo se establece en nuestro directorio de inicio. Aquí es donde ponemos nuestros archivos. En la mayoría de los sistemas, El directorio de inicio se llamará /home/user_name,pero podemos personalizarlo.

Para listar los archivos en el directorio de trabajo, usamos el comando.ls

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/55ea1f36-6820-4f18-aa61-aa9a52f209e2)

Lo que veremos significa desde el directorio raíz (representado por la barra diagonal inicial en el nombre de la ruta) Hay un directorio llamado "usr" que contiene un directorio llamado "bin" con ./usr/bin
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/e98af35c-019e-47d2-8305-26f026eb5f5a)

En seguida, Cambiemos el directorio de trabajo a /usr/bin otra vez:
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/1945e2df-1881-4459-917b-ad79c37c3141)

Si queremos cambiar el directorio de trabajo a la variable padre de los cuales  podríamos hacer eso de dos maneras diferentes. En primer lugar, con un nombre de ruta absoluto:/usr/bin/usr
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/ac1d3a6a-0140-4fcc-bfb9-9f6cfa3f9546)

o con nombre de ruta relativo:
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/8142e8cf-45c3-49f6-9696-e2b835dfe2fc)

también usando un valor absoluto, tan como se muestra:
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/70003d7e-28bd-4ae1-bd91-1bcc73d78ab8)

O bien, con un nombre de ruta relativo:
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/3bd6ca7b-bfc8-4a4f-9090-a4ced6a7cbdd)

Para reducir términos: 
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/bfb5a617-b1df-4d87-8c97-3e90f9a07086)

## MANIPULATING FILES
Con el siguiente comando de todo el código HTML de archivos de un directorio a otro, solo copiaría archivos que no existían en el directorio de destino o eran más recientes que las versiones del directorio de destino.
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/d73111d6-9606-4fef-ad44-c9618befcabc)

### Cp command sirve para copiar archivos y directorios
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/e467d464-2d4c-497c-b846-69db2e3b4499)

O copiar varios de ambos ,tanto archivos y directorios a un archivo o directorio distinto:
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/1e4ed274-a134-4265-8f5b-24013633b34a)

Si quieres editar el nombre de tu archivo, ejecuta mv seguido del archivo elegido mv:
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/67cb4ac9-324d-437d-b0b8-ae89779e5ca9)

y para mover de dirección tu archivo, opta por mv también!:
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/7b249b7c-857b-4814-9e6f-f0237c661eac)

En el caso de que decidas eliminar el archivo y/o directorio, trabaja con : rm, pero lastimosamente, no podrás recuperarlos una vez suprimidos en Linux:
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/be62d232-bfbc-4423-9768-635960863213)

Y para crear directorios, a través de mkdir lo harás!  :D
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/8a0ba4ad-129b-4fc3-beed-776288a48a52)


## WORKING WITH COMMANDS

### Interacción con los comandos iniciales de linux, por ejemplo, vemos 3 comandos distintos, , ls es un alias por el comando añadido de color=auto". 
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/25d58a56-02d7-44d5-becc-c3921dbb6be7)

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/055538c7-1348-47e1-9660-77007165bf82)
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/de4fe3c5-9a19-429a-a37d-f5ce1973104f)

### Which sirve para programas funcionales que pueden ejecutarse, no ni alias que son sustitutos de programas ejecutables reales.

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/b2652bf9-22d0-4ee4-9562-81782ad12871)

### Aquí se extiende el recurso de ayuda con respecto a su contenido:
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/d6e9c3fc-88d0-44d8-bbb6-f17b5cd1fda5)

### Elementos opcionales son mutuamente excluyentes simbolizados por corchetes :
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/d6f681fd-fcd1-46ab-a04f-2543e1464536)

### A veces puede que no encuentre --help la ayuda necesaria, dado que algunos programas no admiten la variable del comando original de help.
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/253e8c05-5b06-4970-80c0-593d503e0d65)

### Man sirve para llamar a manual en el comando, programa es el nombre del comando a visualizar...
![man](https://github.com/Fx2048/COMU_REDES/assets/131219987/604ae4c4-1351-4dde-8f16-05f061fed4dc)

### ... con una descripción larga sobre dicho contenido:Con nombre,sinopsis, descripción:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/906b75f4-b7c4-4769-9d6f-d5302138e548)

## I/O Redirection
### Dado que el output al archivo fue redirigido, no contamos con resultados a la vista, pero... 
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/a8786fb7-3aaa-49ee-b503-5083fd665702)
### ... Cada que se repiten el comando anterior, para anexarlos al archivo los resultados incluímos ">>" así:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/44862da1-5d5f-4b3d-9765-0c177323809f)
### o bueno quizá no resultó de primeras, pero esto es porque el archivo no existe, y si existiese, sería un archivo mucho más largo, ya que se extendería al último lo que hemos puesto de salida.. [continuará]

### Aquí observamos que se puede redirigir la salida standar, el caracter < procesa el contenido , y no se redirigió a otro archivo, lo cual veremos que no siempre sucede.
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/9bc1c8c4-1a36-4c67-98f3-40cdacbce1b0)

### Aquí por ejemplo, se redirigió el resultado a este archivo, y nos apareció de la manera que mostraremos a continuación :
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/9c89fb6e-0987-4e25-afa6-5e879dd4b3d9)

### Prosiguiendo:
### Con el comando ls -l | less nos aparece así , es muy importante porque permite que cualquier comando tenga una salida de desplazamiento.lsless"| less"
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/c46cc878-75a2-47ad-86cb-f95b848bf69e)


### Plus: Con tar tzvf name_of_file.tar.gz | less  podemos ver el directorio como un archivo en el sistema de linux targzip 
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/ee4ab919-0109-4f64-b1db-315f906f2bf0)

## Expansion

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/4f2bcda1-3e7a-4de4-ba11-af1da8fad5ea)

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/46a05fa3-8c47-42b9-b64e-951fb002e6d0)

![uando se anexan los resultados, los nuevos resultados se agregan al final de la archivo, lo que hace que el archivo sea más largodespués de comandos deusamos el comando para procesar el contenido de Podríamos redirigir la salida estándar a Otro archivo como este:sortfile_list.txt ](https://github.com/Fx2048/COMU_REDES/assets/131219987/a4a76585-407a-4ec9-a247-1e8894935153)

# Expresiones aritméticas usando operadores numéricos
![operacion 2+2](https://github.com/Fx2048/COMU_REDES/assets/131219987/f709aa15-8892-4c41-b9ec-928ad5847af2)

![-bash expression ](https://github.com/Fx2048/COMU_REDES/assets/131219987/da13e82e-0c25-4219-a45a-36e0ea74199f)

![operacion grande 75](https://github.com/Fx2048/COMU_REDES/assets/131219987/2658a1d2-f457-4246-93f5-b77412f84b72)

![Five divided by two equals 2](https://github.com/Fx2048/COMU_REDES/assets/131219987/52d607d4-a9fd-4d9e-b338-306378ed7445)

![with1 left over](https://github.com/Fx2048/COMU_REDES/assets/131219987/ed404ec9-af77-428e-817a-9e745769e8fd)
![Front-A-Back Front-B-Back Front-C-Back](https://github.com/Fx2048/COMU_REDES/assets/131219987/47d914e5-e210-400d-b0ae-f25fc98b7699)

![Number_1 Number_2 Number_3 Number_4 Number_5](https://github.com/Fx2048/COMU_REDES/assets/131219987/1137757c-0d2f-4f4d-abeb-c540207c801a)

![aA1b aA2b aB3b aB4b](https://github.com/Fx2048/COMU_REDES/assets/131219987/e47cb887-dda8-43a8-b51f-40693df6c86a)


![photos I](https://github.com/Fx2048/COMU_REDES/assets/131219987/b678a4be-b398-4797-a66b-c47852d64683)

![photos 2](https://github.com/Fx2048/COMU_REDES/assets/131219987/9c3619dd-73d7-4d06-b021-f5c8f3c09f51)


![user blues_soul](https://github.com/Fx2048/COMU_REDES/assets/131219987/c7aa6922-e798-4fce-832f-c8543c13295c)

con el comando me apareció así:
![printenv | less](https://github.com/Fx2048/COMU_REDES/assets/131219987/c8dcabc5-64cd-4d38-a02e-c1d41c0a7b5e)


![SUER](https://github.com/Fx2048/COMU_REDES/assets/131219987/56790b3d-a699-4d60-9e5b-1b3f9b5a2a62)
no aparece nada xd

![imPhotos file_list.txt snap sorted_file_list.txt user_space_report.txte](https://github.com/Fx2048/COMU_REDES/assets/131219987/532d0481-2f22-4558-a3df-c55921a11e31)

![ls -l $(which cp)](https://github.com/Fx2048/COMU_REDES/assets/131219987/22c909ea-5765-4013-94a1-c604caab8c89)

![file $(ls /usr/bin/* | grep bin/zip)](https://github.com/Fx2048/COMU_REDES/assets/131219987/96fcb854-e73d-4b4f-b215-05167f7cd81c)

![ls -l `which cp`](https://github.com/Fx2048/COMU_REDES/assets/131219987/10f25fac-2040-4dff-853e-94d15fe981de)

![echo this is a     teste](https://github.com/Fx2048/COMU_REDES/assets/131219987/a58d31a1-99d1-46bf-b375-ee952ef36409)

![echo The total is $100.00](https://github.com/Fx2048/COMU_REDES/assets/131219987/bb7be2c0-9671-428a-b34d-ff0bc8cb5c51)

![ls -l two words.txt](https://github.com/Fx2048/COMU_REDES/assets/131219987/e7303f48-c2c3-4a72-baa5-0883e6e4fe13)


![ls -l "two words.txt"](https://github.com/Fx2048/COMU_REDES/assets/131219987/104fb461-1a1b-4748-aa9d-4c3c18fe4b61)


![echo "$USER $((2+2)) $(cal)"](https://github.com/Fx2048/COMU_REDES/assets/131219987/7b6c131c-f1ac-44a0-8a37-b55bfc46710b)


![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/bd4a0537-5c22-43fb-9048-1a56ccfcb862)


![echo $(cal)](https://github.com/Fx2048/COMU_REDES/assets/131219987/5b1317a6-98bf-462a-a10d-25ed9559462d)


![echo "$(cal)"](https://github.com/Fx2048/COMU_REDES/assets/131219987/2235b2d9-c7a1-4e72-9b11-4e3cca2ca8f4)


![echo text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER](https://github.com/Fx2048/COMU_REDES/assets/131219987/d925b77c-44db-4997-90ea-cdb05edd7d89)

![echo "text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER"](https://github.com/Fx2048/COMU_REDES/assets/131219987/2ce46b01-8353-493a-bfd4-a26e425f14ad)

![echo 'text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER'](https://github.com/Fx2048/COMU_REDES/assets/131219987/31473c9b-6eed-4a71-9128-7c4b24e9c7df)


![echo "The balance for user $USER is: \$5.00"](https://github.com/Fx2048/COMU_REDES/assets/131219987/7cd567ac-63de-4893-b329-ad414a7c1acb)


![mv bad\&filename good_filename](https://github.com/Fx2048/COMU_REDES/assets/131219987/d77d39d6-99ec-465f-8fb5-a16702446234)


![ls -r](https://github.com/Fx2048/COMU_REDES/assets/131219987/0adcb38e-4bd9-4cd6-b55b-80a563075e14)


![ls - l ---fulltime-reverse -human-reandable-gfull time](https://github.com/Fx2048/COMU_REDES/assets/131219987/59730161-80c0-4095-b996-8dbe195df271)


![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/9a3cc11e-a547-4cef-8a5f-172fe81177cf)


## Permissions
Para mirar los permisos en un archivo, usamos comando de ls, dentro del programa bash, localizamos /bin directorio:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/233aedec-8885-4529-9115-87612a289e0f)
Aparecen las siguientes características:
El archivo "/bin/bash" es propiedad del usuario "raíz"
El superusuario tiene derecho a leer, escribir, y ejecute este archivo
El archivo es propiedad del grupo "root"
Los miembros del grupo "raíz" también pueden leer y Ejecute este archivo
Todos los demás pueden leer y ejecutar esto archivo

## Job control

## WRITING SHELL SCRIPTS 

## A Closer Look at Long Format Desde Ubuntu terminal en Window
