"""
This is the main application file for MoSnoPro-US Dashboard.
It provides an interactive interface for visualizing snowpack properties.
"""
import logging
from mosnopro_us import data_manager, plotting, map_builder
from streamlit_folium import st_folium
import streamlit as st
import pandas as pd
import os

# Configure logging
logging.basicConfig(
    filename="mosnopro_us.log",
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s %(message)s"
)

# Set page config
st.set_page_config(
    page_title="MoSnoPro-US Dashboard",
    page_icon="🏔️",
    layout="wide",
    initial_sidebar_state="expanded",
)
# if a .streamlit/secrets file exists, then we'll pull data from there
# otherwise, we'll use the example data
if os.path.exists('../.streamlit/secrets.toml'):
    # Constants
    SNOTEL_PATH = "/Apps/push-and-pull-pysumma/snotel_csvs/"
    SUMMA_PATH = "/Apps/push-and-pull-pysumma/output/"
else:
    print("Secrets file not found. Using example data instead.")
    SNOTEL_PATH = "snotel_csvs/"
    SUMMA_PATH = "output/"

# Header section
st.title("MoSnoPro-US Dashboard 🏔️❄️")
st.markdown(
    """
    Welcome to **MoSnoPro-US**, a tool designed for visualizing
    and analyzing snowpack properties across Washington State.
    Using real-time data from SNOTEL stations and the SUMMA model,
    this app provides insights into snow depth, density,
    and temperature trends, helping users understand
    snowpack instabilities and potential avalanche risks.
    """
)
st.markdown("---")

# Sidebar Navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["Overview", "Interactive Map"])


# Helper Functions
def load_and_filter_data(site, time_slice):
    """
    Load and filter data for the selected SNOTEL site.
    Args:
        site (str): The name of the SNOTEL site.
        time_range (str): The selected time range.
    Returns:
        tuple: Filtered SUMMA and SNOTEL data.
    """
     # Path to the xarray file in Dropbox
    db_xr_file = f"{SUMMA_PATH}_{site}_timestep.nc"
    # Path to csv in Dropbox
    db_pd_file = f"{SNOTEL_PATH}{site}.csv"

    if not os.path.exists('../.streamlit/secrets.toml'):
        snotel_df = data_manager.load_pandas_file_from_examples(db_pd_file)
        summa_ds = data_manager.load_xarray_file_from_examples(db_xr_file)
    else:
        snotel_df = data_manager.load_pandas_df_from_dropbox(dropbox_file_path=db_pd_file)
        summa_ds = data_manager.load_xarray_file_from_dropbox(dropbox_file_path=db_xr_file)

    filtered_summa_data = summa_ds.sel(time=time_slice)
    filtered_snotel_data = snotel_df.loc[time_slice]

    return filtered_summa_data, filtered_snotel_data


def plot_selected_figure(filtered_summa_data, filtered_snotel_data, site, plot_type):
    """
    Plot the selected figure based on user input.
    Args:
        filtered_summa_data (xr.Dataset): Filtered SUMMA data.
        filtered_snotel_data (pd.DataFrame): Filtered SNOTEL data.
        site (str): The name of the SNOTEL site.
        plot_type (str): The selected plot type (Temperature or Density).
    Returns:
        matplotlib.figure.Figure: The generated figure.
    Raises:
        ValueError: If the plot type is invalid.
    """
    if plot_type == "Temperature":
        # Plot Snow Depth for the selected site
        return plotting.produce_temp_depth_fig(filtered_summa_data, filtered_snotel_data, site)
    if plot_type == "Density":
        # Plot Density for the selected site
        return plotting.produce_density_depth_fig(filtered_summa_data, filtered_snotel_data, site)

    raise ValueError(f"Invalid plot type: {plot_type}. Choose from 'Temperature' or 'Density'.")


# Overview Section
if section == "Overview":
    st.markdown("## Overview")
    st.markdown(
        """
        ### Key Features
        - **Interactive Maps**:
        Explore snowpack metrics at various SNOTEL stations.
        - **Visualizations**:
        View snow depth, temperature, and density trends over time.
        - **Real-Time Data**:
        Integrates SNOTEL and weather forecast data for actionable insights.

        ### How to Use
        1. Select a SNOTEL site from the interactive map.
        2. View detailed snowpack metrics and visualizations.
        3. Use the dashboard to explore trends and generate insights.
        """
    )

# Interactive Map and Visualization
elif section == "Interactive Map":
    st.subheader("Interactive Map")
    st.markdown(
        "Click on a Snotel site to produce a figure of Snow Depth versus Temperature or Density.")
    left, right = st.columns(2)

    with left:
        st.markdown("### Select a SNOTEL Site")
        m = map_builder.plot_map()

        # save points clicked to variable
        # call to render Folium map in Streamlit
        st_data = st_folium(
            m,
            returned_objects=['last_active_drawing', 'last_object_clicked_popup'],
            width=725, height=500
        )

    with right:
        placeholder_message = st.empty()    # Placeholder for temporary messages

        if st_data['last_active_drawing'] is None:
            st.write("No Snotel site clicked")
        elif 'properties' not in st_data['last_active_drawing'].keys():
            st.write("No Snotel site clicked")
        elif st_data['last_active_drawing']['properties'] == {}:
            st.write("No Snotel site clicked")
        else:
            try:
                site = st_data['last_active_drawing']["properties"]["name"]
                site = str.replace(site, " ", "_")

                placeholder_message.write(
                    f"Producing figure for {site}... Please wait..."
                )

                # Time Range Selection
                st.markdown("### Time Range")
                time_col, plot_col = st.columns(2)

                with time_col:
                    time_range = st.radio(
                        "Select Time Range:",
                        ["Entire period", "Recent Week", "Recent Month"],
                        key="time_range",
                    )

                with plot_col:
                    # User selection of Map type
                    plot_type = st.radio(
                        "Select Plot Type:",
                        ["Temperature", "Density"],
                        key="plot_type",
                    )

                if time_range == "Entire period":
                    time_slice = slice(None)
                elif time_range == "Recent Week":
                    time_slice = slice(
                        pd.Timestamp.now() - pd.Timedelta(weeks=1), pd.Timestamp.now()
                    )
                elif time_range == "Recent Month":
                    time_slice = slice(
                        pd.Timestamp.now() - pd.Timedelta(days=30), pd.Timestamp.now()
                    )

                # Filter data by selected time range
                filtered_summa_data, filtered_snotel_data = load_and_filter_data(site, time_slice)
                fig = plot_selected_figure(
                        filtered_summa_data, filtered_snotel_data, site, plot_type
                )
                # Display the figure
                st.pyplot(fig)

                # Clear temporary messages
                placeholder_message.empty()
                st.write("Figure completed.")

            except KeyError as e:
                placeholder_message.error(f"Missing key in data for {site}: {e}")
            except FileNotFoundError as e:
                placeholder_message.error(f"File not found for {site}: {e}")
            except ValueError as e:
                placeholder_message.error(f"Error processing data for {site}: {e}")
            except Exception as e:
                placeholder_message.error(f"Error loading or processing data for {site}: {e}")
                logging.error("Error loading or processing data fro %s: %s", site, e)
