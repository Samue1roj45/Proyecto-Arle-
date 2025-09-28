
# 🏠 Proyecto Inmobiliaria

Este proyecto es una aplicación web desarrollada en **Django**.  
Permite gestionar inmuebles, usuarios y favoritos, con un panel de administración personalizado.

---

## ⚙️ Requisitos previos

Asegúrate de tener instalado:

- [Python 3.11+](https://www.python.org/downloads/)  
- [pip](https://pip.pypa.io/en/stable/installation/)  
- [virtualenv](https://virtualenv.pypa.io/) *(opcional pero recomendado)*  
- [Git](https://git-scm.com/)  

---

## 🚀 Instalación y configuración

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/TU-USUARIO/TU-REPO.git
   cd TU-REPO
   ```

2. **Crear y activar un entorno virtual**
   ```bash
   # En Windows (PowerShell)
   python -m venv .venv
   .venv\Scripts\activate

   # En Linux/Mac
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la base de datos**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crear un superusuario (acceso admin)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecutar el servidor**
   ```bash
   python manage.py runserver
   ```

   Ahora abre [http://127.0.0.1:8000](http://127.0.0.1:8000) en tu navegador.  

---

## 📂 Estructura principal del proyecto

```
inmobiliaria/
│── inmobiliaria/        # Configuración principal de Django
│── inmuebles/           # App para gestión de inmuebles
│── usuarios/            # App para gestión de usuarios
│── templates/           # Plantillas HTML
│── media/               # Archivos subidos (ignorado en git)
│── db.sqlite3           # Base de datos local (ignorada en git)
requirements.txt         # Dependencias del proyecto
manage.py                # Punto de entrada Django
```

---

## 🛑 Archivos que NO se suben a GitHub

El `.gitignore` ya está configurado para ignorar:

```
db.sqlite3
media/
__pycache__/
*.pyc
.idea/
.vscode/
```

---

## ✅ Comandos útiles de Git

- Ver el estado de los cambios:
  ```bash
  git status
  ```

- Agregar archivos específicos:
  ```bash
  git add ruta/al/archivo.py
  ```

- Agregar una carpeta completa:
  ```bash
  git add templates/admin/
  ```

- Confirmar cambios:
  ```bash
  git commit -m "Mensaje del commit"
  ```

- Subir al repositorio remoto:
  ```bash
  git push origin version_1
  ```

- Restaurar (sacar de staging) un archivo:
  ```bash
  git restore --staged archivo.py
  ```

---

## 👥 Contribuir

1. Crear una rama:
   ```bash
   git checkout -b mi_rama
   ```

2. Hacer cambios y subir:
   ```bash
   git add .
   git commit -m "Descripción"
   git push origin mi_rama
   ```

3. Abrir un Pull Request en GitHub.