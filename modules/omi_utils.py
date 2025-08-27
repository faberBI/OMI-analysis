from shapely.geometry import Point
import geopandas as gpd

def find_omi_zone(lat: float, lon: float, gdf: gpd.GeoDataFrame):
    """
    Trova la zona OMI in cui ricade un punto (lat, lon).
    """
    point = Point(lon, lat)  # shapely usa (x=lon, y=lat)
    for _, row in gdf.iterrows():
        if row['geometry'] and row['geometry'].contains(point):
            return row
    return None
