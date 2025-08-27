import os
import streamlit as st
from kaggle.api.kaggle_api_extended import KaggleApi

def download_from_kaggle(dataset: str, path: str = "data"):
    if not os.path.exists(path):
        os.makedirs(path)
    
    # Setta le credenziali come variabili d'ambiente
    os.environ["KAGGLE_USERNAME"] = st.secrets["kaggle"]["username"]
    os.environ["KAGGLE_KEY"] = st.secrets["kaggle"]["key"]

    api = KaggleApi()
    api.authenticate()

    api.dataset_download_files(dataset, path=path, unzip=True)
    st.write(f"✅ Dataset `{dataset}` scaricato correttamente in `{path}`.")
