import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Análisis de Sentimientos ✨", page_icon="💬", layout="centered")

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    body {
        background-color: #f7f9fc;
    }
    .main {
        background-color: #ffffff;
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    h1 {
        color: #4a4e69;
        text-align: center;
        font-size: 2.5rem !important;
        font-weight: 800;
    }
    h2, h3, h4 {
        color: #22223b;
    }
    .stTextArea textarea {
        border-radius: 10px !important;
        border: 2px solid #9a8c98 !important;
    }
    .result-box {
        background-color: #f2e9e4;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- TÍTULO ---
st.title("💬 Analizador de Sentimientos con TextBlob")

st.markdown("""
Explora cómo un texto expresa **emociones y opiniones**.  
Esta aplicación traduce tu frase al inglés, analiza su **polaridad** y **subjetividad**,  
y muestra si el sentimiento es **positivo**, **negativo** o **neutral** 🌈.
""")

translator = Translator()

# --- SIDEBAR ---
with st.sidebar:
    st.header("🧠 Conceptos Clave")
    st.markdown("""
    **Polaridad:**  
    Indica si el sentimiento del texto es positivo, negativo o neutral.  
    Valor entre **-1** (muy negativo) y **1** (muy positivo).

    **Subjetividad:**  
    Mide cuán emocional u opinativo es el texto.  
    Valor entre **0** (objetivo) y **1** (subjetivo).
    """)

# --- ANÁLISIS DE SENTIMIENTO ---
st.subheader("🔍 Analizar Polaridad y Subjetividad")
text1 = st.text_area("✏️ Escribe una frase para analizar:", placeholder="Ejemplo: Me encanta aprender cosas nuevas...")

if text1:
    with st.spinner("Analizando el texto... ⏳"):
        translation = translator.translate(text1, src="es", dest="en")
        blob = TextBlob(translation.text)
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

    st.success("✅ Análisis completado con éxito")
    st.markdown(f"**Traducción al inglés:** _{translation.text}_")
    st.write("---")
    st.metric("📈 Polaridad", f"{polarity}")
    st.metric("🎭 Subjetividad", f"{subjectivity}")

    if polarity >= 0.5:
        st.markdown('<div class="result-box">💖 Sentimiento Positivo</div>', unsafe_allow_html=True)
    elif polarity <= -0.5:
        st.markdown('<div class="result-box">💔 Sentimiento Negativo</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result-box">😐 Sentimiento Neutral</div>', unsafe_allow_html=True)

# --- CORRECCIÓN EN INGLÉS ---
st.subheader("📝 Corrección Ortográfica en Inglés")
text2 = st.text_area("✍️ Escribe en inglés para corregir:", key="4", placeholder="Ejemplo: I am lerning english evry day")

if text2:
    blob2 = TextBlob(text2)
    corrected = blob2.correct()
    st.info("🔧 Texto corregido:")
    st.markdown(f"**{corrected}**")

# --- FOOTER ---
st.markdown("""
---
💡 **Desarrollado con Python, TextBlob y Streamlit**  
Autor: *Tu nombre o alias ✨*
""")
