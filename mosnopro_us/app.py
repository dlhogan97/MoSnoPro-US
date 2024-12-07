import streamlit as st
import data_manager
from streamlit_folium import st_folium
import folium
import plotting
import map_builder

# Set page config
st.set_page_config(
    page_title="MoSnoPro-US Dashboard",
    page_icon="🏔️",
    layout="wide",
)

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

# Sidebar Navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["Overview", "Interactive Map"])

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
    st.markdown("## Interactive Map")
    st.markdown("Click on a Snotel site to produce a figure of Snow Depth and Temperature.")
    left, right = st.columns(2)

    with left:
        st.markdown("### Map")
        m = map_builder.plot_map()

        # save points clicked to variable
        # call to render Folium map in Streamlit
        st_data = st_folium(m,
                            returned_objects=['last_active_drawing',
                                              'last_object_clicked_popup'],
                            width=725, height=600)

    with right:

        if st_data['last_active_drawing'] is None:
            st.write("No Snotel site clicked")
        elif 'properties' not in st_data['last_active_drawing'].keys():
            st.write("No Snotel site clicked")
        elif st_data['last_active_drawing']['properties'] == {}:
            st.write("No Snotel site clicked")
        else:
            site = st_data['last_active_drawing']["properties"]["name"]
            # Add text to indicate the type of figure (snow depth vs. temp)? 
            st.write(f"Producing figure for {site}... Please wait...")
            site = str.replace(site, " ", "_")

                # Remove text after figure is completed? 

            st.write(f"Loading data for {site}...")
            # Path to the xarray file in Dropbox
            db_xr_file = f"/Apps/push-and-pull-pysumma/output/_{site}_timestep.nc"
            # Path to csv in Dropbox
            db_pd_file = f"/Apps/push-and-pull-pysumma/snotel_csvs/{site}.csv"
            snotel_df = data_manager.load_pandas_df_from_dropbox(dropbox_file_path=db_pd_file)
            summa_ds = data_manager.load_xarray_file_from_dropbox(dropbox_file_path=db_xr_file)

            # Remove "Loading data for {site}" after file is loaded?

            # Recent week and recent month options

            # User selection of map type

            # Plot Temperature for the selected site
            fig = plotting.produce_temp_depth_fig(summa_ds, snotel_df, site)

            # Display the figure
            st.pyplot(fig)

            # reset for the next user click
