# dsplotter/geodata.py

import geopandas as gpd

def prepare_geodata(data):
    '''
    Prepares the GeoDataFrame from the input data.

    Parameters
    ----------
    data : pandas.DataFrame
        The dataframe containing the data to be plotted. Must (!) contain longitude and latitude column.

    Returns
    -------
    gpd.GeoDataFrame
    '''
    if 'longitude' not in data.columns:
        longitude_col = data.columns[~data.columns.str.find('longitude').values.astype(bool)][0]
        print(f'Use column {longitude_col} for the longitude coordinate.')
    else:
        longitude_col = 'longitude'
    if 'latitude' not in data.columns:
        latitude_col = data.columns[~data.columns.str.find('latitude').values.astype(bool)][0]
        print(f' Use the column {latitude_col} for the latitude coordinate.')        
    else:
        latitude_col = 'latitude'
    data.rename(columns={longitude_col: 'longitude', latitude_col: 'latitude'}, inplace=True)
    gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data['longitude'], data['latitude']), crs="EPSG:4326")
    return gdf
