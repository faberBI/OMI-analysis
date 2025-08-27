import os
import subprocess

def download_from_kaggle(dataset: str, path: str = "data"):
    """
    Scarica un dataset da Kaggle nella cartella data/.
    Richiede 'kaggle' CLI installata e API Key configurata (~/.kaggle/kaggle.json).
    
    :param dataset: nome del dataset Kaggle, es. "username/zone-omi-2024"
    :param path: cartella di destinazione
    """
    if not os.path.exists(path):
        os.makedirs(path)

    # scarica con kaggle CLI
    subprocess.run([
        "kaggle", "datasets", "download", "-d", dataset, "-p", path, "--unzip"
    ], check=True)

    print(f"✅ Dataset {dataset} scaricato in {path}")
