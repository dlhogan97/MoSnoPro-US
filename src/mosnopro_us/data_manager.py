import geopandas as gpd
import pandas as pd
import importlib.resources as pkg_resources
from src.mosnopro_us import data

def load_geojson(file_name):
    try:
        with pkg_resources.files(data).joinpath(file_name).open("r") as f:
            return gpd.read_file(f)
    except Exception as e:
        raise ValueError(f"Error loading GeoJSON file '{file_name}': {e}")
    
def load_snotel_points():
    return load_geojson("WA_snotel_points.geojson")

def load_washington_boundary():
    return load_geojson("washington.geojson")

def load_snow_depth_data(file_path):
    try:
        return pd.read_csv(file_path, parse_dates=["Date"])
    except Exception as e:
        raise ValueError(f"Error loading snow depth data : {e}")

def summarize_snotel_points(gdf):
    return gdf[["Name", "Elevation", "Latitude", "Longitude"]]

