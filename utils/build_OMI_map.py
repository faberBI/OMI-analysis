import zipfile
import os
import geopandas as gpd
import re


def extract_and_read_kml(zip_path, extract_to="extracted_files"):
    # Estrai i file dallo ZIP
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    # Trova tutti i file .kml nella cartella estratta
    kml_files = [os.path.join(root, file)
                 for root, _, files in os.walk(extract_to)
                 for file in files if file.endswith(".kml")]
    print('Numero di comuni in kml files:', len(kml_files))

    # Creazione di un GeoDataFrame vuoto
    all_gdfs = []

    # Leggi i file KML con geopandas e aggiungili al GeoDataFrame
    for kml_file in kml_files:
        try:
            print(f"Reading: {kml_file}")
            gdf = gpd.read_file(kml_file, driver="KML")
            gdf['Fonte'] = kml_file
            all_gdfs.append(gdf)
        except Exception as e:
            # Gestisce l'errore per il file specifico
            print(f"Errore per il file {kml_file}: {e}")

            # Prova a riparare il file KML (errore di encoding o altro)
            with open(kml_file, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()

            with open(kml_file, "w", encoding="utf-8") as f:
                f.write(content)

            # Riprova a leggere il file KML dopo averlo "riparato"
            try:
                gdf = gpd.read_file(kml_file, driver="KML")
                gdf['Fonte'] = kml_file
                all_gdfs.append(gdf)
            except Exception as e:
                print(f"Impossibile leggere il file {kml_file} anche dopo la correzione: {e}")

    # Concatenazione di tutti i GeoDataFrame
    if all_gdfs:
        final_gdf = gpd.pd.concat(all_gdfs, ignore_index=True)
        print(final_gdf.head())
        return final_gdf
    else:
        print("No KML files found.")
        return None

