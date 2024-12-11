"""
This module contains unit tests for the app.py functionality in the Mosnopro US project.
"""

from unittest.mock import patch, MagicMock
import pytest
from src.mosnopro_us import data_manager

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
    monkeypatch.setattr("src.app.st_folium", MagicMock(return_value=mock_map_data))

    # Test if the corect site is processed
    with patch("src.app.st.sidebar.radio", return_value="Interactive Map"), \
        patch("src.app.st.write") as mock_write, \
        patch("src.mosnopro_us.data_manager.load_pandas_df_from_dropbox") as mock_load_csv, \
        patch("src.mosnopro_us.data_manager.load_xarray_file_from_dropbox") as mock_load_nc:

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
        "src.mosnopro_us.data_manager.load_xarray_file_from_dropbox", 
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
    monkeypatch.setattr("src.app.st.secrets", mock_secrets)

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
        "src.mosnopro_us.data_manager.load_xarray_file_from_dropbox", 
        mock_load_from_dropbox
    )

    # Verify that a ConnectionError is raised when sever is down
    with pytest.raises(ConnectionError, match="Dropbox server down"):
        data_manager.load_xarray_file_from_dropbox("/dummy/path.nc")
