import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Análisis de Sentimientos",
    page_icon="💬",
    layout="centered",
)

# --- ESTILOS VISUALES ---
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(180deg, #f0f9ff 0%, #e0f2fe 50%, #fafafa 100%);
            color: #1e293b;
            font-family: 'Poppins', sans-serif;
        }

        h1 {
            text-align: center;
            font-size: 2.5em;
            background: linear-gradient(to right, #0284c7, #2563eb);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 700;
        }

        h2, h3 {
            color: #1e40af;
            text-align: center;
            font-weight: 600;
        }

        .stButton>button {
            background: linear-gradient(90deg, #2563eb, #1d4ed8);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 10px 25px;
            font-weight: 600;
            font-size: 16px;
            transition: 0.3s ease-in-out;
            box-shadow: 0 4px 10px rgba(37, 99, 235, 0.3);
        }

        .stButton>button:hover {
            transform: scale(1.03);
            background: linear-gradient(90deg, #1e3a8a, #3b82f6);
            box-shadow: 0 6px 14px rgba(37, 99, 235, 0.4);
        }

        section[data-testid="stSidebar"] {
            background-color: #eff6ff;
            border-right: 2px solid #bfdbfe;
        }

        .highlight {
            background-color: #e0f2fe;
            border-left: 5px solid #0284c7;
            padding: 10px;
            border-radius: 8px;
            font-weight: 500;
        }

        .sentimiento {
            text-align: center;
            font-size: 1.2em;
            font-weight: 600;
            margin-top: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# --- TÍTULO ---
st.title("💬 Analizador de Sentimientos con TextBlob")
st.markdown("<h3>Descubre si tu texto transmite una emoción positiva, negativa o neutral</h3>", unsafe_allow_html=True)

translator = Translator()

# --- SIDEBAR ---
with st.sidebar:
    st.header("📘 Polaridad y Subjetividad")
    st.markdown("""
    **Polaridad:** mide si el sentimiento es positivo, negativo o neutral.  
    -1 ➜ Muy negativo 😞  
    0 ➜ Neutral 😐  
    1 ➜ Muy positivo 😄  
    
    **Subjetividad:** indica cuánto del texto es una opinión (1) o un hecho (0).  
    """)

# --- ANÁLISIS DE SENTIMIENTOS ---
with st.expander("🔍 Analizar polaridad y subjetividad"):
    st.markdown("<div class='highlight'>Escribe una frase o párrafo en español para analizar su tono emocional:</div>", unsafe_allow_html=True)
    text1 = st.text_area("✍️ Escribe aquí tu texto:")

    if text1:
        # Traducción a inglés para mejor precisión de TextBlob
        translation = translator.translate(text1, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)

        # Resultados
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        st.write(f"**🧭 Polaridad:** {polarity}")
        st.write(f"**📊 Subjetividad:** {subjectivity}")

        # Interpretación
        if polarity >= 0.5:
            st.markdown("<div class='sentimiento' style='color:#16a34a;'>🌞 Sentimiento Positivo</div>", unsafe_allow_html=True)
        elif polarity <= -0.5:
            st.markdown("<div class='sentimiento' style='color:#dc2626;'>🌧️ Sentimiento Negativo</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='sentimiento' style='color:#334155;'>🌤️ Sentimiento Neutral</div>", unsafe_allow_html=True)

# --- CORRECCIÓN DE TEXTO ---
with st.expander("📝 Corrección en inglés"):
    st.markdown("<div class='highlight'>Escribe un texto en inglés para ver su corrección gramatical:</div>", unsafe_allow_html=True)
    text2 = st.text_area("✍️ Escribe tu texto en inglés:", key="text_correct")

    if text2:
        blob2 = TextBlob(text2)
        st.write("✅ **Texto corregido:**")
        st.success(blob2.correct())
