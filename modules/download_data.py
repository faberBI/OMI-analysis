from kaggle.api.kaggle_api_extended import KaggleApi
import os

def download_from_kaggle(dataset: str, path: str = "data"):
    if not os.path.exists(path):
        os.makedirs(path)

    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(dataset, path=path, unzip=True)
    print(f"✅ Dataset {dataset} scaricato in {path}")
