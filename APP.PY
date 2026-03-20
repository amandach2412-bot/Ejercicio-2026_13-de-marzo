import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# CONFIGURACIÓN INICIAL
# ---------------------------
st.set_page_config(page_title="Mi Dashboard", layout="wide")

# ---------------------------
# TÍTULO
# ---------------------------
st.title("📊 Dashboard de Análisis")
st.write("Este es un dashboard básico en Streamlit")

# ---------------------------
# CARGA DE DATOS
# ---------------------------
@st.cache_data
def cargar_datos():
    # Puedes cambiar esto por tu propio archivo
    data = pd.DataFrame({
        'Categoria': ['A', 'B', 'C', 'D'],
        'Valores': [10, 20, 15, 30]
    })
    return data

df = cargar_datos()

# ---------------------------
# SIDEBAR (FILTROS)
# ---------------------------
st.sidebar.header("Filtros")

categoria = st.sidebar.selectbox(
    "Selecciona categoría",
    df['Categoria']
)

df_filtrado = df[df['Categoria'] == categoria]

# ---------------------------
# MÉTRICAS
# ---------------------------
st.subheader("🔢 Métricas")
col1, col2 = st.columns(2)

col1.metric("Total", int(df['Valores'].sum()))
col2.metric("Seleccionado", int(df_filtrado['Valores'].sum()))

# ---------------------------
# TABLA
# ---------------------------
st.subheader("📋 Datos")
st.dataframe(df)

# ---------------------------
# GRÁFICA
# ---------------------------
st.subheader("📈 Gráfica")

fig, ax = plt.subplots()
ax.bar(df['Categoria'], df['Valores'])
st.pyplot(fig)

# ---------------------------
# TEXTO FINAL
# ---------------------------

streamlit==1.33.0
pandas==2.2.2
matplotlib==3.8.4
numpy==1.26.4
st.write("Dashboard creado con Streamlit 🚀")
