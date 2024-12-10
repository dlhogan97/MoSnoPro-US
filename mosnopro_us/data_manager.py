import geopandas as gpd
import pandas as pd
import xarray as xr
import numpy as np
import importlib.resources as pkg_resources
import dropbox
import io
import streamlit as st
import os


def load_geojson(file_name):
    """
    Dynamically load a GeoJSON file from the `data` directory.

    Parameters:
    - file_name (str): Name of the GeoJSON file to load.

    Returns:
    - GeoDataFrame: A GeoPandas DataFrame containing the data from the GeoJSON file.

    Raises:
    - ValueError: If the file cannot be loaded or doesn't exist.

    """
    try:
        # Dynamically construct the file path relative to this script's location
        base_dir = os.path.dirname(__file__)  # Directory of the current script
        data_dir = os.path.join(base_dir, "../data")  # Subdirectory containing data files
        file_path = os.path.join(data_dir, file_name)

        # Load the GeoJSON file using GeoPandas
        return gpd.read_file(file_path)
    except Exception as e:
        raise ValueError(f"Error loading GeoJSON file '{file_name}': {e}")



def load_snotel_points():
    """
    Reads and returns geospatial data for SNOTEL points (Snow Telemetry monitoring stations) in Washington state from a GeoJSON file.

    Parameters:
    - "WA_snotel_points.geojson" pre-set data, outputted from load_geojson function

    Returns:
    - GeoJSON object/dict containing SNOTEL point data.
    """
    return load_geojson("WA_snotel_points.geojson")


def load_washington_boundary():
    """
    Reads and returns the geospatial boundary data for Washington state.

    Parameters:
    - Outputs from load_geojson function

    Returns:
    - GeoJSON object/dict containing boundary data for Washington state
    """
    return load_geojson("washington.geojson")


def load_snow_depth_data(file_path):
    """
    Reads snow depth data from a CSV file. Parses "Date" column as datetime objects.

    Parameters:
    - file_name (str): Name of the CSV file to load.

    Returns:
    - DataFrame containing the datatime objects.

    Raises:
    - ValueError: If the file cannot be loaded or doesn't exist.
    """
    try:
        return pd.read_csv(file_path, parse_dates=["Date"])
    except Exception as e:
        raise ValueError(f"Error loading snow depth data : {e}")


def summarize_snotel_points(gdf):
    """
    Extracts key attributes ("demographics") from SNOTEL sites.

    Parameters:
    - GeoDataFrame: containing SNOTEL point data with all columns

    Returns:
    - GeoDataFrame: containing only Name, Elevation, Latitude, Longitude columns
    """
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

        # Load the file content as an pandas dataframe
        df = pd.read_csv(file_content, index_col=0,
                         parse_dates=True, date_format='%Y-%m-%d %H:%M:%S')
        df.index = pd.to_datetime(df.index)
        df.index = df.index.tz_localize(None)
        return df
    except Exception as e:
        raise RuntimeError(f"Failed to read file from Dropbox: {e}")

def load_pandas_file_from_examples(file_name):
    """
    Loads a CSV file from the `examples` directory.

    Parameters:
    - file_name (str): Name of the CSV file to load.

    Returns:
    - pd.DataFrame: A pandas DataFrame containing the data from the CSV file.

    Raises:
    - ValueError: If the file cannot be loaded or doesn't exist.

    """
    try:
        # Dynamically construct the file path relative to this script's location
        base_dir = os.path.dirname(__file__)  # Directory of the current script
        data_dir = os.path.join(base_dir, "../data/example_data/")  # Subdirectory containing data files
        file_path = os.path.join(data_dir, file_name)

        # Load the CSV file using pandas
        df = pd.read_csv(file_path, index_col=0,
                         parse_dates=True, date_format='%Y-%m-%d %H:%M:%S')
        df.index = pd.to_datetime(df.index)
        df.index = df.index.tz_localize(None)
        return df
    except Exception as e:
        raise ValueError(f"Error loading CSV file '{file_name}': {e}")

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

def load_xarray_file_from_examples(file_name):
    """
    Loads an xarray file from the `examples` directory.

    Parameters:
    - file_name (str): Name of the xarray file to load.

    Returns:
    - xr.Dataset: An xarray Dataset containing the data from the file.

    Raises:
    - ValueError: If the file cannot be loaded or doesn't exist.

    """
    try:
        # Dynamically construct the file path relative to this script's location
        base_dir = os.path.dirname(__file__)  # Directory of the current script
        data_dir = os.path.join(base_dir, "../data/example_data/")  # Subdirectory containing data files
        file_path = os.path.join(data_dir, file_name)

        # Load the xarray file using xarray
        ds = xr.open_dataset(file_path)
        return ds 
    except Exception as e:
        raise ValueError(f"Error loading xarray file '{file_name}': {e}")
    
def check_lengths_match(dataframe, dataset, time_dimension='time', extra_length=2148):
    """
    Check if the length of the DataFrame index matches the length of the Dataset's time dimension.
    
    Parameters:
        dataframe (pd.DataFrame): The dataframe to compare.
        dataset (xr.Dataset): The dataset to compare.
        time_dimension (str): The name of the time dimension in the dataset.
        extra_length (int): Number of timesteps that the dataframe has for runup that are greater than the model output
    
    Returns:
        bool: True if lengths match, False otherwise.
    """
    df_length = len(dataframe.iloc[extra_length:])
    ds_length = len(dataset[time_dimension])
    return df_length == ds_length

def get_snotel_depth(df, min_time):
    """
    This function processes daily snow depth observations from SNOTEL sites and returns it as a pandas series. It performs the following steps: 
        - Filters data to include records from `min_time` onwards (specified by user)
        - Cleans out-of-range data by replacing negative values with 0 and values with large sudden changes (>25) with NaN to be interpolated linearly
        - Takes maximum snow depth daily
        - Converts from inches to meters

    Parameters:
    - df: SNOTEL dataframe with observation data

    Returns:
    - pandas.Series: time series of daily snow depth observations (meters)
    """
    # get snotel observation depth
    snow_depth_obs = df.loc[min_time:]['SNOWDEPTH'].resample('1D').max().shift() * 2.54/100
    # replace below zero values with 0
    snow_depth_obs[snow_depth_obs < 0] = 0
    # replace nan values with nan
    snow_depth_obs[abs(snow_depth_obs.diff()) > 25] = np.nan
    # interpolate missing values
    snow_depth_obs = snow_depth_obs.interpolate()
    return snow_depth_obs