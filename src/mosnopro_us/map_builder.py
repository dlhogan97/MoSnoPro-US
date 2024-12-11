import folium
from mosnopro_us.data_manager import load_snotel_points, load_washington_boundary
from pyproj import Transformer


def plot_map():
    """
    Generate an interactive map using folium to display SNOTEL sites as points and
    the Washington state boundary. The folium map has the following features:
        - SNOTEL sites are only a subset (n=9) of all SNOTEL sites (closer to 80 sites).
        - SNOTEL sites are displayed as points.
            - Each point includes tooltips and popups that display the SNOTEL site name, ID, and elevation.
        - WA state boundary is displayed as a blue overlay.

    Parameters:
    - Output from load_snotel_points(): GeoJSON.
    - Output from load_washington_boundary(): GeoJSON.

    Returns:
    - folium.Map: A folium map object with added layers.
    """
    # Load SNOTEL points and filter for specific sites
    snotels = load_snotel_points()
    sites = ['Morse Lake', 'Olallie Meadows', 'Paradise',
             'Stampede Pass', 'Stevens Pass', 'Swift Creek',
             'Waterhole', 'Wells Creek', 'White Pass']
    snotels = snotels[snotels['name'].isin(sites)]
    snotels['alt'] = (snotels['geometry'].z / 3.28).astype(int).astype(str) + ' M'

    # Load Washington boundary
    wa_state = load_washington_boundary()

    # plot these points on a folium map
    transformer = Transformer.from_crs("EPSG:32638", "EPSG:4326", always_xy=True)

    x, y = [wa_state.to_crs(32638).centroid.x.mean(), wa_state.to_crs(32638).centroid.y.mean()]

    lon, lat = transformer.transform(x, y)
    m = folium.Map(location=[lat, lon],
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
