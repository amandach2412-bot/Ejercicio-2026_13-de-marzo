import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# CONFIGURACION
# ---------------------------
st.set_page_config(page_title="Dashboard Psicologia e IA", layout="wide")

# ---------------------------
# TITULO
# ---------------------------
st.title("Dashboard: IA en la Psicologia")
st.write("Analisis del uso de chatbots en la salud mental")

# ---------------------------
# SIDEBAR
# ---------------------------
st.sidebar.header("Secciones")

seccion = st.sidebar.radio(
    "Selecciona una seccion",
    [
        "Resumen",
        "Ventajas",
        "Desventajas",
        "Futuro",
        "Reflexion critica",
        "Visualizacion"
    ]
)

# ---------------------------
# CONTENIDO
# ---------------------------

if seccion == "Resumen":
    st.header("Resumen")
    st.write("""
    Los chatbots son herramientas digitales que simulan conversaciones humanas y 
    estan siendo utilizados en el campo de la psicologia como apoyo emocional.
    
    Permiten acceso rapido a ayuda, especialmente para estudiantes con estres o TDAH.
    """)

elif seccion == "Ventajas":
    st.header("Ventajas de los chatbots")

    ventajas = [
        "Disponibilidad inmediata",
        "Acceso rapido a apoyo emocional",
        "Uso de terapia cognitivo conductual",
        "Facilitan autoevaluacion",
        "Apoyo constante"
    ]

    for v in ventajas:
        st.write("- " + v)

elif seccion == "Desventajas":
    st.header("Desventajas de los chatbots")

    desventajas = [
        "No tienen empatia real",
        "Pueden generar dependencia",
        "Pueden aumentar la soledad",
        "No reemplazan a un profesional",
    ]

    for d in desventajas:
        st.write("- " + d)

elif seccion == "Futuro":
    st.header("Futuro de la IA en psicologia")

    st.write("""
    Los chatbots no reemplazaran a los psicologos, sino que funcionaran como asistentes.
    
    Pueden ayudar a detectar sintomas tempranos y apoyar en tareas repetitivas.
    """)

elif seccion == "Reflexion critica":
    st.header("Reflexion critica")

    st.write("""
    La inteligencia artificial es util para organizar informacion y generar contenido rapido.
    
    Sin embargo, presenta limitaciones:
    - Puede generar informacion incorrecta
    - Falta profundidad critica
    - Depende de la calidad del prompt
    
    El juicio humano sigue siendo esencial.
    """)

# ---------------------------
# VISUALIZACION
# ---------------------------
elif seccion == "Visualizacion":
    st.header("Analisis visual")

    data = pd.DataFrame({
        "Categoria": ["Ventajas", "Desventajas"],
        "Cantidad": [5, 4]
    })

    st.subheader("Comparacion")

    fig, ax = plt.subplots()
    ax.bar(data["Categoria"], data["Cantidad"])
    ax.set_title("Comparacion de aspectos positivos y negativos")
    ax.set_ylabel("Cantidad")

    st.pyplot(fig)

# ---------------------------
# METRICAS
# ---------------------------
st.sidebar.header("Metricas")

col1, col2 = st.sidebar.columns(2)

col1.metric("Ventajas", 5)
col2.metric("Desventajas", 4)
