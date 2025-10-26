import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Tipos de Aprendizaje en IA", layout="wide", page_icon="🧠")

st.title("🧠 Tipos de Aprendizaje en Inteligencia Artificial")
st.markdown("Explora los principales tipos de **aprendizaje automático (Machine Learning)** con ejemplos, imágenes y diagramas interactivos.")

tabs = st.tabs([
    "📘 Supervisado",
    "📗 No Supervisado",
    "🤖 Reforzamiento",
    "🧩 Semisupervisado",
    "⚙️ Auto-supervisado"
])

# --- Función para mostrar un diagrama tipo Sankey ---
def mostrar_diagrama(labels, sources, targets, values, titulo):
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=25,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=labels,
            color="lightblue"
        ),
        link=dict(
            source=sources,
            target=targets,
            value=values
        )
    )])
    fig.update_layout(title_text=titulo, font_size=12, height=400)
    st.plotly_chart(fig, use_container_width=True)


# --- Supervisado ---
with tabs[0]:
    st.header("📘 Aprendizaje Supervisado")
    st.write("""
    El **modelo aprende a partir de ejemplos etiquetados**.  
    Cada entrada tiene una salida conocida, y el algoritmo busca **aprender la relación entre ambas**.
    """)
    st.image("https://cdn.pixabay.com/photo/2016/03/31/20/10/analysis-1296805_960_720.png", use_container_width=True)
    
    mostrar_diagrama(
        ["Datos de Entrada", "Etiquetas (Respuestas)", "Modelo", "Predicción"],
        [0, 1, 0],  # Fuentes
        [2, 2, 3],  # Destinos
        [5, 5, 10], # Valores
        "Flujo del Aprendizaje Supervisado"
    )

    st.subheader("Ejemplo:")
    st.markdown("- Predecir el **precio de una casa** a partir de su tamaño, ubicación y número de habitaciones.")


# --- No Supervisado ---
with tabs[1]:
    st.header("📗 Aprendizaje No Supervisado")
    st.write("""
    El modelo **no conoce las etiquetas** y debe **descubrir estructuras o patrones ocultos** en los datos.  
    Ideal para **agrupar, reducir dimensiones o detectar anomalías**.
    """)
    st.image("https://cdn.pixabay.com/photo/2017/06/07/18/05/network-2386310_960_720.jpg", use_container_width=True)
    
    mostrar_diagrama(
        ["Datos sin etiquetas", "Modelo de Agrupamiento", "Grupos Descubiertos"],
        [0, 0],
        [1, 2],
        [8, 10],
        "Flujo del Aprendizaje No Supervisado"
    )

    st.subheader("Ejemplo:")
    st.markdown("- Agrupar clientes según sus hábitos de compra (clustering).")


# --- Reforzamiento ---
with tabs[2]:
    st.header("🤖 Aprendizaje por Reforzamiento")
    st.write("""
    Un **agente** aprende interactuando con un **entorno**, tomando **acciones** y recibiendo **recompensas**.  
    Aprende por **prueba y error** a maximizar su recompensa acumulada.
    """)
    st.image("https://cdn.pixabay.com/photo/2020/08/18/12/12/robot-5493733_1280.png", use_container_width=True)
    
    mostrar_diagrama(
        ["Agente", "Entorno", "Acción", "Recompensa"],
        [0, 2, 1],
        [2, 1, 0],
        [10, 8, 5],
        "Ciclo del Aprendizaje por Reforzamiento"
    )

    st.subheader("Ejemplo:")
    st.markdown("- Un robot aprende a moverse sin chocar o una IA aprende a jugar ajedrez.")


# --- Semisupervisado ---
with tabs[3]:
    st.header("🧩 Aprendizaje Semisupervisado")
    st.write("""
    Combina datos **etiquetados y no etiquetados**.  
    Usa los pocos ejemplos conocidos para **guiar el aprendizaje de los desconocidos**.
    """)
    st.image("https://cdn.pixabay.com/photo/2021/01/14/11/45/data-5918063_1280.jpg", use_container_width=True)
    
    mostrar_diagrama(
        ["Datos Etiquetados", "Datos No Etiquetados", "Modelo", "Predicciones"],
        [0, 1, 0],
        [2, 2, 3],
        [5, 8, 10],
        "Flujo del Aprendizaje Semisupervisado"
    )

    st.subheader("Ejemplo:")
    st.markdown("- Reconocimiento facial con pocas imágenes etiquetadas y muchas sin etiquetas.")


# --- Auto-supervisado ---
with tabs[4]:
    st.header("⚙️ Aprendizaje Auto-supervisado")
    st.write("""
    El modelo **genera sus propias etiquetas** a partir de los datos.  
    Se usa en modelos modernos como **GPT, BERT y CLIP** para crear representaciones útiles del lenguaje o imágenes.
    """)
    st.image("https://cdn.pixabay.com/photo/2022/01/28/16/10/artificial-intelligence-6976011_1280.jpg", use_container_width=True)
    
    mostrar_diagrama(
        ["Datos sin procesar", "Generación de etiquetas internas", "Modelo", "Representación aprendida"],
        [0, 1, 2],
        [1, 2, 3],
        [5, 7, 10],
        "Flujo del Aprendizaje Auto-supervisado"
    )

    st.subheader("Ejemplo:")
    st.markdown("- Predecir la palabra faltante en una oración para entender el contexto del lenguaje.")

st.markdown("---")
st.info("💡 Consejo: usa las pestañas superiores para explorar cómo cada tipo de aprendizaje procesa la información.")
st.caption("Desarrollado con ❤️ en Streamlit | Néstor Carpio")
