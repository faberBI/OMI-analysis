import geopandas as gpd
import pandas as pd

def load_data(csv_path, shp_path):
    # Carica CSV dei valori
    omi = pd.read_csv(csv_path, sep=";")

    # Carica shapefile
    gdf = gpd.read_file(shp_path)

    # 🔎 Debug (utile la prima volta)
    # import streamlit as st
    # st.write("Colonne shapefile:", list(gdf.columns))

    # Merge sui campi corretti
    df = omi.merge(
        gdf[['COD_BELFIORE', 'ZONA_OMI', 'geometry']],
        how="left",
        left_on=['Comune_amm', 'Zona'],
        right_on=['COD_BELFIORE', 'ZONA_OMI']
    )

    # Rinomina per avere uniformità
    df = df.rename(columns={
        "COD_BELFIORE": "Belfiore",
        "ZONA_OMI": "Zona OMI"
    })

    return gpd.GeoDataFrame(df, geometry="geometry")

