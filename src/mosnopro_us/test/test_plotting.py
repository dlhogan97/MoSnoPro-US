import unittest
import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from src.mosnopro_us.plotting import plot_layers, produce_temp_depth_fig, produce_density_depth_fig, produce_liquid_water_depth_fig

class TestPlotLayers(unittest.TestCase):
    
    def setUp(self):
        # Create mock data for testing
        self.depth = xr.DataArray(
            np.random.uniform(-1, 1, (10, 1, 5)),
            dims=("time", "hru","ifcToto"),
            coords={"time": pd.date_range("2024-01-01", periods=10)}
        )
        self.var = xr.DataArray(
            np.random.uniform(-10, 1, (10, 1, 5)),
            dims=("time", "hru", "ifcToto"),
            coords={"time": pd.date_range("2024-01-01", periods=10)}
        )

    def test_plot_layers_returns_plot(self):
        fig, ax = plt.subplots()
        ax, mappable = plot_layers(self.var, self.depth, ax=ax, plot_snow=False, plot_soil=False)
        self.assertIsInstance(ax, plt.Axes)
        self.assertIsNotNone(mappable)

    def test_plot_layers_data_type(self):
        with self.assertRaises(AssertionError):
            plot_layers(np.random.rand(10, 5), self.depth, plot_snow=False, plot_soil=False)  # var not an xarray DataArray

        with self.assertRaises(AssertionError):
            plot_layers(self.var, np.random.rand(10, 5), plot_snow=False, plot_soil=False)  # depth not an xarray DataArray

    def test_plot_layers_invalid_variable_range(self):
        with self.assertRaises(AssertionError):
            plot_layers(self.var, self.depth, variable_range=[-10])  # invalid range length

class TestProduceFigures(unittest.TestCase):

    def setUp(self):
        # Mock SUMMA and SNOTEL data
        self.summa_df = xr.Dataset({
            "iLayerHeight": xr.DataArray(np.random.uniform(-1, 1, (10, 5, 1)),
                                          dims=("time", "ifcToto", "hru"),
                                          coords={"time": pd.date_range("2024-01-01", periods=10)}),
            "mLayerTemp": xr.DataArray(np.random.uniform(-10, 1, (10, 5, 1)),
                                        dims=("time", "ifcToto", "hru"),
                                        coords={"time": pd.date_range("2024-01-01", periods=10)}),
            "mLayerVolFracWat": xr.DataArray(np.random.uniform(0, 1, (10, 5, 1)),
                                                dims=("time", "ifcToto", "hru"),
                                                coords={"time": pd.date_range("2024-01-01", periods=10)}),
            "mLayerVolFracLiq": xr.DataArray(np.random.uniform(0, 1, (10, 5, 1)),
                                                dims=("time", "ifcToto", "hru"),
                                                coords={"time": pd.date_range("2024-01-01", periods=10)}),
            "scalarSnowDepth": xr.DataArray(np.random.uniform(0, 1, (10,1)),
                                             dims=("time","hru"),
                                             coords={"time": pd.date_range("2024-01-01", periods=10)})
        })

        self.snotel_df = pd.DataFrame({
            "geometry": ["POINT (100 200)"] * 10,
            "SNOWDEPTH": np.random.rand(10)
        }, index=pd.date_range("2024-01-01", periods=10))

        self.name = "Test Site"

    def test_produce_temp_depth_fig(self):
        fig = produce_temp_depth_fig(self.summa_df, self.snotel_df, self.name, plot_snow=False)
        self.assertIsInstance(fig, Figure)

    def test_produce_density_depth_fig(self):
        fig = produce_density_depth_fig(self.summa_df, self.snotel_df, self.name, plot_snow=False)
        self.assertIsInstance(fig, Figure)

    def test_produce_liquid_water_depth_fig(self):
        fig = produce_liquid_water_depth_fig(self.summa_df, self.snotel_df, self.name, plot_snow=False)
        self.assertIsInstance(fig, Figure)
    
    # test for missin dimensions
    def test_produce_temp_depth_fig_missing_dimensions(self):
        # Remove the 'layer' dimension
        self.summa_df = self.summa_df.drop_dims("hru")
        with self.assertRaises(ValueError) as e:
            produce_temp_depth_fig(self.summa_df, self.snotel_df, self.name)
        the_exception = e.exception
        self.assertEqual(str(the_exception), "DataArray is missing dimension. Check for hru, time, and ifcToto.")
    
    # test to make sure index of the dataframe is a datetime index
    def test_df_index_type(self):
        self.snotel_df.index = pd.date_range("2024-01-01", periods=10).strftime("%Y-%m-%d")
        with self.assertRaises(ValueError) as e:
            produce_temp_depth_fig(self.summa_df, self.snotel_df, self.name)
        the_exception = e.exception
        self.assertEqual(str(the_exception), "snotel_df index is not a datetime index. Check input data.")

if __name__ == "__main__":
    unittest.main()
