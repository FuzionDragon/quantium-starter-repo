import pytest
from dash.testing.application_runners import import_app
from dash import Dash, html, dcc
import pandas as pd

def test_header_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)
    
    header = dash_duo.find_element("#header")
    assert header is not None, "Header should be present"
    assert header.text == "Pink Morsel Sales Trend", f"Header text should be 'Pink Morsel Sales Trend', got '{header.text}'"
    
    assert header.tag_name == "h1", "Header should be an H1 element"
    assert "textAlign" in header.get_attribute("style") or "text-align" in header.get_attribute("style"), \
           "Header should have text alignment styling"

def test_visualization_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)
    
    visualization = dash_duo.find_element("#sales-trend-graph")
    assert visualization is not None, "Visualization should be present"
    
    assert visualization.tag_name == "div", "Visualization should be a div element containing the graph"
    
    graph_container = dash_duo.find_element(".js-plotly-plot")
    assert graph_container is not None, "Plotly graph should be rendered"

def test_region_picker_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)
    
    region_picker = dash_duo.find_element("#region-picker")
    assert region_picker is not None, "Region picker should be present"
    
    assert region_picker.tag_name == "div", "Region picker should be a div element containing radio items"
    
    expected_options = ['north', 'east', 'south', 'west', 'all']
    radio_options = dash_duo.find_elements("input[type='radio']")
    assert len(radio_options) == len(expected_options), \
           f"Should have {len(expected_options)} radio options, found {len(radio_options)}"
