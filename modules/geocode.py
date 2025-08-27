from geopy.geocoders import Nominatim
import time

def geocode_address(address):
    geolocator = Nominatim(user_agent="omi-analysis")
    for i in range(3):  # retry fino a 3 volte
        try:
            location = geolocator.geocode(address, timeout=10)
            if location:
                return location.latitude, location.longitude
        except Exception:
            time.sleep(5)
    return None, None
