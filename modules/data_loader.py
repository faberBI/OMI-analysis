import geopandas as gpd
import pandas as pd

def load_data(csv_path, shp_path):
    # Carica CSV valori OMI
    df = pd.read_csv(csv_path, sep=";")

    # Uniforma i nomi chiave nel CSV
    df = df.rename(columns={
        "Comune_amm": "COD_BELFIORE",
        "Zona": "ZONA_OMI"
    })

    # Carica shapefile OMI
    gdf = gpd.read_file(shp_path)

    # Uniforma i nomi chiave nello shapefile
    gdf = gdf.rename(columns={
        "Belfiore": "COD_BELFIORE",
        "Zona OMI": "ZONA_OMI"
    })

    # Merge shapefile + CSV sul codice Belfiore + Zona
    merged = gdf.merge(
        df,
        how="left",
        on=["COD_BELFIORE", "ZONA_OMI"]
    )

    merged = gpd.GeoDataFrame(merged, geometry = 'geometry')
    return merged

