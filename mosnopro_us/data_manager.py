import geopandas as gpd
import pandas as pd
import xarray as xr
import importlib.resources as pkg_resources
import data
import dropbox
import io
import streamlit as st


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


def load_pandas_df_from_dropbox(dropbox_file_path):
    """
    Reads an csv file directly from Dropbox into memory.

    Parameters:
        dropbox_file_path (str): Path to the file in Dropbox
        (e.g., '/folder/file.nc').
        access_token (str): Dropbox API access token.

    Returns:
        pandas.DataFrame: Loaded dataset.
    """
    token = st.secrets.db_credentials.refresh_token
    app_key = st.secrets.db_credentials.APP_KEY
    app_secret = st.secrets.db_credentials.APP_SECRET
    try:
        # Initialize Dropbox client
        dbx = dropbox.Dropbox(app_key=app_key,
                              app_secret=app_secret,
                              oauth2_refresh_token=token)

        # Download the file content into memory
        metadata, res = dbx.files_download(dropbox_file_path)
        file_content = io.BytesIO(res.content)

        # Load the file content as an xarray dataset
        df = pd.read_csv(file_content, index_col=0,
                         parse_dates=True, date_format='%Y-%m-%d %H:%M:%S')
        df.index = pd.to_datetime(df.index)
        df.index = df.index.tz_localize(None)
        return df
    except Exception as e:
        raise RuntimeError(f"Failed to read file from Dropbox: {e}")


def load_xarray_file_from_dropbox(dropbox_file_path):
    """
    Reads an xarray file directly from Dropbox into memory.

    Parameters:
        dropbox_file_path (str): Path to the file in Dropbox
        (e.g., '/folder/file.nc').
        access_token (str): Dropbox API access token.

    Returns:
        xarray.Dataset: Loaded dataset.
    """
    token = st.secrets.db_credentials.refresh_token
    app_key = st.secrets.db_credentials.APP_KEY
    app_secret = st.secrets.db_credentials.APP_SECRET
    try:
        # Initialize Dropbox client
        dbx = dropbox.Dropbox(app_key=app_key,
                              app_secret=app_secret,
                              oauth2_refresh_token=token)

        # Download the file content into memory
        metadata, res = dbx.files_download(dropbox_file_path)
        file_content = io.BytesIO(res.content)

        # Load the file content as an xarray dataset
        dataset = xr.open_dataset(file_content)
        return dataset
    except Exception as e:
        raise RuntimeError(f"Failed to read file from Dropbox: {e}")
