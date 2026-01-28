Nombre del proyecto  
qa-project-Urban-Grocers-app-es
Cohorte 31
Nelly Dominguez

Descripción del Proyecto:

El Proyecto se trató de comprobar cómo la aplicación Urban Grocers crea kits de productos, Se establecieron los siguientes endpoint para la automatizacion de pruebas para la creación de kit en Urban Grocers, especificamente, para el campo "name":
# URL_SERVICE 
# CREATE_USER_PATH = "/api/v1/users/"
# KITS_PATH = "/api/v1/kits/"

Instrucciones para ejecutar las pruebas:

•	Automatizar las pruebas desde esta lista de comprobación, cargar el código en GitHub y enviar el repositorio a revisión.

•	Api de Urban Grocers.

•	Tener instalados los paquetes pytest y request para ejecutar las pruebas.

•	Ejecuta todas las pruebas con el comando pytest.

Así mismo se ejecutaron las siguientes funciones para la ejecución de las pruebas:
# post_new_user(body)
# post_new_client_kit(kit_body, auth_token)
# get_kit_body(name)
# get_new_user_token()
# positive_assert(kit_body)
# negative_assert_code_400(kit_body)

Descripción de tecnologías utilizadas:

•	Pycharm Community Edition 2025.1.2.

•	Git Bash.

•	Github.

Se enlistaron las siguientes pruebas según requerimiento:
![img_1.png](img_1.png)

Así mismo se instalaron las librerías pip:
La ejecución del proyecto se apoyo con la documentación de la api
Se realizaron las importaciones de request, configuración y data






