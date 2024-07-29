# dsplotter/plot_map.py

from .geodata import prepare_geodata
from .map_creation import create_map
from .color_mapping import create_color_mapping
from .markers import add_markers
from IPython.display import display
import folium

def plot_map(data, color_col, radius_col=None, radius_scale=10, alpha=0.9):
    '''
    Plots an interactive map of Goettingen and sets location markers according to the 'longitude' and 'latitude' column in the given dataframe. 
    The appearance of the location marker can be adjusted in color and radius by other columns in the given dataframe. 
    The radius scale and the opacity can also be adjusted separately.

    Parameters
    ----------
    data : pandas.DataFrame
        The dataframe containing the data to be plotted. Must (!) contain longitude and latitude column.
    color_col : str
        The name of the column in the dataframe to use for color.
    radius_col : str, optional
        The name of the column in the dataframe to use for radius. If none is given, the radius is a constant value. Default: None
    radius_scale : float, optional
        A scalar value to increase or decrease the radius of all location markers
    alpha : float
        The opacity value for the location markers
    '''
    
    gdf = prepare_geodata(data)
    if radius_col is None:
        gdf['radius_col'] = [1.]*gdf.shape[0]
        radius_col = 'radius_col'
    m = create_map()
    scalar_map, cmap = create_color_mapping(gdf, color_col)
    add_markers(gdf, m, color_col, radius_col, radius_scale, alpha, scalar_map, cmap)

    display(m)
