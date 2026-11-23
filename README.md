# Mi Blog

Blog web desarrollado con Django como entrega final del curso de Python. Permite registrarse, iniciar sesión y publicar posts con imagen.

## Tecnologías

- Python
- Django
- Bootstrap 5
- SQLite
- Pillow
- python-decouple

## Funcionalidades principales

- Listado y detalle de posts
- Crear, editar y eliminar posts desde la interfaz web
- Carga de imagen en los posts (el post se ve bien aunque no tenga imagen)
- Registro, inicio y cierre de sesión de usuarios
- Rutas protegidas: solo usuarios con sesión iniciada pueden crear posts, y solo el autor puede editarlos o eliminarlos
- Panel de administración de Django

## Instalación

1. Clonar el repositorio:

   ```
   git clone https://github.com/Gimenez-thomi/blog-django.git
   cd blog-django
   ```

2. Crear y activar el entorno virtual:

   En Windows (PowerShell):

   ```
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

   En macOS / Linux:

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instalar las dependencias:

   ```
   pip install -r requirements.txt
   ```

4. Crear el archivo de variables de entorno copiando el de ejemplo:

   En Windows (PowerShell):

   ```
   copy .env.example .env
   ```

   En macOS / Linux:

   ```
   cp .env.example .env
   ```

   Después abrir `.env` y reemplazar `SECRET_KEY` por una clave propia.

5. Aplicar las migraciones:

   ```
   python manage.py migrate
   ```

6. Crear un superusuario (necesario para entrar al panel de administración):

   ```
   python manage.py createsuperuser
   ```

7. Iniciar el servidor:

   ```
   python manage.py runserver
   ```

La aplicación queda disponible en http://127.0.0.1:8000/ y el panel de administración en http://127.0.0.1:8000/admin/.

## Cómo probar el proyecto

El repositorio no incluye la base de datos (`db.sqlite3`) ni la carpeta `media/`, así que el proyecto arranca vacío. Para probarlo:

1. Registrarse desde el botón "Registrarse" (o iniciar sesión con el superusuario).
2. Crear un post desde "Nuevo post", con y sin imagen.
3. Editar y eliminar el post desde su página de detalle.
4. Cerrar sesión y comprobar que, como visitante, no se puede entrar a `/posts/nuevo/` (redirige al login).

## Autor

Thomas Gimenez - Gimenez-thomi