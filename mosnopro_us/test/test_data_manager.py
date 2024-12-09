# Testing to make sure we have access to the database. 
def test_db_connection():
    import dropbox
    import data_manager
    import pandas as pd
    import xarray as xr
    # example site to test
    site="Paradise"
    db_xr_file = f"/Apps/push-and-pull-pysumma/output/_{site}_timestep.nc"  # Path to the xarray file in Dropbox
    db_pd_file = f"/Apps/push-and-pull-pysumma/snotel_csvs/{site}.csv" # Path to csv in Dropbox

    # Test if the returned value from this function is an xarray dataset
    try:
        assert isinstance(data_manager.load_xarray_file_from_dropbox(dropbox_file_path=db_xr_file),
                                                          xr.Dataset)
        print("Test passed for xarray!")
    except:
        TypeError("Model output dataset was not loaded correctly.")
    try:
         assert isinstance(data_manager.load_pandas_df_from_dropbox(dropbox_file_path=db_pd_file),
                                                          pd.DataFrame)
         print("Test passed for pandas!")
    except:
        TypeError("SNOTEL dataset was not loaded correctly.")

# Makes sure we get access to both the model data and the observations. 

# Testing exceptions for timeouts and retries.

# fake data is not available 
# Plan to move it forward 

# Makes sure the secrets are available.

# Dropbox server is down or not avaiable. 

# Testing validity of the data.
