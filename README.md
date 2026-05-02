Sistema de solicitudes HTTP con Flask

Descripción

Este proyecto implementa una API REST desarrollada con Flask para gestionar recursos mediante solicitudes HTTP. Incluye operaciones CRUD (crear, consultar, actualizar y eliminar registros), validación de peticiones JSON, manejo de códigos de estado HTTP y consumo de una API externa de API Ninjas utilizando variables de entorno.

Los datos se almacenan temporalmente en memoria mediante un diccionario Python definido en bd.py.

Requisitos

Python 3.x

Visual Studio Code

Flask

requests

python-dotenv

Postman o Insomnia para pruebas

1. Instalación

Clonar o crear la carpeta del proyecto

Ubicar el proyecto en una carpeta local.

2. Instalar dependencias

py -m pip install Flask
py -m pip install requests
py -m pip install python-dotenv

3. Crear archivo .env

En la raíz del proyecto crear un archivo llamado .env con el siguiente contenido:

API_NINJAS_KEY=tu_api_key

4. Ejecutar el servidor
py main.py

Servidor local:
http://127.0.0.1:5000

Estructura del proyecto
SEMANA 1 HTTP/
│
├── bd.py
├── main.py
├── .env
└── README.md

Endpoints

| Método |      Endpoint      |        Descripción             |
|--------|--------------------|--------------------------------|
|   GET  |   /api/recursos      | Lista todos los registros |
|   GET  |   /api/recursos/<id> | Obtiene un registro por ID |
|  POST  |  /api/recursos      |    Crea un nuevo registro     |
|   PUT  |   /api/recursos/<id> | Actualiza un registro existente |
| DELETE | /api/recursos/<id> |         Elimina un registro      |
|   GET  |    /api/frase        |   Consume una API externa     |

Ejemplos de request y response
GET /api/recursos

Response

{
  "1": {
    "nombre": "Recurso 1"
  },
  "2": {
    "nombre": "Recurso 2"
  }
}

POST /api/recursos

Request

{
  "nombre": "Nuevo recurso"
}

Response — 201 Created

{
  "id": 3,
  "nombre": "Nuevo recurso"
}

GET /api/recursos/3

Response — 200 OK

{
  "nombre": "Nuevo recurso"
}

PUT /api/recursos/3

Request

{
  "nombre": "Recurso actualizado"
}

Response — 200 OK

{
  "nombre": "Recurso actualizado"
}

PUT /api/recursos/999

Response — 404 Not Found

{
  "error": "Recurso no encontrado"
}

DELETE /api/recursos/999

Response — 404 Not Found

{
  "error": "Recurso no encontrado"
}

GET /api/frase

Response

[
  {
    "quote": "Example quote",
    "author": "Example author",
    "category": "success"
  }
]

Códigos de estado HTTP utilizados

Código	    Significado
200  	    Solicitud exitosa
201 	    Recurso creado correctamente
400 	    Solicitud inválida o cuerpo no JSON
404 	    Recurso no encontrado

Pruebas realizadas

Las pruebas se realizaron con Postman verificando:

creación de registros sin enviar ID manualmente
actualización de registros existentes
intento de actualización de IDs inexistentes
eliminación de registros existentes
intento de eliminación de IDs inexistentes
respuestas en formato JSON válido

Notas de entrega
El almacenamiento es temporal en memoria, por lo que los datos se reinician al detener el servidor.
La API key se almacena en .env para evitar exponer credenciales dentro del código.
El proyecto fue desarrollado con fines académicos como práctica de solicitudes HTTP, Flask y consumo de APIs externas.