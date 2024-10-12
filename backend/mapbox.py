from geopy.geocoders import MapBox


MAPBOX_API = "pk.eyJ1IjoiZ3NpZ21hdSIsImEiOiJjbTI2YjJ1MmswaXcwMmtwemdpaGQ5c3VhIn0.cndahCtzuJv1LbxarbUt_Q"


def get_coordinates(location):
    # location = "Fairfax, VA"
    geolocator = MapBox(api_key=MAPBOX_API)
    location = geolocator.geocode(location)
    return location.latitude, location.longitude