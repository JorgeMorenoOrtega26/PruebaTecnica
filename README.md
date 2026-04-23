## PruebaTecnica

# Ejecución de las pruebas:

Las pruebas deben ser ejecutadas mediante pytest, con una sintaxis como la siguiente:
pytest .\tests\Web\test_loginKO.py

Todo test ejecutado creara en la raíz de la carpeta un fichero HTML con los resultados de la prueba en el fichero "report.html"

# Decisiones tomadas

He optado por la mejor organización del proyecto para que la legibilidad tanto del proyecto como del código sea la más eficiente posible, he intentado en la medida de lo posible no reutilizar constantemente métodos repetitivos en cada test como es el caso del login en la página web, he utilizado un config file para poder lanzar las pruebas simplemente especificando el nombre del fichero sin preocuparse de parametros adicionales, además, he utilizado checks constantes en las pruebas para hacer los tests robustos.

# Mejoras a tomar

- Organización por POM
- Integración de pruebas en pipelines
- Externalizar los datos sensibles, como usuarios, correos o api keys en ficheros externos
- Modificar los locators por otros más robustos para disminuir la posibilidad de fallos, como data-testid
