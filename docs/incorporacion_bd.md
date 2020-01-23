#### Incorporación del almacén de datos.

Tal y como se comentó anteriormente, se va a utilizar como almacén de datos **MongoDB** local, en particular haré uso de la biblioteca especial para esta base de datos escrita en *Python* denominada ***pymongo***. Para integrarla en mi proyecto utilizaré el mecanismo de *inyección de dependencias* de modo que se implemente una única clase específica en la que se desarrollen las diferentes operaciones que se pueden realizar en la base de datos, como añadir elementos, obtener uno en particular, entre otros. Posteriormente, se incluirá un atributo en cada una de las clases de la lógica de la aplicación, como es la clase *Mascotas* y de esa forma se le pasará a su constructor un argumento que será un objeto de la clase asociada a la base de datos ya inicializado. De este modo inyectamos en cada clase de la lógica de la aplicación un objeto de la base de datos con el fin de aportar cierta independencia entre el almacén de información y las clases del proyecto.

Para añadir el almacén de datos escogido de forma local, en primer lugar, deberemos instalar la biblioteca mencionada anteriormente y configurar tanto una base de datos como un usuario con el que acceder a ella mediante la *shell de mongo*. Una vez realizado este proceso ya podemos construir la variable de entorno `MONGODB_URI` necesaria para poder conectarnos a la base de datos que acabamos de crear y configurar. Esta variable es **imprescindible** para que el microservicio disponga de un almacén de datos.

Los siguientes cambios que se han producido han consistido en añadir a *mongo* como servicio tanto en **Travis** como en **CircleCI**. En este último, además, se debe añadir una imagen adicional en la que esté instalada *MongoDB*. En mi caso he utilizado aquella que se encuentra disponible en la propia herramienta: `circleci/mongo:latest`. Del mismo modo, en ambos casos, se ha añadido como **variable de entorno encriptada la URI a la base de datos local** para poder realizar los tests de la clase en la que se encuentran las operaciones de esta.

En relación a las herramientas de despliegue simplemente se ha añadido la clase de la base de datos para copiarla dentro del contenedor y tras construir el contenedor se deberá pasar una variable de entorno más denominada `MONGODB_URI` donde se encuentre la dirección con la que se llevará a cabo la conexión al almacén de datos. Este aspecto en **Heroku** se lleva a cabo de forma distinta puesto que, en primer lugar, la base de datos debe ser remota. Para ello he utilizado la plataforma [***MongoDB Atlas***](https://www.mongodb.com/cloud/atlas) y he seguido los pasos descritos a continuación:

* Nos damos de alta en la plataforma y a continuación creamos un nuevo *cluster* donde alojar la base de datos.
* Escoger el proveedor del servicio en la nube así como la región en la que se encuentra el servidor. En mi caso he optado por establecer los valores por defecto que definen un plan gratuito.
* Una vez establecida esta configuración podemos crear la base de datos, que en mi caso se denomina *Petfinder* así como un usuario para acceder a ella.
* Por último podremos crear en dicho almacén de datos una colección donde almacenar las mascotas, que en mi caso se llama *mascotas*.

Al finalizar el proceso podemos comprobar en la siguiente captura el estado de la base de datos remota que ha sido creada junto con la única colección que se ha registrado.

![MongoDB Atlas.](https://github.com/lidiasm/ProyectoCC/blob/master/docs/imgs/MongoDB%20Atlas.png)

Tras crear y configurar el almacén de datos basta con obtener la *URI* de la base de datos remota y añadirla como variable de entorno a **Heroku** mediante su interfaz dentro de la opción *Settings/Config Vars*. Por último, se han añadido las dependencias necesarias para instalar la librería *pymongo* en el fichero `docker_requirements.txt` de modo que en todas las futuras construcciones del contenedor se instalen las librerías necesarias para ejecutar el microservicio.