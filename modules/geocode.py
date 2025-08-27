from geopy.geocoders import Nominatim
import time

def geocode_address(address):
    geolocator = Nominatim(user_agent="omi-analysis")
    for i in range(3):  # retry fino a 3 volte
        try:
            return geolocator.geocode(address, timeout=10)
        except Exception as e:
            time.sleep(5)
    return None
