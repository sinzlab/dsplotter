# dsplotter/map_creation.py

import folium

def create_map():
    '''
    Initializes the folium map centered around Goettingen coordinates.

    Returns
    -------
    folium.Map
    '''
    goe_lat = 51.5322
    goe_long = 9.9368
    return folium.Map(location=[goe_lat, goe_long], zoom_start=15)
