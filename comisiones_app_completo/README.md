# Plataforma de Comisiones de Trabajo Marinas de España

Esta es una aplicación web desarrollada con Flask para la gestión de comisiones de trabajo en el sector marítimo español. La plataforma permite la creación de comisiones, gestión de miembros, propuesta y votación de temas, subida de documentos, comentarios y programación de reuniones.

## Características principales

- Sistema de autenticación de usuarios con aprobación por administrador
- Gestión de comisiones con imágenes
- Sistema de aprobación de miembros
- Propuesta y votación de temas
- Gestión de patrocinadores
- Subida de documentos
- Sistema de comentarios
- Programación de reuniones

## Requisitos

- Python 3.8 o superior
- PostgreSQL (para producción)
- SQLite (para desarrollo)

## Instalación local

1. Clona este repositorio:
   ```
   git clone https://github.com/tu-usuario/comisiones-app.git
   cd comisiones-app
   ```

2. Crea un entorno virtual e instala las dependencias:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Configura las variables de entorno:
   ```
   cp .env.example .env
   ```
   Edita el archivo `.env` con tus configuraciones.

4. Inicializa la base de datos:
   ```
   flask db init
   flask db migrate -m "initial migration"
   flask db upgrade
   ```

5. Crea un usuario administrador:
   ```
   flask create-admin tu-email@ejemplo.com tu-contraseña
   ```

6. Ejecuta la aplicación:
   ```
   flask run
   ```

7. Accede a la aplicación en tu navegador: http://localhost:5000

## Despliegue en Render

### Paso 1: Preparar el repositorio en GitHub

1. Crea un nuevo repositorio en GitHub
2. Sube todos los archivos de este proyecto a tu repositorio:
   ```
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/tu-usuario/tu-repositorio.git
   git push -u origin main
   ```

### Paso 2: Configurar el servicio en Render

1. Crea una cuenta en [Render](https://render.com/) si aún no tienes una
2. En el Dashboard de Render, haz clic en "New" y selecciona "Web Service"
3. Conecta tu repositorio de GitHub
4. Configura el servicio con los siguientes valores:
   - **Name**: comisiones-app (o el nombre que prefieras)
   - **Runtime**: Python
   - **Build Command**: `pip install -r requirements.txt && flask db init && flask db migrate -m "initial migration" && flask db upgrade`
   - **Start Command**: `gunicorn "app:create_app()" --bind 0.0.0.0:$PORT`
   - **Root Directory**: Déjalo en blanco

5. En la sección "Environment", añade las siguientes variables:
   - `FLASK_APP`: run.py
   - `FLASK_ENV`: production
   - `SECRET_KEY`: (genera un valor aleatorio largo)

6. Crea una base de datos PostgreSQL en Render:
   - Haz clic en "New" y selecciona "PostgreSQL"
   - Configura un nombre para tu base de datos
   - Una vez creada, copia la "Internal Connection String"
   - Vuelve a tu servicio web y añade la variable `DATABASE_URL` con el valor de la cadena de conexión

7. Haz clic en "Create Web Service"

8. Una vez desplegado, podrás acceder a tu aplicación en la URL proporcionada por Render

9. Para crear un usuario administrador, ve a la pestaña "Shell" de tu servicio en Render y ejecuta:
   ```
   cd comisiones_app && python -c "from app import create_app, db; from app.models import Usuario; app = create_app(); app.app_context().push(); admin = Usuario(email='admin@ejemplo.com', nombre='Admin', apellidos='Sistema', telefono='123456789', razon_social='Administración', nombre_comercial='Admin', cargo='Administrador', rol='admin', activo=True); admin.set_password('admin123'); db.session.add(admin); db.session.commit(); print('Admin creado')"
   ```

10. Ahora podrás iniciar sesión con:
    - Email: admin@ejemplo.com
    - Contraseña: admin123

## Estructura del proyecto

```
comisiones_app/
├── app/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   ├── img/
│   │   └── uploads/
│   ├── templates/
│   │   ├── admin/
│   │   ├── auth/
│   │   ├── comisiones/
│   │   ├── temas/
│   │   ├── errors/
│   │   └── main/
│   ├── routes/
│   ├── forms/
│   ├── utils/
│   ├── __init__.py
│   ├── config.py
│   └── models.py
├── migrations/
├── .env
├── .env.example
├── requirements.txt
├── render.yaml
└── run.py
```

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

## Contacto

Para cualquier consulta o sugerencia, por favor contacta a: info@comisionesmarinas.es
