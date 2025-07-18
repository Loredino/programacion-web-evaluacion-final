# Evaluación Final: Loredana Romano
Entrega de la evaluación final para el ramo de Programación Web

## Estructura del proyecto

El directorio app contiene el código del proyecto.

```
src
├── app
│   ├── main.py
│   ├── static
│   │   ├── css
│   │   │   ├── bootstrap.min.css
│   │   │   └── estilo.css
│   │   └── js
│   │       └── bootstrap.bundle.min.js
│   └── templates
│       ├── ejercicios
│       │   │   ├── 1.html
│       │   │   └── 2.html
│       │   ├── layout
│       │   │   └── base.html
│       └── menu.html
├── init-db.py
├── LICENSE
├── README.md
└── requirements.txt
```

## Endpoints
- Base: `http://localhost:5000`
- Ejercicio 1: `/ejercicio1`
- Ejercicio 2: `/ejercicio2`

## Iniciar y activar ambiente
Documentación oficial: [venv](https://docs.python.org/3/library/venv.html)
**Nota**: Se debe ingresar con la terminal a la carpeta **src**.
El ambiente debe ser iniciado antes de ejecutar el proyecto.
1. `python -m venv venv`
2.
    - `venv\Scripts\activate.bat` <- cmd
    - `venv\Scripts\activate.ps1` <- PowerShell

> Si PowerShell bloquea la ejecución, se debe permitir temporalmente con:
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`

## Desactivar ambiente
Para desactivar el ambiente se debe ejecutar: `deactivate`

## Instalación de dependencias
Para instalar pip revisar "[pip installation](https://pip.pypa.io/en/stable/installation/#installation)".

`pip install -r requirements.txt`

## MongoDB
Se espera que la instancia de mongo esté corriendo o sea accesible desde **localhost:27017** con el usuario por defecto sin contraseña.
En caso contrario, se debe configurar en **main.py:16**.

## Inicio del proyecto
Para iniciar el servidor de flask:
1. Entra al directorio app: `cd app`
2. Carga bd y colección de usuarios: `python init-db.py`
3. Inicia el proyecto: `flask --app main run --debug`
4. Abrir navegador en `http://localhost:5000`