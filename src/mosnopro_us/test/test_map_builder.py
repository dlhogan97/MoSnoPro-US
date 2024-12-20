import pytest
import folium
from mosnopro_us.data_manager import load_snotel_points
from mosnopro_us.map_builder import plot_map


@pytest.fixture
def map_object():
    """Fixture to generate the map object."""
    return plot_map()


@pytest.fixture
def snotel_data():
    """Fixture to load snotel points."""
    return load_snotel_points()


def test_map_has_correct_sites(map_object):
    """
    Test that the generated map contains GeoJson layers and SNOTEL tooltips.
    [quality check test]
    """
    # Check for GeoJson layers
    geojson_layers = [
        layer for layer in map_object._children.values()
        if isinstance(layer, folium.GeoJson)
    ]
    assert len(geojson_layers) > 0, "No GeoJson layers found in the map"

    # Check that at least one GeoJson layer has the expected fields in its tooltip
    for layer in geojson_layers:
        if hasattr(layer, "tooltip"):
            tooltip_fields = layer.tooltip.fields
            assert "name" in tooltip_fields, "Tooltip does not contain 'name'"
            assert "id" in tooltip_fields, "Tooltip does not contain 'id'"
            assert "alt" in tooltip_fields, "Tooltip does not contain 'alt'"
            break


def test_altitude_values(snotel_data):
    """
    Test that the altitude (alt) values are valid.
    [pattern test (evaluate how the conversions were computed)]
    """
    # Ensure all altitudes are greater than 0 and not excessively high
    altitudes = snotel_data['geometry'].z / 3.28  # Convert feet to meters
    assert all(alt > 0 for alt in altitudes), "Some altitude values are <= 0"
    assert all(alt < 10000 for alt in altitudes), "Some altitude values are excessively high (>10,000 m)"
