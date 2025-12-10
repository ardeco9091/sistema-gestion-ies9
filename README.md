# Sistema de Gestión Académica - IES Nº 9 🎓

Plataforma web para la gestión administrativa de alumnos, desarrollada como parte de la **Práctica Profesionalizante** de la Tecnicatura Superior en Programación.

## 📋 Descripción del Proyecto

Este sistema moderniza el proceso de validación y búsqueda de alumnos mediante una interfaz web, reemplazando procesos manuales por una solución automatizada y escalable en la nube.

### 🚀 Funcionalidades Principales
1.  **Buscador Inteligente:** Permite localizar alumnos por Nombre o DNI (lectura de base de datos CSV/Excel).
2.  **Módulo de QA (Calidad):** Validador automático de correos institucionales para detectar errores de carga.
3.  **Reportes:** Visualización de estado académico (Regular/Ingresante).

---

## 🛠 Competencias Profesionales Aplicadas

Este proyecto fue desarrollado cumpliendo con los siguientes ejes de la práctica profesional:

### 1. Evaluación de Calidad de Software (Testing) 🛡️
Se implementó una estrategia de **Test Driven Development (TDD)** parcial.
* **Unit Testing:** Se desarrollaron pruebas automatizadas (`tests/test_validadores.py`) utilizando la librería `unittest`.
* **Cobertura:** Los tests verifican "caminos felices" (emails correctos), casos de error (dominios Gmail/Outlook) y manejo de excepciones (datos vacíos).
* **Ejecución:** Automatizada mediante scripts de verificación.

### 2. Administración de Proyectos (Metodologías Ágiles) 🔄
El desarrollo se gestionó simulando un entorno **Scrum**:
* **Sprint 1 (Backend):** Desarrollo de la lógica de validación y estructura de datos (`validadores.py`, `datos.py`).
* **Sprint 2 (Frontend):** Implementación de interfaz web con Flask y Jinja2 (`app.py`, templates).
* **Sprint 3 (Integración):** Conexión con base de datos CSV y despliegue.
* **Control de Versiones:** Gestión del código fuente mediante **Git y GitHub**.

### 3. Gestión de Servicios en la Nube ☁️
El software fue diseñado con arquitectura **Cloud-Native**:
* **Infraestructura:** Preparado para despliegue PaaS (Platform as a Service) en proveedores como **Render** o **Heroku**.
* **Configuración:** Incluye archivo `Procfile` para el servidor Gunicorn y `requirements.txt` para gestión de dependencias en la nube.

---

## 💻 Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Framework Web:** Flask
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Datos:** CSV (Simulación de Base de Datos legada)
* **Control de Versiones:** Git

---

## ⚙️ Instalación y Ejecución Local

Si deseas correr este proyecto en tu máquina:

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/TU_USUARIO/sistema-gestion-ies9.git](https://github.com/TU_USUARIO/sistema-gestion-ies9.git)
    ```
2.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Ejecutar la aplicación:**
    ```bash
    python app.py
    ```
4.  **Abrir en el navegador:**
    Visita `http://127.0.0.1:5000`

---
*Desarrollado por Ariel Artur de la Villarmois - IES Nº 9*
