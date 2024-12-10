import pytest
import dropbox
from mosnopro_us.data_manager import *
import pandas as pd
import xarray as xr
import streamlit as st
import os

# Makes sure we get access to both the model data and the observations. 
def test_xarray_db_connection():
    # example site to test
    site="Paradise"

    # if secrets are available, use the dropbox file path
    if os.path.exists('../../.streamlit/secrets.toml'):
        db_xr_file = f"/Apps/push-and-pull-pysumma/output/_{site}_timestep.nc"  # Path to the xarray file in Dropbox
        ds = load_xarray_file_from_dropbox(dropbox_file_path=db_xr_file)
    else:
        db_xr_file = f"../../data/example_data/output/_{site}_timestep.nc"
        ds = load_xarray_file_from_examples(db_xr_file)

    # Test if the returned value from this function is an xarray dataset
    try:
        assert isinstance(ds, xr.Dataset)
        print("Test passed for xarray!")
    except:
        TypeError("Model output dataset was not loaded correctly.")

def test_pandas_db_connection():
    # example site to test
    site="Paradise"
    if os.path.exists('../../.streamlit/secrets.toml'):
        db_pd_file = f"/Apps/push-and-pull-pysumma/snotel_csvs/{site}.csv" # Path to csv in Dropbox
        df = load_pandas_df_from_dropbox(dropbox_file_path=db_pd_file)
    else:
        db_pd_file = f"../../data/example_data/snotel_csvs/{site}.csv"
        df = load_pandas_file_from_examples(db_pd_file)

    # Test if the returned value from this function is a pandas dataframe
    try:
        assert isinstance(df, pd.DataFrame)
        print("Test passed for pandas!")
    except:
        TypeError("SNOTEL data was not loaded correctly.")

# Makes sure the secrets are available if db_credentials are available.
def test_secrets():
# Test if the secrets are available
    if os.path.exists('../../.streamlit/secrets.toml'):
        try:
            assert st.secrets.db_credentials
            print("Test passed for secrets!")
        except:
            FileNotFoundError("Secrets are not available. Reach out to authors for credentials.")
    else:
        print("Secrets are not available. Using example data instead. Reach out to authors for credentials.")

# Dropbox server is down or not avaiable. 
def test_dropbox_response():
    import dropbox
    if os.path.exists('../../.streamlit/secrets.toml'):
        token = st.secrets.db_credentials.refresh_token
        app_key = st.secrets.db_credentials.APP_KEY
        app_secret = st.secrets.db_credentials.APP_SECRET
        try:
            # Initialize Dropbox client
            dbx = dropbox.Dropbox(app_key=app_key,
                                app_secret=app_secret,
                                oauth2_refresh_token=token,
                                max_retries_on_error=4)
            assert isinstance(dbx.users_get_current_account(), dict)
            print("Test passed for dropbox response!")
        except:
            ConnectionRefusedError("Dropbox response was not loaded correctly.")
    else:
        print("Secrets are not available. Using example data instead. Reach out to authors for credentials.")

# Testing validity of the data. Run these tests on example data
def test_lengths_match():
    df = pd.DataFrame({
        'value': [1, 2, 3, 4, 5],
    }, index=pd.date_range('2023-01-01', periods=5, freq='h'))

    ds = xr.Dataset({
        'value': (['time'], [1, 2, 3])
    }, coords={'time': pd.date_range('2023-01-01', periods=3)})

    assert check_lengths_match(df, ds, extra_length=2) is True

def test_lengths_do_not_match():
    df = pd.DataFrame({
        'value': [1, 2],
    }, index=pd.date_range('2023-01-01', periods=2))

    ds = xr.Dataset({
        'value': (['time'], [1, 2, 3])
    }, coords={'time': pd.date_range('2023-01-01', periods=3)})

    assert check_lengths_match(df, ds) is False

def test_empty_dataframe():
    df = pd.DataFrame(columns=['value'])
    ds = xr.Dataset({
        'value': (['time'], []),
    }, coords={'time': []})
    assert check_lengths_match(df, ds) is True

def test_missing_time_dimension():
    df = pd.DataFrame({
        'value': [1, 2, 3],
    }, index=pd.date_range('2023-01-01', periods=3))

    ds = xr.Dataset({
        'value': (['x'], [1, 2, 3]),
    }, coords={'x': [0, 1, 2]})

    with pytest.raises(KeyError):
        check_lengths_match(df, ds)

# test one of the example files to make sure it will work
def test_example_dimension():
    site = "Paradise"
    db_xr_file = f"../../data/example_data/output/_{site}_timestep.nc"
    db_pd_file = f"../../data/example_data/snotel_csvs/{site}.csv"
    ds = load_xarray_file_from_examples(db_xr_file)
    df = load_pandas_file_from_examples(db_pd_file)
    # test the dimesion match
    assert check_lengths_match(df, ds) 

# Test if the data is valid by looking at extremes in the observed data

# test that the max SNOWDEPTH is less than 20 meters
def test_max_values():
    site = "Paradise"
    db_xr_file = f"../../data/example_data/output/_{site}_timestep.nc"
    db_pd_file = f"../../data/example_data/snotel_csvs/{site}.csv"
    ds = load_xarray_file_from_examples(db_xr_file)
    df = load_pandas_file_from_examples(db_pd_file)
    
    assert (df['SNOWDEPTH'].max() < 20*100) & (ds['scalarSnowDepth'].max() < 20)

def test_min_values():
    import datetime as dt
    site = "Wells_Creek"
    db_xr_file = f"../../data/example_data/output/_{site}_timestep.nc"
    db_pd_file = f"../../data/example_data/snotel_csvs/{site}.csv"
    ds = load_xarray_file_from_examples(db_xr_file)
    df = load_pandas_file_from_examples(db_pd_file)

    # make sure we get values near zero for this data
    min_time = pd.to_datetime(ds.time.values.min())
    df_snow = get_snotel_depth(df, min_time)
    # drop all NaN and test to see if min values are greater than 0
    assert (df_snow.min() == 0) & (ds['scalarSnowDepth'].where(~ds['scalarSnowDepth'].isnull().all()).min() == 0)