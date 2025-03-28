# 🚗 API de Clasificación de Autos

## 📌 Descripción del Proyecto
Este proyecto proporciona una **API REST basada en FastAPI** para clasificar modelos de automóviles según características de entrada. El modelo ha sido previamente entrenado con un conjunto de datos de diferentes atributos de vehículos y puede predecir la categoría de un automóvil dado sus características.

## 🚀 Características
- **API REST con FastAPI**
- **Codificación y decodificación automática de variables categóricas**
- **Predicción de la clasificación del automóvil según sus características**
- **Documentación en Swagger UI disponible en `/docs`**
- **Dockerizado para una fácil implementación**
- **Incluye monitoreo y registro del modelo**

## 📂 Estructura del Proyecto
```
📁 car-classification-api/
│-- 📄 main.py              # Aplicación FastAPI
│-- 📄 model.pkl            # Modelo de clasificación preentrenado con encoders
│-- 📄 requirements.txt     # Dependencias
│-- 📄 Dockerfile           # Configuración del contenedor Docker
│-- 📄 README.md            # Documentación del proyecto
│-- 📄 test_api.py          # Script de prueba de la API
│-- 📁 notebooks/           # Notebooks documentando el proceso
```

## 🛠️ Instalación y Configuración
### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/santiloc-hub/car-classification-deployment.git
cd car-classification-api
```

### 2️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3️⃣ Ejecutar el servidor FastAPI
```bash
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```
La API estará accesible en `http://localhost:8080/docs` (Swagger UI).

## 🔥 Endpoints de la API
### 🚀 Predicción de Categoría del Automóvil
**Endpoint:** `POST /predict`

**Cuerpo de la solicitud (Formato Original de los Datos):**
```json
{
  "buying": "vhigh",
  "maint": "low",
  "doors": "4",
  "persons": "more",
  "lug_boot": "big",
  "safety": "med"
}
```

**Respuesta:**
```json
{
  "prediction": "acc"
}
```

### 🛠️ Codificación y Decodificación
- **Los valores de entrada (ej. `"vhigh"`, `"low"`) son convertidos automáticamente a enteros antes de ser procesados por el modelo.**
- **El resultado de la predicción se decodifica de nuevo a su categoría original (`"unacc"`, `"acc"`, `"good"`, `"vgood"`).**

## 🧪 Pruebas
Ejecutar el script de prueba para validar la API:
```bash
pytest test_api.py
```

## 📜 Licencia
Este proyecto está bajo la licencia MIT.

## ✨ Contribuidores
- **Tu Nombre** - [Perfil de GitHub](https://github.com/santiloc-hub)

