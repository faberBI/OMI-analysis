import geopandas as gpd
import pandas as pd

def load_data(omi_path: str, gdf_path: str) -> gpd.GeoDataFrame:
    """
    Carica il CSV dei valori OMI e il GeoDataFrame con le geometrie.
    """
    # Carica valori OMI
    omi = pd.read_csv(omi_path, sep=';')

    # Carica geometrie zone OMI
    gdf = gpd.read_file(gdf_path)

    # Merge dati OMI + geometrie
    df = omi.merge(
        gdf[['Belfiore', 'Zona OMI', 'geometry']],
        how='left',
        left_on=['Comune_amm', 'Zona'],
        right_on=['Belfiore', 'Zona OMI']
    )

    return gpd.GeoDataFrame(df, geometry="geometry")
