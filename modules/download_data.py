import os
import subprocess

def download_from_kaggle(dataset: str, path: str = "data"):
    """
    Scarica un dataset da Kaggle nella cartella indicata.
    Richiede la CLI 'kaggle' configurata correttamente con API key.
    """
    if not os.path.exists(path):
        os.makedirs(path)

    print(f"Scaricando il dataset {dataset}...")
    subprocess.run([
        "kaggle", "datasets", "download", "-d", dataset,
        "-p", path, "--unzip"
    ], check=True)
    print(f"Dataset {dataset} scaricato e decompresso in '{path}'.")

