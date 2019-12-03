install:
	# Instala y crea un entorno virtual con Python 3.
	pipenv install --three
	# Instala las dependencias necesarias para la aplicación en el entorno virtual.
	pipenv run pip install -r requirements.txt 
	
test:
	# Ejecuta los tests de la clase Mascotas y de la clase de su API REST.
	pipenv run python -m pytest tests/test_mascotas.py tests/test_mascotas_rest.py
	# Tests de covertura para la clase Mascotas y la clase de su API REST.
	pipenv run python -m pytest --cov=mascotas --cov=mascotas_rest tests/
	
start:
	# Inicio del servidor Green Unicorn. Para ello se realizan una serie de pasos:
		# 1) Cambio al directorio del módulo "mascotas" donde se encuentran las clases
		#			de la lógica de la aplicación y del microservicio.
		# 2) Escribe en el directorio del módulo mascotas un fichero con el identificador del proceso
		# 		asociado al servidor. Esto nos será de utilidad cuando deseemos terminar su ejecución sin 
		# 		utilizar un gestor de procesos adicional.
		# 3) Con la opción "-D" evitamos que el terminal se quede bloqueado por la ejecución del servidor.
		# 4) Con la opción "-b" especificamos el puerto en el que se atenderán las peticiones.
		#			Por razones de seguridad este puerto se establecerá mediante una variable de entorno que deberá 
		#			estar creada antes de ejecutar esta orden.
	pipenv run gunicorn --chdir src/mascotas/ mascotas_rest:app -p pid_gunicorn.pid -D -b :${PORT}

stop:
	# Fin de la ejecución del proceso asociado al servidor Gunicorn. Para ello se hará uso del comando 
	# 	'kill', el cual solo necesita el identificador de un proceso para terminar su ejecución.
	#		Como se comentaba anteriormente, este ID se encuentra en el fichero "pid_gunicorn.pid".
	pipenv run kill `cat src/mascotas/pid_gunicorn.pid`

	