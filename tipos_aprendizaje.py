import streamlit as st
import plotly.graph_objects as go
import time

st.set_page_config(page_title="Tipos de Aprendizaje en IA", layout="wide", page_icon="🧠")

st.title("🧠 Tipos de Aprendizaje en Inteligencia Artificial")
st.markdown("Explora los principales tipos de **aprendizaje automático (Machine Learning)** con ejemplos, imágenes y diagramas interactivos.")

tabs = st.tabs([
    "📘 Supervisado",
    "📗 No Supervisado",
    "🤖 Reforzamiento (Animado)",
    "🧩 Semisupervisado",
    "⚙️ Auto-supervisado"
])

# --- Función para mostrar diagramas simples ---
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
    Cada entrada tiene una salida conocida, y el algoritmo busca aprender la relación entre ambas.
    """)
    st.image("https://cdn.pixabay.com/photo/2016/03/31/20/10/analysis-1296805_960_720.png", use_container_width=True)
    mostrar_diagrama(
        ["Datos de Entrada", "Etiquetas", "Modelo", "Predicción"],
        [0, 1, 0],
        [2, 2, 3],
        [5, 5, 10],
        "Flujo del Aprendizaje Supervisado"
    )
    st.markdown("💡 *Ejemplo:* Predecir el precio de una casa según sus características.")


# --- No Supervisado ---
with tabs[1]:
    st.header("📗 Aprendizaje No Supervisado")
    st.write("""
    El modelo **no tiene etiquetas** y debe **descubrir patrones o agrupamientos** en los datos.
    """)
    st.image("https://cdn.pixabay.com/photo/2017/06/07/18/05/network-2386310_960_720.jpg", use_container_width=True)
    mostrar_diagrama(
        ["Datos sin etiquetas", "Modelo", "Grupos Descubiertos"],
        [0, 0],
        [1, 2],
        [8, 10],
        "Flujo del Aprendizaje No Supervisado"
    )
    st.markdown("💡 *Ejemplo:* Agrupar clientes según sus hábitos de compra.")


# --- Reforzamiento con animación ---
with tabs[2]:
    st.header("🤖 Aprendizaje por Reforzamiento (Animado)")
    st.write("""
    En el **aprendizaje por refuerzo**, un **agente** interactúa con un **entorno**, toma **acciones** y recibe **recompensas**.
    Aprende mediante **prueba y error** a maximizar su recompensa total.
    """)

    st.image("https://cdn.pixabay.com/photo/2020/08/18/12/12/robot-5493733_1280.png", use_container_width=True)

    st.subheader("🎬 Ciclo de aprendizaje del agente")

    labels = ["Agente", "Acción", "Entorno", "Recompensa"]
    sources = [0, 1, 2, 3]
    targets = [1, 2, 3, 0]

    # Creamos frames para la animación del flujo circular
    frames = []
    for i in range(4):
        frame_links = [dict(source=[sources[i]], target=[targets[i]], value=[10])]
        fig = go.Figure(data=[go.Sankey(
            node=dict(
                pad=30,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=labels,
                color="lightgreen"
            ),
            link=dict(
                source=frame_links[0]['source'],
                target=frame_links[0]['target'],
                value=frame_links[0]['value'],
                color=["rgba(0,200,0,0.5)"]
            )
        )])
        fig.update_layout(title_text=f"Paso {i+1}: {labels[sources[i]]} → {labels[targets[i]]}", font_size=12)
        frames.append(fig)

    # Botón para reproducir la animación
    if st.button("▶️ Reproducir ciclo de aprendizaje"):
        for f in frames:
            st.plotly_chart(f, use_container_width=True)
            time.sleep(1.2)

    st.markdown("""
    **Ciclo de aprendizaje:**
    1️⃣ El **agente** toma una acción.  
    2️⃣ El **entorno** responde.  
    3️⃣ El agente recibe una **recompensa o castigo**.  
    4️⃣ Actualiza su política para mejorar la próxima decisión.
    """)

    st.success("El agente aprende con el tiempo qué acciones lo acercan más a su objetivo 🏆")


# --- Semisupervisado ---
with tabs[3]:
    st.header("🧩 Aprendizaje Semisupervisado")
    st.write("""
    Combina **pocos datos etiquetados** con **muchos no etiquetados**, aprovechando lo mejor de ambos mundos.
    """)
    st.image("https://cdn.pixabay.com/photo/2021/01/14/11/45/data-5918063_1280.jpg", use_container_width=True)
    mostrar_diagrama(
        ["Datos Etiquetados", "Datos No Etiquetados", "Modelo", "Predicciones"],
        [0, 1, 0],
        [2, 2, 3],
        [5, 8, 10],
        "Flujo del Aprendizaje Semisupervisado"
    )
    st.markdown("💡 *Ejemplo:* Reconocimiento facial con pocas imágenes etiquetadas.")


# --- Auto-supervisado ---
with tabs[4]:
    st.header("⚙️ Aprendizaje Auto-supervisado")
    st.write("""
    El modelo **genera sus propias etiquetas** a partir de los datos.
    Es utilizado por modelos modernos como **GPT, BERT y CLIP**.
    """)
    st.image("https://cdn.pixabay.com/photo/2022/01/28/16/10/artificial-intelligence-6976011_1280.jpg", use_container_width=True)
    mostrar_diagrama(
        ["Datos sin procesar", "Etiquetas internas", "Modelo", "Representación aprendida"],
        [0, 1, 2],
        [1, 2, 3],
        [5, 7, 10],
        "Flujo del Aprendizaje Auto-supervisado"
    )
    st.markdown("💡 *Ejemplo:* Predecir la palabra faltante en una oración para aprender contexto.")

st.markdown("---")
st.info("💡 Explora cada pestaña para visualizar cómo cada tipo de aprendizaje procesa y transforma los datos.")
st.caption("Desarrollado con ❤️ en Streamlit | Néstor Carpio")
