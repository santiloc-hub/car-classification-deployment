import requests

# 📌 Definir la URL base de la API
API_URL = "http://127.0.0.1:8080/predict"

# 📌 Datos de prueba
test_data = {
    "buying": "low",
    "maint": "med",
    "doors": "4",
    "persons": "4",
    "lug_boot": "big",
    "safety": "high"
}

# 📌 Hacer la solicitud POST a la API
response = requests.post(API_URL, json=test_data)

# 📌 Verificar la respuesta
if response.status_code == 200:
    print("✅ Respuesta de la API:", response.json())
else:
    print("❌ Error en la API:", response.status_code, response.text)
