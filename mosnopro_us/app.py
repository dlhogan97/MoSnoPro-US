import streamlit as st
import data_manager
from streamlit_folium import st_folium
import folium
import plotting
import map_builder

st.set_page_config(
    page_title="MoSnoProUS documentation",
    page_icon=":world_map:️",
    layout="wide",
)

"# MoSnoPro-US"

"""Need to fill this in"""

"""
Currently, 
"""

"""


### Click on site to produce figure.
"""
left, right = st.columns(2)

with left:
    m = map_builder.plot_map()

    # save points clicked to variable
    # call to render Folium map in Streamlit
    st_data = st_folium(m, 
                        returned_objects= ['last_active_drawing','last_object_clicked_popup'],
                        width=725, height=300)

with right:
    if st_data['last_active_drawing'] is None:
        st.write("No Snotel site clicked")
    elif not 'properties' in st_data['last_active_drawing'].keys():
        st.write("No Snotel site clicked")
    elif st_data['last_active_drawing']['properties'] == {}:
        st.write("No Snotel site clicked")
    else:
        site = st_data['last_active_drawing']["properties"]["name"]
        st.write(f"Producing figure for {site}... Please wait...")
        site = str.replace(site, " ", "_")

        st.write(f"Loading data for {site}...")
        db_xr_file = f"/Apps/push-and-pull-pysumma/output/_{site}_timestep.nc"  # Path to the xarray file in Dropbox
        db_pd_file = f"/Apps/push-and-pull-pysumma/snotel_csvs/{site}.csv" # Path to csv in Dropbox
        snotel_df = data_manager.load_pandas_df_from_dropbox(dropbox_file_path=db_pd_file)
        summa_ds = data_manager.load_xarray_file_from_dropbox(dropbox_file_path=db_xr_file)

        # Plot Temperature for the selected site
        fig = plotting.produce_temp_depth_fig(summa_ds, snotel_df, site)

        # Display the figure
        st.pyplot(fig)

        # reset for the next user click


