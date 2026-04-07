# Blog Torres - TP Final

**Alumna:** Libel Torres
**Tecnologías:** Python 3 · Django 4.2 · SQLite · Bootstrap 5

---

## ¿De qué trata?

Blog personal donde los usuarios pueden leer entradas, registrarse y, una vez logueados, crear sus propias publicaciones con texto enriquecido e imágenes. También incluye perfiles de usuario y mensajería privada entre usuarios registrados.

---

## Cómo levantar el proyecto

### 1. Crear y activar el entorno virtual

```bash
python -m venv venv
venv\Scripts\activate
```

> Tiene que aparecer `(venv)` al inicio de la línea.

### 2. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 3. Crear la base de datos

```bash
python manage.py migrate
```

### 4. Crear un usuario administrador

```bash
python manage.py createsuperuser
```

### 5. Levantar el servidor

```bash
python manage.py runserver
```

### 6. Abrir en el navegador

```
http://127.0.0.1:8000/
```

---

## Páginas principales

| URL | Descripción |
|-----|-------------|
| `/` | Inicio |
| `/about/` | Acerca de mí |
| `/pages/` | Listado del blog |
| `/accounts/registro/` | Registro de usuario |
| `/accounts/login/` | Iniciar sesión |
| `/accounts/perfil/` | Ver y editar perfil |
| `/messaging/bandeja/` | Mensajes privados |
| `/admin/` | Panel de administración |

---

## Funcionalidades

- Registro, login y logout de usuarios
- Perfil editable con biografía, link y fecha de nacimiento
- CRUD de entradas del blog (solo usuarios logueados)
- Editor de texto enriquecido con soporte de imágenes (CKEditor)
- Mensajería privada entre usuarios
- Panel de administración en `/admin/`
