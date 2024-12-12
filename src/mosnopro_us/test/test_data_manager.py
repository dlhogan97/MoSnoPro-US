import pytest
from mosnopro_us.data_manager import load_xarray_file_from_dropbox, load_pandas_df_from_dropbox, \
    load_xarray_file_from_examples, load_pandas_file_from_examples, check_lengths_match, get_snotel_depth
import pandas as pd
import xarray as xr
import streamlit as st
import os
import unittest


def test_xarray_db_connection():
    """
    Makes sure we get access to both the SUMMA model data and the observations.
    [One-shot test]
    """
    # example site to test
    site = "Paradise"

    # if secrets are available, use the dropbox file path
    if os.path.exists('~/../../.streamlit/secrets.toml'):
        db_xr_file = f"/Apps/push-and-pull-pysumma/output/_{site}_timestep.nc"  # Path to the xarray file in Dropbox
        ds = load_xarray_file_from_dropbox(dropbox_file_path=db_xr_file)
    else:
        db_xr_file = f"output/_{site}_timestep.nc"
        ds = load_xarray_file_from_examples(db_xr_file)

    # Test if the returned value from this function is an xarray dataset
    try:
        assert isinstance(ds, xr.Dataset)
        print("Test passed for xarray!")
    except Exception:
        # make sure a ValueError is raised
        unittest.TestCase.assertRaises(ValueError, load_xarray_file_from_examples, db_xr_file)


def test_pandas_db_connection():
    """
    Makes sure csv was correctly converted to pandas df
    [one-shot test]
    """
    # example site to test
    site = "Paradise"
    if os.path.exists('../../../.streamlit/secrets.toml'):
        db_pd_file = f"/Apps/push-and-pull-pysumma/snotel_csvs/{site}.csv"  # Path to csv in Dropbox
        df = load_pandas_df_from_dropbox(dropbox_file_path=db_pd_file)
    else:
        db_pd_file = f"snotel_csvs/{site}.csv"
        df = load_pandas_file_from_examples(db_pd_file)

    # Test if the returned value from this function is a pandas dataframe
    try:
        assert isinstance(df, pd.DataFrame)
        print("Test passed for pandas!")
    except Exception:
        TypeError("SNOTEL data was not loaded correctly.")


def test_secrets():
    """
    Makes sure the secrets are available if db_credentials are available.
    [one-shot test]
    """
    # Test if the secrets are available
    if os.path.exists('~/../../../.streamlit/secrets.toml'):
        try:
            assert st.secrets.db_credentials
            print("Test passed for secrets!")
        except Exception:
            assert pytest.raises(FileNotFoundError)
    else:
        assert pytest.raises(FileNotFoundError)
        print("Secrets are not available. Using example data instead. Reach out to authors for credentials.")


def test_dropbox_response():
    """
    Case when Dropbox server is down or not available.
    [edge test]
    """
    import dropbox
    if os.path.exists('~/../../../.streamlit/secrets.toml'):
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
        except Exception:
            assert pytest.raises(ConnectionRefusedError)
    else:
        assert pytest.raises(FileNotFoundError)


# Testing validity of the data. Run these tests on example data
# Suite of pattern tests
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
    db_xr_file = f"output/_{site}_timestep.nc"
    db_pd_file = f"snotel_csvs/{site}.csv"
    ds = load_xarray_file_from_examples(db_xr_file)
    df = load_pandas_file_from_examples(db_pd_file)
    # test the dimesion match
    assert check_lengths_match(df, ds)


def test_non_existent_site():
    """
    Case when a non-existent datafile is referenced.
    [edge test]
    """
    site = "NonExistentSite"
    db_xr_file = f"output/_{site}_timestep.nc"
    db_pd_file = f"snotel_csvs/{site}.csv"
    # test that the file doesn't exist
    with pytest.raises(FileNotFoundError):
        load_xarray_file_from_examples(db_xr_file)
    with pytest.raises(FileNotFoundError):
        load_pandas_file_from_examples(db_pd_file)


def test_max_values():
    """
    Checks if data are valid by looking at extremes (max depth is <20 meters) in observed data.
    [edge test]
    """
    site = "Paradise"
    db_xr_file = f"output/_{site}_timestep.nc"
    db_pd_file = f"snotel_csvs/{site}.csv"
    ds = load_xarray_file_from_examples(db_xr_file)
    df = load_pandas_file_from_examples(db_pd_file)

    assert (df['SNOWDEPTH'].max() < 20*100) & (ds['scalarSnowDepth'].max() < 20)


def test_min_values():
    """
    Checks if data are valid (if they have successfully be processed to be close to 0 m).
    [edge test]
    """
    site = "Wells_Creek"
    db_xr_file = f"output/_{site}_timestep.nc"
    db_pd_file = f"snotel_csvs/{site}.csv"
    ds = load_xarray_file_from_examples(db_xr_file)
    df = load_pandas_file_from_examples(db_pd_file)

    # make sure we get values near zero for this data
    min_time = pd.to_datetime(ds.time.values.min())
    df_snow = get_snotel_depth(df, min_time)
    # drop all NaN and test to see if min values are greater than 0
    assert (df_snow.min() == 0) & (ds['scalarSnowDepth'].where(~ds['scalarSnowDepth'].isnull().all()).min() == 0)
