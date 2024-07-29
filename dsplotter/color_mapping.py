# dsplotter/color_mapping.py

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import branca.colormap as cm

def create_color_mapping(gdf, color_col):
    '''
    Creates a colormap and normalization for the color values.

    Parameters
    ----------
    gdf : gpd.GeoDataFrame
        The geodataframe containing the data to be plotted.
    color_col : str
        The name of the column in the dataframe to use for color.

    Returns
    -------
    scalar_map : matplotlib.cm.ScalarMappable
    cmap : matplotlib.colors.Colormap
    '''
    cmap = plt.cm.coolwarm
    norm = mcolors.Normalize(vmin=gdf[color_col].min(), vmax=gdf[color_col].max())
    scalar_map = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
    return scalar_map, cmap
