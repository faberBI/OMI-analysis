import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

def download_from_kaggle(dataset: str, path: str = "data"):
    """
    Scarica un dataset da Kaggle.
    Se è uno zip, lo estrae nella cartella indicata.
    """
    os.makedirs(path, exist_ok=True)

    api = KaggleApi()
    api.authenticate()

    # Scarica nella cartella "path"
    api.dataset_download_files(dataset, path=path, unzip=True)

    print(f"✅ Dataset {dataset} scaricato in {path}")
