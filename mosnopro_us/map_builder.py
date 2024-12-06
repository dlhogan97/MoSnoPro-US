import folium
import data_manager


def plot_map():
    snotels = data_manager.load_snotel_points()
    sites = ['Morse Lake', 'Olallie Meadows', 'Paradise',
             'Stampede Pass', 'Stevens Pass', 'Swift Creek',
             'Waterhole', 'Wells Creek', 'White Pass']
    snotels = snotels[snotels['name'].isin(sites)]
    snotels['alt'] = (snotels['geometry']
                      .z/3.28).astype(int).astype(str) + ' m elevation'
    wa_state = data_manager.load_washington_boundary()

    # plot these points on a folium map
    m = folium.Map([wa_state.centroid.y.loc[0], wa_state.centroid.x.loc[0]],
                   zoom_start=7, tiles="openstreetmap")

    folium.GeoJson(wa_state.geometry).add_to(m)
    folium.GeoJson(snotels,
                   control=False,
                   marker=folium.CircleMarker(radius=10,
                                              weight=0,  # outline weight
                                              fill_color='#000000',
                                              fill_opacity=1),
                   tooltip=folium.GeoJsonTooltip(fields=["name", "id", "alt"]),
                   popup=folium.GeoJsonPopup(fields=["name", "id", "alt"]),
                   highlight_function=lambda x: {"fillOpacity": 0.8},
                   zoom_on_click=True,
                   ).add_to(m)
    return m
