import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

def download_from_kaggle(dataset: str, path: str):
    # Autenticazione ritardata: usa i secret di Streamlit
    import streamlit as st

    os.environ["KAGGLE_USERNAME"] = st.secrets["KAGGLE_USERNAME"]
    os.environ["KAGGLE_KEY"] = st.secrets["KAGGLE_KEY"]

    api = KaggleApi()
    api.authenticate()

    api.dataset_download_files(dataset, path=path, unzip=True)

