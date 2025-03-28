import pickle
import os
import numpy as np
import uvicorn
import logging
from fastapi import FastAPI
from pydantic import BaseModel
from threading import Thread

# 📌 Configurar logging
logging.basicConfig(
    filename="app.log",  # Guarda los logs en un archivo
    level=logging.INFO,  # Nivel de log (INFO, DEBUG, ERROR, etc.)
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# 📌 Cargar el modelo y los encoders
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
with open(model_path, "rb") as f:
    model, label_encoder_y, encoders = pickle.load(f)

# 📌 Instanciar FastAPI
app = FastAPI(title="Car Classification API")

# 📌 Definir la estructura de la solicitud con Pydantic
class CarFeatures(BaseModel):
    buying: str
    maint: str
    doors: str
    persons: str
    lug_boot: str
    safety: str

# 📌 Endpoint para predecir la categoría del automóvil
@app.post("/predict")
def predict_category(car: CarFeatures):
    try:
        logging.info(f"Solicitud recibida: {car.dict()}")  # Log de entrada
        
        # Convertir datos de entrada a formato numérico usando los encoders
        input_data = np.array([
            encoders["buying"].transform([car.buying])[0],
            encoders["maint"].transform([car.maint])[0],
            encoders["doors"].transform([car.doors])[0],
            encoders["persons"].transform([car.persons])[0],
            encoders["lug_boot"].transform([car.lug_boot])[0],
            encoders["safety"].transform([car.safety])[0]
        ]).reshape(1, -1)

        # Hacer la predicción
        prediction = model.predict(input_data)[0]

        # Decodificar la predicción a su valor original
        decoded_prediction = label_encoder_y.inverse_transform([prediction])[0]

        logging.info(f"Predicción realizada: {decoded_prediction}")  # Log de salida

        return {"prediction": decoded_prediction}

    except Exception as e:
        logging.error(f"Error en la predicción: {str(e)}")  # Log de error
        return {"error": str(e)}

# 📌 Función para iniciar FastAPI con logs
def start_fastapi():
    logging.info("Iniciando servidor FastAPI en http://127.0.0.1:8080")
    uvicorn.run(app, host="127.0.0.1", port=8080, log_level="info")

if __name__ == "__main__":
    start_fastapi()
