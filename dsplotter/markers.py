# dsplotter/markers.py

import folium
import matplotlib.colors as mcolors
import branca.colormap as cm

def add_markers(gdf, m, color_col, radius_col, radius_scale, scalar_map, cmap):
    '''
    Adds markers to the map.

    Parameters
    ----------
    gdf : gpd.GeoDataFrame
        The geodataframe containing the data to be plotted.
    m : folium.Map
        The folium map object.
    color_col : str
        The name of the column in the dataframe to use for color.
    radius_col : str
        The name of the column in the dataframe to use for radius.
    radius_scale : int
        Scale factor for the radius of the markers.
    '''
    def map_value_to_color(value):
        return mcolors.to_hex(scalar_map.to_rgba(value))
    
    gdf['radius_norm'] = (gdf[radius_col] - gdf[radius_col].min()) / (gdf[radius_col].max() - gdf[radius_col].min())
    for idx, row in gdf.iterrows():
        popup_content = "<b>Details:</b><br>"
        for key, value in row.items():
            if key not in ['latitude', 'longitude', 'geometry', 'color', 'radius_norm']:
                popup_content += f"<b>{key.capitalize()}:</b> {value}<br>"
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=5 + radius_scale * row['radius_norm'],
            color=map_value_to_color(row[color_col]),
            fill=True,
            fill_color=map_value_to_color(row[color_col]),
            fill_opacity=0.9,
            popup=popup_content
        ).add_to(m)
    
    colormap = cm.LinearColormap(
        colors=[cmap(i) for i in range(cmap.N)],
        vmin=gdf[color_col].min(),
        vmax=gdf[color_col].max(),
        caption=color_col
    )
    colormap.add_to(m)
