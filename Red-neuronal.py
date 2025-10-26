import streamlit as st
import time
import random

# --- Configuración de la app ---
st.set_page_config(page_title="Red Neuronal Animada", page_icon="🧠", layout="centered")

st.title("🧠 Red Neuronal Animada – Aprendizaje Supervisado")
st.markdown("""
Esta simulación muestra cómo los datos **fluyen a través de una red neuronal**,  
desde las **entradas** hasta la **salida**, en un proceso conocido como  
**propagación hacia adelante (forward propagation)**.
""")

# --- Parámetros de la red ---
layers = [3, 4, 2, 1]  # Número de neuronas por capa
colors = ["#1E88E5", "#43A047", "#FB8C00", "#E53935"]  # Colores por capa

# --- Función para dibujar la red neuronal ---
def draw_network(active_neuron=None, active_connection=None):
    html = "<div style='display:flex; justify-content:center; align-items:center; gap:60px;'>"
    for i, n_neurons in enumerate(layers):
        html += "<div style='display:flex; flex-direction:column; align-items:center;'>"
        for j in range(n_neurons):
            color = colors[i]
            glow = "0 0 15px #fff" if active_neuron == (i, j) else "0 0 5px #000"
            html += f"""
            <div style='width:30px; height:30px; border-radius:50%;
                        background:{color}; margin:8px 0;
                        box-shadow:{glow};'></div>
            """
        html += "</div>"
    html += "</div>"

    # Conexiones (líneas animadas)
    if active_connection:
        html += f"""
        <div style='position:relative; top:-250px; left:50%; width:2px; height:100px;
                    background:linear-gradient(to bottom, {active_connection}, transparent);
                    animation: pulse 0.3s infinite alternate;'>
        </div>
        <style>
            @keyframes pulse {{
                0% {{ opacity: 0.2; }}
                100% {{ opacity: 1; }}
            }}
        </style>
        """
    st.markdown(html, unsafe_allow_html=True)

# --- Botón de inicio ---
start = st.button("🚀 Iniciar Propagación hacia Adelante")

placeholder = st.empty()

if start:
    for i, n_neurons in enumerate(layers):
        for j in range(n_neurons):
            with placeholder.container():
                st.subheader(f"🔹 Activando neurona: Capa {i+1}, Neurona {j+1}")
                draw_network(active_neuron=(i, j))
                time.sleep(0.4)
            
            # Dibujar una conexión simulada
            with placeholder.container():
                draw_network(active_neuron=(i, j), active_connection=random.choice(colors))
                time.sleep(0.3)

    with placeholder.container():
        draw_network()
        st.success("✅ Propagación completada: la red ha generado una salida final.")

# --- Explicación adicional ---
st.markdown("---")
st.info("""
### 💡 Concepto Clave
1. Cada **neurona** recibe señales de las anteriores y calcula una salida.
2. Las **líneas** representan las **conexiones sinápticas** (pesos).
3. El color muestra cómo **la información se propaga capa por capa**.
4. Durante el entrenamiento, la red ajusta los pesos usando **backpropagation**.
""")

st.caption("Creado con ❤️ en Streamlit — por Néstor Carpio")
