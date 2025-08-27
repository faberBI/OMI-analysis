from geopy.geocoders import Nominatim

def geocode_address(address: str):
    """
    Geocodifica un indirizzo in (lat, lon) usando Nominatim.
    """
    geolocator = Nominatim(user_agent="omi_app")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    return None, None
