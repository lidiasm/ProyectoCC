#### Entidades del proyecto.

* Mascotas: es la entidad protagonista del sistema. En ella se incluyen los aspectos relacionados con la recopilación de la información de las mascotas así como la búsqueda de animales basada en preferencias. Si bien el primer ámbito debe de ejecutarse periódicamente a diferencia de la consulta de mascotas, esta entidad se dividirá en dos subentidades:

  - Recopilar datos de mascotas: en esta subentidad se encuentran las funcionalidades relacionadas con la conexión con la API Petfinder y la recopilación de un conjunto de datos definidos como son el nombre, el tipo de animal, la raza, el tamaño, el género, la edad, el tipo de pelaje, el estado (encontrado, adoptable o adoptado), cómo se relaciona tanto con niños como con otros animales así como la organización en la que se encuentra.
  
  - Búsqueda de mascotas: esta subentidad se centra en la consulta de mascotas basada en una serie de preferencias establecidas. Por lo tanto los usuarios podrán buscar mascotas en base al tipo de animal, la edad, el género, el tamaño y si se relaciona bien con un entorno en el que se incluyen niños, gatos o perros.
  
* Estadísticas: es la entidad encargada de generar una serie de estadísticas concretas y almacenarlas en una base de datos para posteriormente ser visualizadas por los usuarios. Como en el caso anterior esta entidad se dividirá en dos subentidades puesto que la primera funcionalidad necesita ejecutarse cada cierto tiempo en relación con la obtención de los datos actualizados de mascotas. Por lo tanto las subentidades serán:

  - Generar estadísticas: en esta subentidad se encargará de generar los siguientes seis tipos de informes estadísticos.
  
    - Porcentaje para cada tipo de animal en adopción que sea capaz de relacionarse correctamente con niños. De este modo los usuarios podrán conocer qué tipo de mascota es la más adecuada para convivir con sus hijos.
    - Clasificar cada raza de perro en función del porcentaje que refleje su aptitud para convivir tanto con niños como con otros animales, ya sean perros o gatos. De este modo podremos comprobar qué razas de perros son las más amigables y capaces de convivir con otros seres distintos o no de su propia especie.
    - Clasificación de las razas de perro en base al porcentaje más alto de adopciones. De este modo podremos analizar qué razas de este tipo de animal son las favoritas.
    - Concentración del número de organizaciones orientadas a la adopción de mascotas por país. Con ello podremos analizar qué países cuentan con un mayor número de protectoras de animales.
    - Tipos de animales que se pueden encontrar en adopción ordenados en función del número de ejemplares que pertenezca a cada categoría. Así podremos conocer todos los animales que se pueden adoptar y cuáles son los grupos mayoritarios que se encuentran en adopción.
    - Clasificación de las diferentes etapas de la vida de un animal en función del porcentaje de adopción. Con esto se pretende conocer si las personas tienen mayor preferencia por adoptar un cachorro o prefieren un animal ya adulto.
    
  - Almacenar estadísticas: una vez se han generado los anteriores informes estadísticos, esta subentidad será la encargada de almacenarlos en la base de datos para que, posteriormente, puedan ser visualizados por los usuarios.
     