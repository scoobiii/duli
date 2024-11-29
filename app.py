import streamlit as st
import requests
import tensorflow as tf
import numpy as np
from PIL import Image
import plotly.express as px
from io import BytesIO

# URLs dos arquivos do modelo
MODEL_URL = "https://storage.googleapis.com/tm-model/1f9ATyXbr/model.json"
WEIGHTS_URL = "https://storage.googleapis.com/tm-model/1f9ATyXbr/model.weights.bin"
METADATA_URL = "https://storage.googleapis.com/tm-model/1f9ATyXbr/metadata.json"

# Lista de labels (extraídas do metadata fornecido)
LABELS = [
    "SARS", "Pneumocistos...", "PneumoAspira...", "PneumoCavita...", "PneumoClamíd...",
    "PneumoKlebsi...", "PneumoLegion...", "Pneumococcal", "Pneumocystis...", "PneumoCystis...",
    "Pneumocystis", "PneumoStrept...", "NORMAL", "Pneumonia", "Covid-19 ARD...", 
    "Covid-19 & P...", "Covid-19 TC", "Não Covid-19...", "Covid-19", "NIMG", "COVID BR", "NORMAL BR"
]

# Função para carregar o modelo
@st.cache_resource
def load_model():
    """Baixa e carrega o modelo do Teachable Machine."""
    model = tf.keras.models.load_model(MODEL_URL)
    return model

model = load_model()

# Função para pré-processar a imagem
def preprocess_image(image):
    """Ajusta o tamanho da imagem e a normaliza para o modelo."""
    image = image.resize((224, 224))  # O tamanho esperado pelo modelo
    img_array = np.array(image) / 255.0  # Normalizar valores entre 0 e 1
    img_array = np.expand_dims(img_array, axis=0)  # Adicionar batch dimension
    return img_array

# Função para prever usando o modelo
def predict_image(image):
    """Faz a previsão usando o modelo carregado."""
    img_array = preprocess_image(image)
    predictions = model.predict(img_array)[0]  # Obter as probabilidades
    return predictions

# Configuração da interface
st.title("DULI - Diagnóstico por Imagem com Treemap")
st.write("Carregue uma imagem para analisar possíveis diagnósticos baseados no modelo DULI.")

# Sidebar para escolher a entrada de imagem
st.sidebar.header("Envie sua Imagem")
option = st.sidebar.radio("Escolha a origem da imagem:", ["Upload", "URL", "Webcam"])

uploaded_image = None

# Opção: Upload
if option == "Upload":
    file = st.sidebar.file_uploader("Envie uma imagem:", type=["jpg", "jpeg", "png"])
    if file:
        uploaded_image = Image.open(file)

# Opção: URL
elif option == "URL":
    url = st.sidebar.text_input("Cole a URL da imagem:")
    if url:
        try:
            response = requests.get(url, stream=True)
            uploaded_image = Image.open(BytesIO(response.content))
        except:
            st.sidebar.error("URL inválida. Tente novamente.")

# Opção: Webcam (simulação com imagem exemplo)
elif option == "Webcam":
    uploaded_image = Image.open("sample_image.jpg")  # Substituir pela lógica de webcam, se necessário

# Processar e exibir os resultados
if uploaded_image:
    st.image(uploaded_image, caption="Imagem carregada", use_column_width=True)
    st.write("Analisando a imagem...")
    
    # Obter previsões do modelo
    predictions = predict_image(uploaded_image)

    # Preparar dados para o Treemap
    data = {
        "Classe": LABELS,
        "Probabilidade (%)": [round(p * 100, 2) for p in predictions],
    }

    # Criar o Treemap com Plotly
    fig = px.treemap(
        data,
        path=["Classe"],
        values="Probabilidade (%)",
        title="Treemap - Diagnóstico por Classe",
        color="Probabilidade (%)",
        color_continuous_scale="Viridis",
    )
    st.plotly_chart(fig)

    # Mostrar a classe com maior probabilidade
    max_class = LABELS[np.argmax(predictions)]
    max_prob = np.max(predictions) * 100
    st.write(f"**Classe mais provável:** {max_class} ({max_prob:.2f}%)")
