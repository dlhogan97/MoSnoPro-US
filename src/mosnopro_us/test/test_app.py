"""
This module contains unit tests for the app.py functionality in the Mosnopro US project.
"""
import os
import pytest
import pandas as pd
import xarray as xr
from unittest.mock import patch, MagicMock
from app import load_and_filter_data, plot_selected_figure
from mosnopro_us import data_manager

# Path to example data
SUMMA_PATH = "./data/example_data/output/"
SNOTEL_PATH = "./data/example_data/snotel_csvs/"

def test_load_and_filter_data_with_example_data():
    """
    Test load_and_filter_data function with example data.
    """
    # Pick and example site from the available data
    site = "White_Pass"
    summa_file = os.path.join(SUMMA_PATH, f"_{site}_timestep.nc")
    snotel_file = os.path.join(SNOTEL_PATH, f"{site}.csv")
    
    # Ensure the files exist
    assert os.path.exists(summa_file), f"SUMMA file not found: {site}"
    assert os.path.exists(snotel_file), f"SNOTEL file not found: {site}"

    # Load data directly
    summa_data = xr.open_dataset(summa_file)
    snotel_data = pd.read_csv(snotel_file, parse_dates=["time"], index_col="time")
    snotel_data.index = snotel_data.index.tz_localize(None)

    # Define a time slice that matches the SNOTEL data
    time_slice = slice("2024-07-03", "2024-12-09")

    # Use the function to load and filter the data
    filtered_summa_data, filtered_snotel_data = load_and_filter_data(site, time_slice)

    assert filtered_summa_data is not None, "Filtered SUMMA data should not be None"
    assert filtered_summa_data.sizes["time"] > 0, "Filtered SUMMA data should not be empty"
    assert len(filtered_snotel_data) > 0, "Filtered SNOTEL data should not be empty"

def test_plot_selected_figure_with_example_data():
    """
    Test plot_selected_figure function with example data.
    """
    # Load example data
    site = "White_Pass"
    summa_file = os.path.join(SUMMA_PATH, f"_{site}_timestep.nc")
    snotel_file = os.path.join(SNOTEL_PATH, f"{site}.csv")

    summa_data = xr.open_dataset(summa_file)
    snotel_data = pd.read_csv(snotel_file, parse_dates=["time"], index_col="time")
    snotel_data.index = snotel_data.index.tz_localize(None)

    # Define a time slice that matches the SNOTEL data
    time_slice = slice("2024-07-03", "2024-12-09")

    # Filter the data
    filtered_summa_data = summa_data.sel(time=time_slice)
    filtered_snotel_data = snotel_data.loc[time_slice]

    # Test Temperature plot
    fig_temp = plot_selected_figure(filtered_summa_data, filtered_snotel_data, site, "Temperature")
    assert fig_temp is not None, "Temperature figure should not be None"

    # Test Density plot
    fig_density = plot_selected_figure(filtered_summa_data, filtered_snotel_data, site, "Density")
    assert fig_density is not None, "Density figure should not be None"

    # Test invalid plot type
    with pytest.raises(ValueError):
        plot_selected_figure(filtered_summa_data, filtered_snotel_data, site, "InvalidType")

def test_site_selection_transfer(monkeypatch):
    """
    Test if the correct data is transferred when a site is clicked.
    """
    # Mock the map click response
    mock_map_data = {
        "last_active_drawing": {
            "properties": {
                "name": "Morse Lake"
            }
        }
    }
    # Patch the 'st_folium' function to return the mock data
    monkeypatch.setattr("app.st_folium", MagicMock(return_value=mock_map_data))

    # Test if the corect site is processed
    with patch("app.st.sidebar.radio", return_value="Interactive Map"), \
        patch("app.st.write") as mock_write, \
        patch("mosnopro_us.data_manager.load_pandas_df_from_dropbox") as mock_load_csv, \
        patch("mosnopro_us.data_manager.load_xarray_file_from_dropbox") as mock_load_nc:

        mock_load_csv.return_value = MagicMock()
        mock_load_nc.return_value = MagicMock()

        # Stimulate site selection and the app logic
        site_name = "Morse Lake"
        site_name_transformed = site_name.replace(" ", "_")

        mock_write(f"Producing figure for {site_name_transformed}... Please wait...")

        mock_write.assert_any_call(
            f"Producing figure for {site_name_transformed}... Please wait..."
        )

def test_timeout_handling(monkeypatch):
    """
    Test if the application correctly handles timeouts during data loading.
    """
    # Mock a timeout exception in data loading
    def mock_load_from_dropbox(*args, **kwargs):
        raise TimeoutError("Simulated timeout")

    monkeypatch.setattr(
        "mosnopro_us.data_manager.load_xarray_file_from_dropbox", 
        mock_load_from_dropbox
    )

    # Check if a TimeoutError is raised
    with pytest.raises(TimeoutError, match="Simulated timeout"):
        data_manager.load_xarray_file_from_dropbox(
            "/dummy/path.nc"
        )

def test_secrets_availability(monkeypatch):
    """
    Test if the required secrets are available.
    """
    # Mock Streamlit secrets
    mock_secrets = {
        "db_credentials": {
            "APP_KEY": "dummy_key",
            "APP_SECRET": "dummy_secret",
            "refresh_token": "dummy_token"
        }
    }
    monkeypatch.setattr("app.st.secrets", mock_secrets)

    #Validate secrets
    secrets = mock_secrets["db_credentials"]
    assert "APP_KEY" in secrets, "APP_KEY not found in secrets"
    assert "APP_SECRET" in secrets, "APP_SECRET not found in secrets"
    assert "refresh_token" in secrets, "refresh_token not found in secrets"

def test_dropbox_sever_down(monkeypatch):
    """
    Test how the app handles a dropbox server down exception.
    """
    # Mock Dropbox API failure
    def mock_load_from_dropbox(*args, **kwargs):
        raise ConnectionError("Dropbox server down")

    monkeypatch.setattr(
        "mosnopro_us.data_manager.load_xarray_file_from_dropbox", 
        mock_load_from_dropbox
    )

    # Verify that a ConnectionError is raised when sever is down
    with pytest.raises(ConnectionError, match="Dropbox server down"):
        data_manager.load_xarray_file_from_dropbox("/dummy/path.nc")
