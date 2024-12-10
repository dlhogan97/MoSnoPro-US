import pytest
import dropbox
from mosnopro_us.data_manager import load_xarray_file_from_dropbox, load_pandas_df_from_dropbox
import pandas as pd
import xarray as xr

# Makes sure we get access to both the model data and the observations. 
def test_xarray_db_connection():
    # example site to test
    site="Paradise"
    db_xr_file = f"/Apps/push-and-pull-pysumma/output/_{site}_timestep.nc"  # Path to the xarray file in Dropbox

    # Test if the returned value from this function is an xarray dataset
    try:
        assert isinstance(load_xarray_file_from_dropbox(dropbox_file_path=db_xr_file),
                                                          xr.Dataset)
        print("Test passed for xarray!")
    except:
        TypeError("Model output dataset was not loaded correctly.")

def test_pandas_db_connection():
    # example site to test
    site="Paradise"
    db_pd_file = f"/Apps/push-and-pull-pysumma/snotel_csvs/{site}.csv" # Path to csv in Dropbox

    # Test if the returned value from this function is a pandas dataframe
    try:
        assert isinstance(load_pandas_df_from_dropbox(dropbox_file_path=db_pd_file),
                                                          pd.DataFrame)
        print("Test passed for pandas!")
    except:
        TypeError("SNOTEL data was not loaded correctly.")

# Testing exceptions for timeouts and retries.

# fake data is not available 
# Plan to move it forward 

# Makes sure the secrets are available.
def test_secrets():
    import streamlit as st
    # Test if the secrets are available
    try:
        assert st.secrets.db_credentials
        print("Test passed for secrets!")
    except:
        TypeError("Secrets are not available. Using example data instead.")

# Dropbox server is down or not avaiable. 
def test_dropbox_response():
    import dropbox
    # test that user info is returned
    try:
        # Assert that we get a simple dictionary back and can connect to dropbox
        assert isinstance(dropbox.Dropbox.users_get_current_account(), dict)
        print("Test passed for dropbox response!")
    except:
        TypeError("Dropbox response was not loaded correctly.")

# Testing validity of the data.
# Test if the data is valid by checking the shape of the data.

# Test if the data is valid by looking at extremes in the observed data

