import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import fiona
fiona.os.environ['SHAPE_RESTORE_SHX'] = 'YES'

def generate_map(shape, dataset):
    geometry = [Point(xy) for xy in zip(dataset['long'], dataset['lat'])]
    gdf = gpd.GeoDataFrame(dataset, geometry=geometry)
    gdf.crs = "EPSG:4326"
    boundaries = gpd.read_file(shape)
    base = boundaries.plot(figsize =(15, 15), aspect=1, color = 'white', edgecolor='black')
    gdf.plot(ax=base, markersize=10, aspect=1, cmap="Dark2",column='prediction_plot', legend=True)
    map_plot = plt.savefig('my_plot.png')
    return map_plot
