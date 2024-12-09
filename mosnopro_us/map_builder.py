import folium
import data_manager


def plot_map():
    """
    Generate an interactive map using folium with SNOTEL points and the Washington boundary.
    Returns:
    - folium.Map: A folium map object with added layers.
    """
    # Load SNOTEL points and filter for specific sites
    snotels = data_manager.load_snotel_points()
    sites = ['Morse Lake', 'Olallie Meadows', 'Paradise',
             'Stampede Pass', 'Stevens Pass', 'Swift Creek',
             'Waterhole', 'Wells Creek', 'White Pass']
    snotels = snotels[snotels['name'].isin(sites)]
    snotels['alt'] = (snotels['geometry'].z / 3.28).astype(int).astype(str) + ' M'
    # Load Washington boundary
    wa_state = data_manager.load_washington_boundary()
    # plot these points on a folium map
    m = folium.Map([wa_state.centroid.y.loc[0], wa_state.centroid.x.loc[0]],
                   zoom_start=7, tiles="openstreetmap")
    # Add Washington boundary to the map
    folium.GeoJson(
        data=wa_state.geometry,
        name="Washington Boundary",
        style_function=lambda x: {'color': 'blue', 'weight': 2}
    ).add_to(m)
    # Add SNOTEL points with tooltips and popups
    folium.GeoJson(
        data=snotels,
        name="SNOTEL Sites",
        tooltip=folium.GeoJsonTooltip(
            fields=["name", "id", "alt"],
            aliases=["Site Name", "Site ID", "Elevation"],
            localize=True
        ),
        popup=folium.GeoJsonPopup(
            fields=["name", "id", "alt"],
            aliases=["Site Name", "Site ID", "Elevation"]
        ),
        marker=folium.CircleMarker(
            radius=8,
            color="green",
            fill=True,
            fill_color="green",
            fill_opacity=0.6
        ),
        highlight_function=lambda x: {"fillOpacity": 0.8}
    ).add_to(m)
    return m
