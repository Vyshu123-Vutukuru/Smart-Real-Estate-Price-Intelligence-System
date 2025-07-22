from geopy.geocoders import Nominatim

def get_coordinates(location):
    geolocator = Nominatim(user_agent="geoapi")
    loc = geolocator.geocode(location)
    if loc:
        return loc.latitude, loc.longitude
    return None, None
