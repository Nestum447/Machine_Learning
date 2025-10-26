import streamlit as st

# --- Configuración inicial ---
st.set_page_config(page_title="Tipos de Aprendizaje en IA", layout="centered", page_icon="🤖")

st.title("🤖 Tipos de Aprendizaje en Inteligencia Artificial")
st.markdown("Explora los principales **tipos de aprendizaje automático (Machine Learning)** usados en la IA moderna.")

# --- Menú lateral ---
tipo = st.sidebar.radio(
    "Selecciona un tipo de aprendizaje:",
    ["Aprendizaje Supervisado", "Aprendizaje No Supervisado", "Aprendizaje por Reforzamiento"],
)

# --- Contenido dinámico ---
if tipo == "Aprendizaje Supervisado":
    st.header("📘 Aprendizaje Supervisado")
    st.markdown("""
    En este tipo de aprendizaje, el modelo aprende a partir de **datos etiquetados**.  
    El objetivo es que el sistema encuentre una relación entre las entradas (X) y las salidas (Y).

    **Ejemplos comunes:**
    - Predicción del precio de casas 🏠  
    - Clasificación de correos spam 📧  
    - Reconocimiento facial 😃  

    **Algoritmos populares:**
    - Regresión Lineal
    - Árboles de Decisión
    - Máquinas de Soporte Vectorial (SVM)
    - Redes Neuronales Artificiales
    """)

elif tipo == "Aprendizaje No Supervisado":
    st.header("🧩 Aprendizaje No Supervisado")
    st.markdown("""
    En este tipo, el modelo trabaja con **datos sin etiquetas**, buscando patrones ocultos o estructuras naturales.

    **Ejemplos comunes:**
    - Agrupación de clientes por comportamiento 🛍️  
    - Compresión de datos 📉  
    - Detección de anomalías 🔍  

    **Algoritmos populares:**
    - K-Means
    - Análisis de Componentes Principales (PCA)
    - Modelos de Mezclas Gaussianas
    """)

elif tipo == "Aprendizaje por Reforzamiento":
    st.header("🏆 Aprendizaje por Reforzamiento")
    st.markdown("""
    En este tipo, el **agente aprende mediante prueba y error**, recibiendo **recompensas** o **castigos** según sus acciones.  
    Busca **maximizar la recompensa total** aprendiendo la mejor estrategia o política.

    **Ejemplos comunes:**
    - Robots aprendiendo a caminar 🤖  
    - Juegos como ajedrez o Go ♟️  
    - Vehículos autónomos 🚗  

    **Algoritmos populares:**
    - Q-Learning
    - Deep Q-Network (DQN)
    - SARSA
    """)

# --- Estilo visual ---
st.markdown("---")
st.info("💡 Usa el menú lateral para cambiar entre los tipos de aprendizaje.")

st.caption("Creado con ❤️ en Streamlit — por Néstor Carpio")
