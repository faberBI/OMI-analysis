import streamlit as st
import folium
from streamlit_folium import st_folium
import os

from modules.data_loader import load_data
from modules.geocode import geocode_address
from modules.omi_utils import find_omi_zone
from modules.download_data import download_from_kaggle


# ============================
# 1. CARICAMENTO DATI
# ============================

@st.cache_data
def get_data():
    shp_path = "data/ZONE_OMI_2_2024.shp"

    # Scarica shapefile se non c’è
    if not os.path.exists(shp_path):
        download_from_kaggle("faberbi/zone-omi-2-sem-2024", "data")

    # Cerca il CSV dentro tutte le sottocartelle di data/
    csv_path = None
    for root, dirs, files in os.walk("data"):
        for f in files:
            if f == "QI_20242_VALORI.csv":
                csv_path = os.path.join(root, f)
                break

    # Se non trovato → scarica da Kaggle
    if csv_path is None:
        download_from_kaggle("faberbi/qi-20242-valori", "data")
        for root, dirs, files in os.walk("data"):
            for f in files:
                if f == "QI_20242_VALORI.csv":
                    csv_path = os.path.join(root, f)
                    break

    if csv_path is None:
        raise FileNotFoundError("Non trovo QI_20242_VALORI.csv nemmeno dopo il download.")

    return load_data(csv_path, shp_path)





# ============================
# 2. INTERFACCIA STREAMLIT
# ============================
st.title("🏠 Analisi Immobiliare con Zone OMI")
st.markdown("Inserisci un indirizzo per ottenere la zona OMI e i valori associati.")

indirizzo = st.text_input("📍 Inserisci indirizzo (es. 'Via Roma 10, Milano')")

if indirizzo:
    lat, lon = geocode_address(indirizzo)

    if lat and lon:
        st.success(f"Coordinate trovate: {lat:.6f}, {lon:.6f}")

        zona = find_omi_zone(lat, lon, gdf)

        if zona is not None:
            st.subheader("📊 Informazioni sulla Zona OMI")
            st.write(f"**Comune:** {zona['Comune_amm']}")
            st.write(f"**Zona OMI:** {zona['Zona']}")
            st.dataframe(zona.drop("geometry").to_frame().T)

            # Mappa
            m = folium.Map(location=[lat, lon], zoom_start=15)
            folium.GeoJson(zona['geometry'], name="Zona OMI").add_to(m)
            folium.Marker([lat, lon], tooltip="Immobile").add_to(m)
            st_folium(m, width=700, height=500)
        else:
            st.error("❌ L'indirizzo non ricade in nessuna zona OMI.")
    else:
        st.error("Impossibile geolocalizzare l'indirizzo. Riprova.")
