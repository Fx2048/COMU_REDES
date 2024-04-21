# COMANDOS EN LINUX

 A continuación se presentará la realización de trabajo ejecutado, con resultados mostrados en pantalla y con explicación:

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

 Cp command sirve para copiar archivos y directorios

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

 Interacción con los comandos iniciales de linux, por ejemplo, vemos 3 comandos distintos, , ls es un alias por el comando añadido de color=auto". 
 
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/25d58a56-02d7-44d5-becc-c3921dbb6be7)

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/055538c7-1348-47e1-9660-77007165bf82)

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/de4fe3c5-9a19-429a-a37d-f5ce1973104f)

 Which sirve para programas funcionales que pueden ejecutarse, no ni alias que son sustitutos de programas ejecutables reales.

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/b2652bf9-22d0-4ee4-9562-81782ad12871)

Aquí se extiende el recurso de ayuda con respecto a su contenido:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/d6e9c3fc-88d0-44d8-bbb6-f17b5cd1fda5)

Elementos opcionales son mutuamente excluyentes simbolizados por corchetes :

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/d6f681fd-fcd1-46ab-a04f-2543e1464536)

A veces puede que no encuentre --help la ayuda necesaria, dado que algunos programas no admiten la variable del comando original de help.

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/253e8c05-5b06-4970-80c0-593d503e0d65)

 Man sirve para llamar a manual en el comando, programa es el nombre del comando a visualizar...

![man](https://github.com/Fx2048/COMU_REDES/assets/131219987/604ae4c4-1351-4dde-8f16-05f061fed4dc)

... con una descripción larga sobre dicho contenido:Con nombre,sinopsis, descripción:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/906b75f4-b7c4-4769-9d6f-d5302138e548)

## I/O Redirection

Dado que el output al archivo fue redirigido, no contamos con resultados a la vista, pero... 

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/a8786fb7-3aaa-49ee-b503-5083fd665702)

 ... Cada que se repiten el comando anterior, para anexarlos al archivo los resultados incluímos ">>" así:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/44862da1-5d5f-4b3d-9765-0c177323809f)

 o bueno quizá no resultó de primeras, pero esto es porque el archivo no existe, y si existiese, sería un archivo mucho más largo, ya que se extendería al último lo que hemos puesto de salida.. [continuará]

Aquí observamos que se puede redirigir la salida standar, el caracter < procesa el contenido , y no se redirigió a otro archivo, lo cual veremos que no siempre sucede.

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/9bc1c8c4-1a36-4c67-98f3-40cdacbce1b0)

 Aquí por ejemplo, se redirigió el resultado a este archivo, y nos apareció de la manera que mostraremos a continuación :

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/9c89fb6e-0987-4e25-afa6-5e879dd4b3d9)

 Prosiguiendo:
Con el comando ls -l | less nos aparece así , es muy importante porque permite que cualquier comando tenga una salida de desplazamiento.lsless"| less"

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/c46cc878-75a2-47ad-86cb-f95b848bf69e)


 Plus: Con tar tzvf name_of_file.tar.gz | less  podemos ver el directorio como un archivo en el sistema de linux targzip 
 
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


Hemos tomado la siguiente expresión de echo this is a test 

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
Para ejecutar nuestro primer guión con sheel, procedemos con chmod, el 755 nos da permiso de lectura, escritura y ejecución, aclaración, con 700 , este script será privado.

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/85e76973-77b6-4619-ab0c-9fa492c30e73)

Con el siguiente comando veremos hello world en la pantalla.

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/1fc647ef-3579-460b-ae7b-5f3e4e9afd21)

Path es la lista de directorios, ejecutánndola como se observa en seguida:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/c834c2d6-d8f7-489a-ad76-7579617cd522)

Añadimos directory para ver el nombre de directorio que queremos adicionar:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/79d434a7-5fb3-4720-aba1-b409435742ae)

Si no hemos todavía creado un directorio especifico para programas , y un subdirectorio, añadimos:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/e2b987fe-42bc-4908-bd7d-090726d5c5be)

Si copiamos, movemos el script, en el nuevo directorio, ok! Vamos a ejecutar esto, donde , tendremos que reiniciar para encontrar como nuestra ruta elegida:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/e1051284-00fb-43cf-b9ec-03b0e0891951)


![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/b3f61db7-f5d6-49fd-a443-7f42859d0f99)



### Editing the Scripts We Already Have

Con los comandos bashprofile entre hashtag, son comentarios añadidos:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/0788efa7-8ee7-4592-97b7-b178a5e543cb)

En la cuarta línea, observamos  el comando compuesto if:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/3894cd17-830a-4900-a4bd-abe85432eaa2)

Estableceremos un archivo de inicio y ruta, para agregar al diretorio la ruta bash/bin

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/5a4cbc32-0c95-406c-a9dd-f87797387178)

Aquí indicamos que el contenido de PATH es disponible para procesos secundarios de export

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/201720d1-b7e1-4ff2-9a72-e4f7a1b6bc8c)

### ALIAS , crea un comando abreviado de otros más extensos, name es el nombre del comando, y value el texto a ejecutar siempre y cuando , name esté como comando:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/e0a02f79-f7cf-479e-b24f-b73ccdca2780)

Vamos a crear un alias llamado "l" y convertirlo en una abreviatura de El comando "ls -l". Nos moveremos a nuestro directorio de inicio y usaremos nuestro editor de texto favorito, abra el archivo y agregue esta línea hasta el final del archivo:.bashrc , Al agregar el comando al archivo, hemos creado un nuevo comando llamado "l" que ejecutará "ls -l".Usando esta técnica, podemos crear cualquier número de comandos personalizados para nos. Aquí hay otro para probar:alias.bashrc

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/4682d51f-effd-4697-bf72-e52e8ac5e67c)

Este alias crea un nuevo comando llamado "hoy" que mostrará La fecha de hoy con un buen formato.

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/313dc6d3-e685-47f9-8c99-95a53d20e0fd)

Podemos crear nuestros alias directamente en el archivo símbolo del sistema; sin embargo, solo permanecerán vigentes durante el sesión de shell actual. Por ejemplo:alias

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/d8ab4ca9-3d85-4ae5-ae09-a2dd3e28dd5f)


### Here Scripts

```
ESTRUCTURA DE UN FILE HTML:
<html>
<cabeza>
 <título>
 El título de tu página
 </título>
</cabeza>

<cuerpo>
 El contenido de tu página va aquí.
</cuerpo>
</html>
Con este comnado se puede  producir lo anterior contenido
sysinfo_page > sysinfo_page.html
```

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/b8b593cf-a53a-4eeb-a556-ce4a63b6930c)



### Command Substitution and Constants

Los caracteres "$( )" le dicen al shell, "sustituye los resultados de la comando cerrado", una técnica conocida como sustitución de comandos. En nuestro script, queremos que el shell inserte los resultados del comando que genera la fecha y hora actuales. El comando tiene muchas características y opciones de formato. Para verlos todos, probamos esto:date +"%x %r %Z"

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/5836911c-9e9a-42e1-b21d-62733e4eb06a)

### Some Real Work

La función mostrará el resultado del comando de tiempo de actividad. El comando uptime genera varios datos interesantes sobre el sistema, incluyendo el tiempo que el sistema ha estado "en funcionamiento" desde su última reiniciar, el número de usuarios y la carga reciente del sistema.show_uptime

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/7702f5a4-bf56-4161-8c58-99f4efa986c0)

Para obtener la salida del comando uptime en nuestra página HTML, codificaremos nuestro shell de esta manera, reemplazando nuestro código de stubbing temporal con el Versión terminada

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/1ff2f837-cf47-42c7-a90b-14ea101aeed9)

La función drive_space usará el comando df para proporcionar un Resumen del espacio utilizado por todos los sistemas de archivos montados.

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/96410c11-78b5-480d-af22-f65c31afea04)

En términos de estructura, la función es muy similar a la función show_uptime:drive_space

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/59ffe4cd-94c1-4bf1-809a-3350ff10c314)

La función mostrará la cantidad de espacio que cada uno usuario está usando en su directorio de inicio. Mostrará esto como una lista, ordenada en orden descendente por la cantidad de espacio utilizado.home_space

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/31576f94-988a-456e-aee1-518943d445d2)


Todavía no estamos listos para terminar la función. En Mientras tanto, mejoraremos el código stubbing para que produzca HTML válido:system_info

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/cd28f7c7-ee23-481b-b0eb-160670da6c6e)

### Flow Control - Part 1

El comando if es bastante simple en la superficie; Hace que Una decisión basada en el estado de salida de un comando. La sintaxis del comando es la siguiente:ififif donde commands es una lista de comandos. Esto es un poco confuso en A primera vista. Pero antes de que podamos aclarar esto, tenemos que ver cómo funciona el caparazón Evalúa el éxito o el fracaso de un comando.

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/8d3efccd-d229-4a41-bf84-37d0b27a9ec6)

Los comandos (incluidos los scripts y las funciones de shell que escribimos) emiten un valor al sistema cuando terminan, lo que se denomina estado de salida. Este valor, que es Un entero en el rango de 0 a 255, indica el éxito o el fracaso de la ejecución del comando. Por convención, un valor de cero indica éxito y cualquier Otro valor indica un error. El shell proporciona un parámetro que podemos usar para examinar el estado de salida. Aquí lo vemos en acción:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/d0b0c9f5-98af-4d53-a687-ccb4c2ed8253)

El shell proporciona dos comandos incorporados extremadamente simples que no hacen nada excepto terminar con un estado de salida cero o uno. El comando siempre se ejecuta correctamente y el comando siempre se ejecuta sin éxito:truefalse

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/fc4e27cd-58cf-4ef6-8ca7-f9c0108ba619)

Podemos usar estos comandos para ver cómo funciona la instrucción. Lo que realmente hace la declaración es Evalúe el éxito o el fracaso de los comandos:ifif

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/3fdb2734-2311-4fb4-adba-2c125652653c)

El comando se usa con mayor frecuencia con el comando para realizar decisiones de verdadero o falso. El comando es inusual en el sentido de que tiene dos formas sintácticas diferentes:testif

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/33ba90dc-59dc-45f2-bb8f-6d29101e307b)

El comando funciona de forma sencilla. Si el expression es verdadera, sale con un estado de cero; de lo contrario, sale con un estado de 1.testtest

La característica interesante de es la variedad de expresiones que podemos crear. He aquí un ejemplo:test
En este ejemplo, usamos la expresión " ". Esta expresión pregunta: "¿Es .bash_profile un archivo?" Si el expresión es verdadera, luego sale con un cero (indicando true) y el comando ejecuta el comando comando(s) después de la palabra . Si el expression es false, luego sale con un estado de one y el comando ejecuta el(los) comando(s) Siguiendo la palabra .-f .bash_profiletestifthentestifelse

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/90009d02-dcb6-4438-9fa1-9ba63ff0725d)


El punto y coma es un separador de comandos. Usarlo nos permite poner más de Un comando en una línea. Por ejemplo:
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/ce2c48b8-8f81-46b0-9b95-8056094861b3)



### Stay Out of Trouble

Crearemos el método siguiente script llamado . Introdúzcamoslo exactamente como está escrito.trouble.bash

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/15572a6b-4c8d-4cc0-bb31-24e16bb8708d)

Editemos el script para cambiar la línea 3 desde:

número=1
Para:

número=
y volvamoslo a ejecutar el script. Esta vez deberíamos Obtenga lo siguiente:

Cuando ejecutamos este script, debería generar la línea "El número es igual a 1" Porque, bueno, es igual a 1. Si no obtenemos lo esperado salida, necesitamos verificar nuestra escritura; Hemos cometido un error.number

y vuelva a ejecutar el script. Esta vez deberíamos Obtenga lo siguiente:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/15945470-1982-4f66-8094-fbeaf144b5b4)

Como podemos ver, se muestra un mensaje de error cuando ejecutamos el script. Podríamos pensar que al eliminar el "1" en la línea 3 creó un error de sintaxis en la línea 3, pero no fue así. Veamos el error Mensaje de nuevo:bash

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/95e60dee-b253-4d13-9fa0-4ecf0c37b8ae)

Podemos ver que está informando de la error y el error tiene que ver con "". Recordar Ese "" es una abreviatura de la construcción de shell. A partir de esto podemos determinar que el El error está ocurriendo en la línea 5, no en la línea 3../trouble.bash[[test

Primero, para ser claros, no hay nada malo con la línea 3. es una sintaxis perfectamente buena. A veces queremos establecer el valor de una variable en nada. Podemos confirmar la validez de esto probándolo en el comando línea:number=

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/421b8b5b-feb3-4a8c-9065-121ddd5713d0)




### Keyboard Input and Arithmetic

Para obtener información del teclado, usamos el comando. El comando toma la entrada del teclado y la asigna a un variable. He aquí un ejemplo:readread

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/c829a1e1-f07a-4642-9d48-bc0f378452f1)

Si no le damos al comando el nombre de un variable para asignar su entrada, utilizará la variable de entorno .readREPLY

El comando tiene varias opciones de línea de comandos. Los tres más interesantes son , y .read-p-t-s

La opción nos permite especificar un prompt que preceda a la función entrada del usuario. Esto ahorra el paso adicional de usar an para preguntar al usuario. Aquí está el ejemplo anterior reescrito para usar la opción:-pecho-p

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/829961d2-09bd-4334-bd08-29432cc84bc1)

La opción seguida de un número de segundos proporciona un Tiempo de espera automático para el comando. Esto significa que el comando se dará por vencido después de que el Número especificado de segundos si no se ha recibido ninguna respuesta del usuario. Esta opción podría usarse en el caso de un script que debe continuar (tal vez recurriendo a una respuesta predeterminada) incluso si el usuario no responde a las indicaciones. Aquí está la opción en acción:-treadread-t

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/23278ac8-43b3-431a-b614-3d5de4cebc5d)

La opción hace que no se muestre la escritura del usuario. Esto es útil cuando le pedimos al usuario que escriba una contraseña u otra Información confidencial.-s

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/fcabc0ed-95ba-43c0-910b-051a1319c21c)

¿Qué es un número entero? Eso significa números enteros como 1, 2, 458, -2859. Lo hace no números fraccionarios medios como 0.5, .333 o 3.1415. Para tratar con fracciones números, hay un programa separado llamado que proporciona una precisión arbitraria lenguaje de la calculadora.

Digamos que queremos usar la línea de comandos como una calculadora primitiva. Podemos Hazlo así:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/2e3f3a03-c05e-4aa8-8ee5-07d2f4e6cb28)

Cuando rodeamos una expresión aritmética con el doble paréntesis, el shell realizará la expansión aritmética.

Observe que se ignoran los espacios en blanco:


![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/a47acbde-a45e-40ad-b2b8-cd456ee7af96)

El shell puede realizar una variedad de aritméticas comunes (y no tan comunes) Operaciones. He aquí un ejemplo:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/5eed2458-6ea4-4925-bdb3-321bd68197e9)


### Flow Control - Part 2

Podemos construir este tipo de rama con múltiples declaraciones. En el siguiente ejemplo, evaluamos algunas entradas Del usuario:if
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/dfdf0ec3-1d75-4f6f-83d8-0b2ee96be0e4)

El comando tiene la siguiente forma:case


![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/037fdad5-455e-492a-95a2-03bc76af4cc4)

 Aquí hay un Ejemplo para mostrar cómo funciona esto:word| el patrón especial "" coincidirá cualquier cosa, por lo que se utiliza para detectar casos que no coincidían con los patrones anteriores. 
 
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/e1417f7a-5bbc-408f-aebf-825246439861)

Eso proporciona un comando incorporado llamado , que se puede usar para construir Un programa equivalente:case
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/7a371311-777d-496a-8461-136cc9fc9d86)

El comando tiene la siguiente forma:case


![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/afdec8d5-fadd-4e48-9a37-f0a45134c7fd)

case Ejecuta selectivamente instrucciones si coincide con un patrón. Podemos tener cualquier número de patrones y Declaraciones. Los patrones pueden ser texto literal o comodines. Podemos tener múltiples patrones separados por el carácter "". Aquí hay un Ejemplo para mostrar cómo funciona esto:word|

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/fee36fcf-32dd-4296-9004-3457098b2aa2)

El comando hace que un bloque de código sea ejecutado una y otra vez, siempre y cuando el estado de salida de un comando especificado sea verdadero. Aquí hay un ejemplo simple de un programa que cuenta de cero a nueve:while


![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/99f9ef0b-96f0-46d4-a185-743f80d578a8)

El comando funciona exactamente de la misma manera, excepto que el bloque de código se repite siempre que la salida del comando especificado status es false. En el siguiente ejemplo, observe cómo se ha cambiado la expresión dada al comando del ejemplo para lograr el mismo resultado:untiltestwhile

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/4099c2b2-ddf8-442a-aa10-490deb81d1ec)

En el siguiente ejemplo, usamos nuestro nuevo conocimiento de bucles y casos para construir un Aplicación simple basada en menús:El propósito del bucle en este programa es para volver a mostrar el menú cada vez que se haya completado una selección. El bucle Continúe hasta que la selección sea igual a 0, la opción "Salir". defendemos contra las entradas del usuario que no son opciones válidas con .until

![building a menu](https://github.com/Fx2048/COMU_REDES/assets/131219987/fbbe3ec7-b1af-41bc-a6ab-242f96088ab6)

Para que este programa se vea mejor cuando se ejecute, podemos mejorarlo de la siguiente manera: agregar una función que le pida al usuario que presione la tecla Intro después de cada selección se ha completado y borra la pantalla antes de que se muestre el menú. se muestra de nuevo. Aquí está el ejemplo mejorado:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/14f3f531-a2fc-4e27-bb93-07e56b65875e)



### Positional Parameters


La última vez que dejamos nuestro guión, se veía algo así:
Tenemos la mayoría de las cosas funcionando, pero hay varias características más que podemos agregar:

Deberíamos poder especificar el nombre del archivo de salida en la línea de comandos, así como establecer un valor predeterminado nombre del archivo de salida si no se especifica ningún nombre.

Ofrezcamos un modo interactivo que solicitar un nombre de archivo y advertir al usuario si el archivo existente y solicitar al usuario que sobrescriba eso.

Naturalmente, queremos tener una opción de ayuda que mostrará un mensaje de uso.
Todas estas características implican el uso de opciones y argumentos de línea de comandos. Para manejar opciones en la línea de comandos, usamos una función en el shell llamada parámetros posicionales. Los parámetros posicionales son una serie de variables ( a través de ) que contienen el contenido de la línea de comandos. $0$9

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/dc94b39c-ba48-460c-a12d-415ebf8f422d)


Imaginemos la siguiente línea de comandos:


![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/301ed4b4-3ad4-4ed7-a433-fbae1e7830bc)

Si se tratara de un script de shell bash, podríamos leer cada uno de ellos en la línea de comandos, ya que los parámetros posicionales contienen el atributo siguiente: some_program

$0 contendría "some_program"
$1 contendría "palabra1"
$2 contendría "word2"
$3 contendría "word3"

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/b70f7e1f-1a46-4826-9b8d-6536d351c0b6)

Hay un par de maneras de hacer esto. En primer lugar, podríamos simplemente Compruebe si contiene algo así: $1

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/ae544f52-d9c3-42ba-86be-2dc32d842dda)

En segundo lugar, el shell mantiene una variable llamada que contiene El número de elementos de la línea de comandos, además del nombre del comando (). $#$0

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/9817781a-89c4-4949-b58f-79ace2867df0)

Este es el código que usaremos para procesar nuestra línea de comandos:Este código es un poco complicado, así que tenemos que explicarlo.

Las dos primeras líneas son bastante fáciles. Establecemos la variable para que esté vacía. Esto indicará que el interactivo no se ha solicitado el modo. A continuación, establecemos la variable en contienen un nombre de archivo predeterminado. Si no se especifica nada más en la línea de comandos, Se utilizará este nombre de archivo. interactivefilename

Después de establecer estas dos variables, tenemos la configuración predeterminada, en caso de que el El usuario no especifica ninguna opción.

A continuación, construimos un bucle que hará un ciclo a través de todos los elementos de la línea de comandos y procese cada uno con . El detectará cada uno de ellos posible y procesarla en consecuencia.whilecasecase

Ahora viene la parte complicada. ¿Cómo funciona ese bucle? Se basa en la magia de .shift


![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/e2d85334-ea9e-4f1c-b31a-15cea8bc0e6e)

shift, por otra parte, es una orden interna de shell que opera en el parámetros posicionales. Cada vez que invocamos , "desplaza" todos los parámetros posicionales hacia abajo en uno. se convierte en , se convierte en , se convierte en , y así sucesivamente. Pruebe esto:shift$2$1$3$2$4$3

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/f8628a02-b263-407e-b915-caba988b5f13)


Tendremos que mover algunas cosas y agregar una función de uso para obtener Esta nueva rutina se integró en nuestro guión. También agregaremos algo de código de prueba a Comprobar que el procesador de línea de comandos funciona correctamente. Nuestro guión ahora se ve así:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/88456d9e-2a98-4f76-a1ae-3f1ea5b74dae)

El modo interactivo se implementa con el siguiente código:
rimero, verificamos si el modo interactivo está activado, de lo contrario no tenemos cualquier cosa que hacer. A continuación, le pedimos al usuario el nombre del archivo. Fíjemonos en la forma en que el prompt está redactado:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/b38d61fc-2c65-4e98-b6cc-5033de7344ec)








### Flow Control - Part 3

Ahora que hemos aprendido sobre los parámetros posicionales, es hora de cubrir el declaración de control de flujo restante, se usa para construir bucles. funciona así:forwhileuntilforfor

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/640d7128-381d-4cf6-8feb-e6373164e45b)


En esencia, asigna una palabra de la lista de palabras a la variable especificada, ejecuta los comandos y lo repite una y otra vez. y así sucesivamente hasta que se hayan agotado todas las palabras. He aquí un ejemplo:for
En este ejemplo, a la variable se le asigna la cadena "", entonces se ejecuta la instrucción, A continuación, se asigna a la variable la cadena "", y se ejecuta la instrucción, y así sucesivamente, hasta que todos los Se han asignado palabras en la lista de palabras.iword1echo "$i"iword2echo "$i"
Lo interesante de las muchas formas Podemos construir la lista de palabras. Se pueden utilizar todo tipo de expansiones. En En el siguiente ejemplo, construiremos la lista de palabras usando el comando sustitución:for
Aquí tomamos el archivo y contamos el número de palabras en el archivo y el número de caracteres en cada palabra..bash_profile
La variable shell contiene la lista de la línea de comandos Argumentos. Esta técnica se utiliza a menudo para procesar una lista de archivos en el archivo línea de comandos. Aquí hay otro ejemplo:"$@"

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/d3d73995-8f2f-4013-89ef-9ca62d0d01d8)

A continuación se muestra otro script de ejemplo. Este compara los archivos en dos directorios y enumera los archivos del primer directorio que faltan en el directorio segundo.

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/233a9108-9c6f-4f55-98cd-42bbbff816ec)

Pasemos ahora al verdadero trabajo. Vamos a mejorar la función para generar más información. Recordemos que nuestra versión anterior se veía Así:home_space

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/7e523b30-0c2f-472c-ae9a-d0d16b0be4e0)

Aquí está la nueva versión:



![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/01f2f4e3-01dc-40db-ba5d-cdfb514dab1f)

## Esta versión cierra automáticamente la terminal de UBUNTU:

```
 
#!/bin/bash

# cmp_dir - program to compare two directories

# Check for required arguments
if [ $# -ne 2 ]; then
    echo "usage: $0 directory_1 directory_2" 1>&2
    exit 1
fi

# Make sure both arguments are directories
if [ ! -d "$1" ]; then
    echo "$1 is not a directory!" 1>&2
    exit 1
fi

if [ ! -d "$2" ]; then
    echo "$2 is not a directory!" 1>&2
    exit 1
fi

# Process each file in directory_1, comparing it to directory_2
missing=0
for filename in "$1"/*; do
    fn=$(basename "$filename")
    if [ -f "$filename" ]; then
        if [ ! -f "$2/$fn" ]; then
            echo "$fn is missing from $2"
            missing=$((missing + 1))
        fi
    fi
done
echo "$missing files missing"

```
----Termima la sesión de la terminal de ubuntu-------




### Errors and Signals and Traps (Oh My!) - Part 1 

Es muy importante verificar el estado de salida de los programas a los que llamamos en nuestro Scripts. También es importante que nuestros scripts devuelvan un estado de salida significativo cuando terminen. Había una vez un administrador de sistemas Unix que escribió un script para un sistema de producción que contiene las siguientes 2 líneas de código:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/c3d0af8f-197d-429d-a24e-ec5d0a9c540f)

Hay varias formas en que podemos obtener y responder al estado de salida de un programa. En primer lugar, podemos examinar el contenido de la variable de entorno. contendrá el estado de salida del Último comando ejecutado. Podemos ver este trabajo con lo siguiente:$?$? En esta versión, examinamos el estado de salida del comando y si no es cero, imprimimos un mensaje de error en error estándar y Termine el script con un estado de salida de 1.cd

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/aafb70d4-1039-4a7f-9bf0-5013d21361a5)


Entonces, para verificar el estado de salida, podríamos escribir el script de esta manera:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/0ae81cf1-1d8f-4152-8147-8084bb2277b7)

Si bien esta es una solución funcional al problema, hay más métodos que nos ahorrarán algo de teclear. El siguiente enfoque que podemos intentar es Utilice la instrucción directamente, ya que evalúa el estado de salida de órdenes que se le dan.if

Usando , podríamos escribirlo de esta manera:if

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/f78e5cd2-a3f8-489a-9dbf-6c71f48eaf4b)

Dado que comprobaremos si hay errores a menudo en nuestros programas, tiene sentido para escribir una función que muestre mensajes de error. 

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/76d6c815-f427-4f5b-a202-3e30e7b0cbe1)

Finalmente, podemos simplificar aún más nuestro script usando AND y OR operadores de control. Para explicar cómo funcionan, aquí hay una cita de la página del manual:bash
"Los operadores de control && y || denotan listas AND y listas OR, respectivamente. Una lista AND tiene el formato
command2 se ejecuta si, y solo si, devuelve un estado de salida distinto de cero. El estado de salida de las listas AND y OR es el estado de salida del último comando ejecutado en la lista."command1

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/b33ff737-4ba9-4260-a72f-c5773f1086b3)

"Los operadores de control && y || denotan listas AND y listas OR, respectivamente. Una lista AND tiene el formato
command2 se ejecuta si, y solo si, devuelve un estado de salida distinto de cero. El estado de salida de las listas AND y OR es el estado de salida del último comando ejecutado en la lista."command1

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/521fb28b-0305-409a-aa33-09e91c5f7497)

De nuevo, podemos usar los comandos y para ver Este trabajo:truefalse

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/a1609e97-d84c-44ec-a2a2-e8f7732c4936)

Usando esta técnica, podemos escribir una versión aún más simple:



![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/a325e0d3-7b9c-421e-98c9-167146cbedb4)

Si no se requiere una salida en caso de error, incluso podemos hacer esto:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/c0661f68-2996-455f-a4ac-7d196f072d3e)

```

PROGNAME="$(basename $0)"

error_exit()
{

# ----------------------------------------------------------------
# Function for exit due to fatal program error
#   Accepts 1 argument:
#     string containing descriptive error message
# ----------------------------------------------------------------


  echo "${PROGNAME}: ${1:-"Unknown Error"}" 1>&2
  exit 1
}

# Example call of the error_exit function.  Note the inclusion
# of the LINENO environment variable.  It contains the current
# line number.

echo "Example of error with line number and message"
error_exit "$LINENO: An error has occurred."
```
-------------cierra el programa------------


### Errors and Signals and Traps (Oh My!) - Part 2

Después de iniciar este script, parecerá que se cuelga. En realidad, como la mayoría programas que parecen colgarse, en realidad está atrapado dentro de un bucle. En este caso, Está esperando que el comando devuelva una salida distinta de cero estatus, lo que nunca hace. Una vez iniciado, el script continuará hasta bash recibe una señal que lo detendrá. Podemos enviar una señal de este tipo escribiendo Ctrl-c, la señal llamada SIGINT (abreviatura de SIGnal INTerrupt). true

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/df7325d7-a123-46f5-b145-fd375b007f8d)

Este script procesa el archivo de texto especificado en la línea de comandos con el comando y Almacena el resultado en un archivo temporal. A continuación, pregunta al usuario si desea Imprime el archivo. Si el usuario escribe "y", el archivo temporal se pasa a El programa de impresión (sustituya por si no hay un impresora conectada al sistema).prlprlesslpr
Si bien necesita un nombre de archivo pasado en la línea de comandos, no verifica que haya recibido uno, y no comprueba que el archivo exista realmente. Pero el problema que queremos Lo que se centra aquí es que cuando el script termina, deja atrás el archivo temporal.
Las buenas prácticas dictan que eliminemos el archivo temporal cuando finalice el script. Esto es fácilmente Para ello, agregue lo siguiente al final del script:$TEMP_FILE

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/ddb76f6a-5e28-4aed-bd33-cf69a5e8cb53)

El comando nos permite ejecutar un comando cuando nuestro script recibe una señal. Funciona así:trap
"signals" es una lista de señales a interceptar y "arg" es un comando a ejecutar cuando se recibe una de las señales. Para nuestro script de impresión, podríamos manejar El problema de la señal de esta manera:

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/350ebabd-4df3-44fb-9102-c2165104fc7d)


 Podríamos ser inteligentes y usar ";" y poner múltiples comandos en el archivo string para obtener un comportamiento más complejo, pero francamente, es feo. Una mejor manera sería crear una función a la que se llame cuando queramos realizar cualquier acciones al final de un guión. Para nuestros propósitos, llamaremos a esta función .trapclean_up

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/f2df76e4-7f2d-475f-8f83-437f8b7d56c5)

El uso de una función de limpieza es una buena idea para nuestro manejo de errores rutinas también. Después de todo, cuando un programa termina (por la razón que sea), deberíamos limpiar después de nosotros mismos. Aquí está la versión terminada de nuestro programa con Manejo mejorado de errores y señales:

```
PROGNAME="$(basename $0)"

# Create a temporary file name that gives preference
# to the user's local tmp directory and has a name
# that is resistant to tmp race attacks

if [ -d "~/tmp" ]; then
  TEMP_DIR=~/tmp
else
  TEMP_DIR=/tmp
fi
TEMP_FILE="$TEMP_DIR/$PROGNAME.$$.$RANDOM"

usage() {

  # Display usage message on standard error
  echo "Usage: $PROGNAME file" 1>&2
}

clean_up() {

  # Perform program exit housekeeping
  # Optionally accepts an exit status
  rm -f "$TEMP_FILE"
  exit $1
}

error_exit() {

  # Display error message and exit
  echo "${PROGNAME}: ${1:-"Unknown Error"}" 1>&2
  clean_up 1
}

trap clean_up SIGHUP SIGINT SIGTERM

if [ $# != "1" ]; then
  usage
  error_exit "one file to print must be specified"
fi
if [ ! -f "$1" ]; then
  error_exit "file $1 cannot be read"
fi

pr $1 > "$TEMP_FILE" || error_exit "cannot format file"

read -p "Print file? [y/n]: "
if [ "$REPLY" = "y" ]; then
  lpr "$TEMP_FILE" || error_exit "cannot print file"
fi
clean_up
```
----------cietrra el programa-----------

n buen nombre de archivo ayudará a identificar quién escribió el archivo, pero no será totalmente predecible. En el script anterior, la siguiente línea de código creó El archivo temporal :$TEMP_FILE
La variable es dependiendo de la disponibilidad del directorio.

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/39ab2631-3af6-446a-99fa-4dab8486967b)

