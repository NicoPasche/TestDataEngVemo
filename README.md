# TestDataEngVemo
Python Challenge Pasante
Objetivo: Desarrollar una herramienta ETL (Extract, Transform, Load) para mostrar información sobre 
los países del mundo.
Tareas Backend:
1. Configurar el entorno necesario para un proyecto en Python.
2. Usar SQLAlchemy, o cualquier ORM de tu preferencia, para establecer una interacción con una 
base de datos relacional.
3. Crear una base de datos destinada a almacenar la información de los países. Se debe definir un 
modelo de datos que incluya los siguientes campos: Nombre, Capital, Moneda, Continente, 
Lenguaje, Población y Bandera.
4. Recopilar datos sobre los países de la API disponible en https://restcountries.com/v3.1/all .
5. Realizar la transformación necesaria de los datos obtenidos para producir un archivo de salida en 
formato Excel (.xlsx) con las siguientes características:
A. Una hoja llamada "Paises" que liste todos los países con los campos mencionados.
B. Una hoja llamada "Metricas" con gráficos y/o KPIs que consideres relevantes.
6. Cargar la lista de países en la base de datos creada y configurar un sistema que envíe un correo 
electrónico diario con el archivo Excel adjunto.
Aclaraciones:
1. Cualquier mejora adicional que se realice más allá del alcance del proyecto propuesto debe estar 
adecuadamente documentada con docstrings para su correcta interpretación.
Entregables:
1. Enlace a GitHub con el código del proyecto y el script de creación de la base de datos relacional.
2. Un ejemplo del archivo Excel de salida.
