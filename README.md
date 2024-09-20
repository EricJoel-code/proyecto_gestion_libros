# Proyecto de Gestión de Libros con Django

Este es un proyecto simple de una página web para gestionar libros (CRUD) donde los usuarios pueden agregar, eliminar, actualizar y listar libros. El proyecto está construido con Django en un entorno virtual.

## Características

- **Agregar libros**: Los usuarios pueden ingresar información sobre nuevos libros.
- **Listar libros**: Se muestra una lista de todos los libros agregados.
- **Actualizar libros**: Los usuarios pueden editar la información de los libros existentes.
- **Eliminar libros**: Los usuarios pueden eliminar libros de la lista.

## Requisitos Previos

- **Python 3.x**: Asegúrate de tener Python instalado en tu sistema.
- **Virtualenv**: Para crear y gestionar entornos virtuales.
- **Django**: El framework web utilizado para este proyecto.
- **Pillow** Para manejar imágenes

## Instalación

1. Clonar el repositorio (cuando lo hayas subido a GitHub):
    ```bash
    git clone https://github.com/EricJoel-code/proyecto_gestion_libros.git
    ```

2. Crear y activar un entorno virtual:
    ```bash
    python -m venv env
    source env/bin/activate  # Para Linux/macOS
    env\Scripts\activate  # Para Windows
    ```

3. Realizar las migraciones de la base de datos:
    ```bash
    python manage.py migrate
    ```

4. Iniciar el servidor:
    ```bash
    python manage.py runserver
    ```

5. Acceder al proyecto desde el navegador en: `http://127.0.0.1:8000/`.

## Uso

Una vez que el servidor esté en funcionamiento, podrás realizar las siguientes acciones:

- **Agregar** un nuevo libro.
- **Ver** la lista de todos los libros disponibles.
- **Actualizar** la información de un libro.
- **Eliminar** un libro de la lista.

## Estado Actual del Proyecto

- El CRUD de libros está en progreso.
- Se están añadiendo nuevas funcionalidades y mejorando la estructura del proyecto.
- Se agrego el registro e inicio de sesion de usuarios
- Se agrego el ingreso de libros

## Tecnologías Utilizadas

- **Django**: El framework principal para el desarrollo del backend.
- **SQLite**: Base de datos utilizada por defecto en Django (puede cambiarse en futuras versiones).
- **HTML/CSS**: Para la interfaz básica.

## Próximas Actualizaciones

- Validaciones en los formularios actualización de libros.
- Estilización de la interfaz con Bootstrap o CSS personalizado.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas colaborar, por favor abre un issue o crea un pull request.

