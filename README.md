# Data Collector Web App

Esta aplicación es un sistema de recopilación de datos construido con Flask y PostgreSQL. Los usuarios pueden ingresar su dirección de correo electrónico y su altura, y recibir estadísticas agregadas de la altura promedio de todos los usuarios registrados.

Este proyecto fue desarrollado como parte del curso *The Python Mega Course: Build 10 Real World Applications* y se creó para practicar Python y las bibliotecas utilizadas.

## Características
- **Registro de datos**: Los usuarios pueden registrar su correo electrónico y altura.
- **Estadísticas**: Calcula y muestra la altura promedio y el número de registros.
- **Notificaciones por correo**: Envía un correo electrónico al usuario con los datos ingresados y las estadísticas globales.

## Tecnologías Utilizadas
- **Backend**: Flask (Python)
- **Base de Datos**: PostgreSQL
- **Correo Electrónico**: SMTP para enviar correos
- **HTML**: Formularios y plantillas para la interfaz de usuario
- **Variables de Entorno**: Manejo seguro de credenciales con `dotenv`

## Requisitos Previos
1. Tener Python 3.6 o superior instalado.
2. Tener PostgreSQL instalado y configurado.
3. Crear una base de datos en postgres llamada `height_collector`
4. Crear un archivo `.env` con las siguientes variables:
   ```plaintext
   POSTGRES_USER=tu_usuario
   POSTGRES_PASSWORD=tu_contraseña
   FROM_EMAIL=tu_email@gmail.com
   FROM_PASSWORD=tu_contraseña_de_aplicación
   ```

## Configuración y Ejecución
### Paso 1: Clonar el repositorio

### Paso 2: Configurar un entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### Paso 3: Instalar las dependencias
```bash
pip install -r requirements.txt
```

### Paso 4: Inicializar la base de datos
Ejecuta el archivo `init_db.py` para crear las tablas necesarias:
```bash
python init_db.py
```

### Paso 5: Ejecutar la aplicación
Inicia el servidor Flask:
```bash
python app.py
```
La aplicación estará disponible en [http://localhost:5000](http://localhost:5000).

## Estructura del Proyecto
```plaintext
|-- app.py             # Archivo principal de la aplicación
|-- init_db.py         # Inicializa la base de datos
|-- send_email.py      # Módulo para enviar correos
|-- templates/         # Plantillas HTML
|   |-- index.html     # Formulario principal
|   |-- success.html   # Página de éxito
|-- static/            # Archivos estáticos (CSS, JS, imágenes)
|   |-- main.css       # Archivo CSS principal
|-- .env               # Variables de entorno (ignorado por Git)
```

## Dependencias

```plaintext
Flask
Flask-SQLAlchemy
python-dotenv
psycopg2-binary
```

## Contribución
Si deseas contribuir a este proyecto, realiza un fork del repositorio, crea una rama con tus cambios y envía un pull request.
