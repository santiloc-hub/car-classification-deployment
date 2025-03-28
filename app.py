import streamlit as st
import requests

st.title("🚗 Clasificación de Automóviles")
st.write("Selecciona las características del automóvil para predecir su categoría.")

# 📌 Opciones de entrada basadas en el dataset
buying_options = ["vhigh", "high", "med", "low"]
maint_options = ["vhigh", "high", "med", "low"]
doors_options = ["2", "3", "4", "5more"]
persons_options = ["2", "4", "more"]
lug_boot_options = ["small", "med", "big"]
safety_options = ["low", "med", "high"]

# 📌 Controles de entrada en Streamlit
buying = st.selectbox("Precio de compra:", buying_options)
maint = st.selectbox("Costo de mantenimiento:", maint_options)
doors = st.selectbox("Número de puertas:", doors_options)
persons = st.selectbox("Capacidad de personas:", persons_options)
lug_boot = st.selectbox("Tamaño del baúl:", lug_boot_options)
safety = st.selectbox("Seguridad:", safety_options)

# 📌 Botón para hacer la predicción
if st.button("Predecir categoría del automóvil 🚀"):
    # Crear datos de entrada
    input_data = {
        "buying": buying,
        "maint": maint,
        "doors": doors,
        "persons": persons,
        "lug_boot": lug_boot,
        "safety": safety,
    }

    # 📌 Llamar a la API para obtener la predicción
    response = requests.post("http://127.0.0.1:8000/predict", json=input_data)

    # 📌 Mostrar el resultado
    if response.status_code == 200:
        prediction = response.json().get("prediction", None)
        if prediction:
            st.success(f"✅ Categoría Predicha: **{prediction}**")
        else:
            st.error("❌ Error en la predicción.")
    else:
        st.error("❌ No se pudo conectar a la API.")
