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

Aquí imprimimos los argumentos de texto en salida standar de manera Echo this is  a test

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/4df29ef8-0904-47cd-bedb-acee152186ce)

Aquí,  el shell expande el "*" en otra cosa (en este caso, los nombres de los archivos en el archivo directorio de trabajo) antes de que el comando sea ejecutado.

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/75af8c0c-7ce7-4e3e-99a1-65301bb24246)

La siguiente manera también es otra forma de realizar un parthname expansion, donde obtenemos técnicas que empleamos en nuestras lecciones anteriores, Obtener un directorio sea desde ls, o el que veremos a continuación:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/9a05954a-258c-42b1-b1f6-9a100c2c9ce4)


por echo/usr/*/share podemos observar a través de neustro directorio principal

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/6d522a17-815e-4b1f-be09-7d49012c7672)

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/15adb02a-7b89-45f4-b839-cafb5b61828c)

Cuando se utiliza en el comienzo de una palabra, se expande en el nombre del directorio de inicio del usuario designado, o si no se nombra ningún usuario, el directorio principal del usuario actual:cd

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/66fe10ad-346b-49f9-9872-12e2003b4d92)

Si el usuario foo tiene una cuenta, entonces:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/60561c48-34a5-496d-916c-5f56593e975d)


En esta sección, cuando se anexan los resultados, los nuevos resultados se agregan al final de la archivo, lo que hace que el archivo sea más largodespués de comandos deusamos el comando para procesar el contenido de Podríamos redirigir la salida estándar a Otro archivo como este:sortfile_list.txt 

![uando se anexan los resultados, los nuevos resultados se agregan al final de la archivo, lo que hace que el archivo sea más largodespués de comandos deusamos el comando para procesar el contenido de Podríamos redirigir la salida estándar a Otro archivo como este:sortfile_list.txt ](https://github.com/Fx2048/COMU_REDES/assets/131219987/a4a76585-407a-4ec9-a247-1e8894935153)




### Expresiones aritméticas usando operadores numéricas

En esta parte, la expansión aritmética usa la forma de $((expression)) la cual veremos aplicada así:
La expansión aritmética solo admite números enteros (números enteros, sin decimales), pero puede realizar un buen número de operaciones diferentes.

![operacion 2+2](https://github.com/Fx2048/COMU_REDES/assets/131219987/f709aa15-8892-4c41-b9ec-928ad5847af2)
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/b1a49ea9-44c7-4bea-9bbe-23376219d044)


La expresión básica que requiere el terminal para correr expresiones matemáticas:

![-bash expression ](https://github.com/Fx2048/COMU_REDES/assets/131219987/da13e82e-0c25-4219-a45a-36e0ea74199f)

Los espacios no son significativos en las expresiones aritméticas y las expresiones pueden estar anidadas. Para Ejemplo, para multiplicar cinco al cuadrado por tres:

![operacion grande 75](https://github.com/Fx2048/COMU_REDES/assets/131219987/2658a1d2-f457-4246-93f5-b77412f84b72)

A continuación, se muestra un ejemplo en el que se utilizan los operadores de división y resto. Observe el efecto de División de enteros:

![Five divided by two equals 2](https://github.com/Fx2048/COMU_REDES/assets/131219987/52d607d4-a9fd-4d9e-b338-306378ed7445)


 Ahora, podemos crear Varias cadenas de texto de un patrón que contiene llaves. He aquí un ejemplo:
 ![Front-A-Back Front-B-Back Front-C-Back](https://github.com/Fx2048/COMU_REDES/assets/131219987/47d914e5-e210-400d-b0ae-f25fc98b7699)

  A continuación, se muestra un ejemplo con un rango de números enteros:

![Number_1 Number_2 Number_3 Number_4 Number_5](https://github.com/Fx2048/COMU_REDES/assets/131219987/1137757c-0d2f-4f4d-abeb-c540207c801a)

La aplicación más común es hacer listas de archivos o directorios que se van a crear, por lo tanto , Las expansiones de llaves se pueden anidar:

![aA1b aA2b aB3b aB4b](https://github.com/Fx2048/COMU_REDES/assets/131219987/e47cb887-dda8-43a8-b51f-40693df6c86a)

Ahora organizaremos en años y meses una serie de directorios nombrados en formato numérico, ordenado cronológicamente, pudiendo escribir un archivo completo listo de directorios, minimizando la digitación,siguiendo este comando:

![photos I](https://github.com/Fx2048/COMU_REDES/assets/131219987/b678a4be-b398-4797-a66b-c47852d64683)

Examinamos con ls:

![photos 2](https://github.com/Fx2048/COMU_REDES/assets/131219987/9c3619dd-73d7-4d06-b021-f5c8f3c09f51)

Expandiremos parámetros de la siguiente manera: Invocamos mediante  la revelación del contenido del usuario con el comando:

![user blues_soul](https://github.com/Fx2048/COMU_REDES/assets/131219987/c7aa6922-e798-4fce-832f-c8543c13295c)

con el comando me apareció así:

![printenv | less](https://github.com/Fx2048/COMU_REDES/assets/131219987/c8dcabc5-64cd-4d38-a02e-c1d41c0a7b5e)

 Si escribimos mal un patrón, el expansión no se llevará a cabo y el comando echo simplemente mostrará el error patrón. 
 
![SUER](https://github.com/Fx2048/COMU_REDES/assets/131219987/56790b3d-a699-4d60-9e5b-1b3f9b5a2a62)

La sustitución de comandos nos permite usar la salida de un comando como una expansión:

![imPhotos file_list.txt snap sorted_file_list.txt user_space_report.txte](https://github.com/Fx2048/COMU_REDES/assets/131219987/532d0481-2f22-4558-a3df-c55921a11e31)

O de esta manera opcionalmente:
![ls -l $(which cp)](https://github.com/Fx2048/COMU_REDES/assets/131219987/22c909ea-5765-4013-94a1-c604caab8c89)

En esta parte los pipelines se convirtieron en lista de argumentos del comando de la lista, Es una sintax alternate para sustitución de comando en viejos programas de shell donde es soportado dentro.Su uso usa comillas inversa en lugar del signo de dólar y paréntesis:bash
![file $(ls /usr/bin/* | grep bin/zip)](https://github.com/Fx2048/COMU_REDES/assets/131219987/96fcb854-e73d-4b4f-b215-05167f7cd81c)


Hemos tomado la siguiente expresión de echo this is a test para 

![echo this is a     teste](https://github.com/Fx2048/COMU_REDES/assets/131219987/a58d31a1-99d1-46bf-b375-ee952ef36409)

En el primer ejemplo, la división de palabras por parte del shell eliminó el espacio en blanco adicional en la lista de argumentos del comando echo. En el segundo ejemplo, el parámetro expansion sustituyó el valor de "$1" por una cadena vacía porque era un variable indefinida. El shell proporciona un mecanismo llamado quoting to suprimir selectivamente las expansiones no deseadas

![echo The total is $100.00](https://github.com/Fx2048/COMU_REDES/assets/131219987/bb7be2c0-9671-428a-b34d-ff0bc8cb5c51)


 Visualizamos a continuación dos argumentos separados en lugar del único argumento deseado:two words.txt:
![ls -l two words.txt](https://github.com/Fx2048/COMU_REDES/assets/131219987/e7303f48-c2c3-4a72-baa5-0883e6e4fe13)

Al usar comillas dobles, podemos detener la división de palabras y obtener el resultado deseado; Además, incluso puede reparar el daño

![ls -l "two words.txt"](https://github.com/Fx2048/COMU_REDES/assets/131219987/104fb461-1a1b-4748-aa9d-4c3c18fe4b61)



![echo "$USER $((2+2)) $(cal)"](https://github.com/Fx2048/COMU_REDES/assets/131219987/7b6c131c-f1ac-44a0-8a37-b55bfc46710b)
En nuestro ejemplo anterior, vimos Cómo la división de palabras parece eliminar espacios adicionales en nuestro texto

sin comillas Los espacios, tabulaciones y saltos de línea no se consideran parte del texto. Solo sirven como separadores. Dado que separan las palabras en diferentes argumentos, nuestro ejemplo La línea de comandos contiene un comando seguido de cuatro argumentos distintos. Si añadimos Comillas dobles: 

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/bd4a0537-5c22-43fb-9048-1a56ccfcb862)

Veremos una línea de comandos con un argumento que Incluye los espacios incrustados y las nuevas líneas aquí:
![echo $(cal)](https://github.com/Fx2048/COMU_REDES/assets/131219987/5b1317a6-98bf-462a-a10d-25ed9559462d)


![echo "$(cal)"](https://github.com/Fx2048/COMU_REDES/assets/131219987/2235b2d9-c7a1-4e72-9b11-4e3cca2ca8f4)

Cuando necesitamos suprimir todas las expansiones, usamos comillas simples. Aquí hay una comparación de Sin comillas, comillas dobles y comillas simples:

![echo text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER](https://github.com/Fx2048/COMU_REDES/assets/131219987/d925b77c-44db-4997-90ea-cdb05edd7d89)


podemos preceder a un carácter con una barra diagonal inversa, que en este contexto se denomina carácter de escape. Frecuentemente Esto se hace entre comillas dobles para evitar selectivamente una expansión:

![echo "The balance for user $USER is: \$5.00"](https://github.com/Fx2048/COMU_REDES/assets/131219987/7cd567ac-63de-4893-b329-ad414a7c1acb)

Para incluir un carácter especial en un nombre de archivo podemos a esto:

![mv bad\&filename good_filename](https://github.com/Fx2048/COMU_REDES/assets/131219987/d77d39d6-99ec-465f-8fb5-a16702446234)


Aquí hay un truco de la barra invertida, cuya utilidad reside en los nombres de opciones largos, que comienzan con dos guiones, , lo sisguientes incluyen man, hay dos formas ,la larga o la corta.
![ls -r](https://github.com/Fx2048/COMU_REDES/assets/131219987/0adcb38e-4bd9-4cd6-b55b-80a563075e14)

El uso de las opciones de formato largo puede hacer un solo comando línea muy larga. Para combatir este problema, podemos usar una barra invertida para obtener el shell para ignorar un carácter de nueva línea como este:

![ls - l ---fulltime-reverse -human-reandable-gfull time](https://github.com/Fx2048/COMU_REDES/assets/131219987/59730161-80c0-4095-b996-8dbe195df271)

Esta es otra manera de usar la barra invertida:
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


### si quisiéramos establecer que el propietario tenga permiso de lectura y escritura, pero Si queríamos mantener el archivo privado de los demás, haríamos:some_file

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/f144ddec-864a-4662-8787-7f5c45c13b04)


con el siguiente comando ingresamos al superuser el cual nos pedirá una contraseña, y para salir solo ejecutamos suexit

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/24ea10c6-bae1-4d16-a9f4-599e1674aa41)

O de la siguiente manera, para ejecutar un comando como superusuario, el comando deseado simplemente está precedido con el comando, también se puede acceder, por ejemplo: Al usuario se le solicita su propia contraseña en lugar de la del superusuario:susudosudosudo

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/e8921eec-9289-49e5-845d-c394b7f88862)

En otro caso, algunas distribuciones establecen la contraseña de la cuenta de root lo que hace imposible iniciar sesión como usuario root. Todavía es posible un shell raíz with usando la opción "-i": sudo

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/e4e6e1bb-a191-4a3b-8715-d4ed1e0a5157)

Para cambiar propiedad de archivos, es imprescindible contar con la clave de seguridad para acceder al modo privilegios de superusuario, ya que es necesario contar con autorización suya para gestionar el procedimiento.
y es por ello que antecede a la solicitud el comando sudochown
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/8caf0825-515f-4ef2-a37a-513aaf4f601d)

Adicional a ello, se establece una forma de cambiar la propiedad de grupo de un archivo o directorio:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/f7270fb8-0371-46d5-9b85-f078cc597c41)

En la imagen anterior, cambiamos la propiedad del grupo de su grupo anterior a "new_group". Debemos ser el propietario del archivo o directorio para realizar un archivo .some_filechgrp


## Job control
### Hay un pequeño programa suministrado con el sistema X Window llamado que muestra un gráfico que representa la carga del sistema que podemos ejecutar escribiendo xload

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/c8b8759a-97e6-4ea5-afb0-65dfdaef8a3c)

Para ejecutar un programa en segundo plano aplicamos xload:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/e9cae98d-83b3-4caf-9bbb-4424434dccf3)

Si nos olvidamos de escribir completo, no hay de qué preocuparnos, ya que con xloadgb tabién es posble:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/f5e0235b-d662-46cc-8049-aa86ec3ba30a)

Aplicando por otro lado, jobsps tenemos una lista de procesos que hemos puesto en marcha, así:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/15d2e249-f391-4c1b-ac6d-18bce2747aee)

luego de haber identificado que hay un proceso que es incorrecto y no debería ir en nuestra lista, corrijamos con el comando xload &jobskill %1xload &pskill 1293

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/6dd95209-6634-470e-b35f-e9a81a59ce89)

el siguiente comando imprime una lista de las señales que admite:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/a2f3eb4c-cb3b-4319-aaea-4e06c0f41340)

Ahora, pasaremos  a obtener el id del proceso para terminar: con ps
Emitiendo un comando para ese IDP con kill
y si no se termina, porque ignora la señal, seguiremos enviando estas solicitudes de manera más estricta para que termine en una de ellas.
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/cdcec7d4-dcf3-4b97-aa1d-8c5f44a28bb3)

Emitiremos una señal SIGTERM al programa problemático, usando una señal number en lugar de la name signal, pspsgrepkillkillkill
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/123cf947-2da6-4f4b-ae2e-fdcc94453a70)

Y ahora, si el proceso no acaba, como habíamos dicho previamente, forzaremos con SIGKILL signal:
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/daec1ccf-c50d-472b-bfb5-2ab36208f459)


## WRITING SHELL SCRIPTS 
### Writing Our First Script and Getting It to Work
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/85e76973-77b6-4619-ab0c-9fa492c30e73)

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/1fc647ef-3579-460b-ae7b-5f3e4e9afd21)


![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/c834c2d6-d8f7-489a-ad76-7579617cd522)


### Editing the Scripts We Already Have
### Here Scripts
### Variables
### Command Substitution and Constants
### Shell Functions
### Some Real Work
### Flow Control - Part 1
### Stay Out of Trouble
### Keyboard Input and Arithmetic
### Flow Control - Part 2
### Positional Parameters
### Flow Control - Part 3
### Errors and Signals and Traps (Oh My!) - Part 1
### Errors and Signals and Traps (Oh My!) - Part 2
