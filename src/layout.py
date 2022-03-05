from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from si_prefix import si_format

from .plot import *
# from plot import *


SIDEBAR_STYLE = {
    "position": "fixed",
    "top": "0rem",
    "right": 0,
    "bottom": 0,
    "width": 400,
    "padding": "2rem 0rem",
    "background-color": "#2C2C2C",
}

TOPBAR_STYLE = {
    "top": 0,
    "right": 0,
    "left": 0,
    "height": "2rem",
    "margin-right": "10rem",
    "padding": "0rem 0rem",
    "background-color": "#808080",
    # "background-color": "#fffff",
}

CONTENT_STYLE = {
    "margin-left": "0rem",
    "margin-right": "3rem",
    "padding": "0rem 0rem",
}

country_names = data["Country"].unique()
country_names.sort()
country_names = country_names  # ["World"] + list(country_names)


topbar = html.Div(
    [
        dbc.Col(
            [
                html.Div(
                    [
                        html.H2(
                            "Data Science Salaries Dashboard",
                            style={
                                "color": "white",
                                "font-size": "20px",
                                "text-align": "center",
                            },
                        )
                    ]
                ),
            ]
        )
    ],
    style=TOPBAR_STYLE,
)

sidebar = html.Div(
    [
        dbc.Col(
            [
                html.Div(
                    [
                        html.H2(
                            "\rAre you a Data Scientist?",
                            style={"color": "gray", "font-size": "14px"},
                        ),
                        dcc.Dropdown(
                            id="data_scientist",
                            options=[
                                {"label": "Yes", "value": "Yes"},
                                {"label": "No", "value": "No"},
                                {"label": "Sort of", "value": "Sort of (Explain more)"},
                            ],
                            value=["Yes", "No", "Sort of (Explain more)"],
                            multi=True,
                            style={"font-size": "12px", "height": "3vh"},
                        ),
                    ]
                ),
                html.Iframe(
                    id="scatter",
                    # srcDoc=plot_13(DS_identity=['Yes', 'No', 'Sort of (Explain more)']),
                    style={"border-width": "0", "width": "100%", "height": "100vh"},
                ),
            ]
        )
    ],
    style=SIDEBAR_STYLE,
)


content = dbc.Row(
    [
        dbc.Col(
            [
                dbc.Row(
                    dbc.Col(
                        [
                            dcc.Dropdown(
                                id="select-country",
                                placeholder='Please select a country',
                                value=None,
                                options=[
                                    {"label": country, "value": country}
                                    for country in country_names
                                ],
                            ),
                        ],
                        width=7,
                        style={"height": "3vh"},
                    ),
                    style={"height": "3vh"},
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Iframe(
                                    id="world_map",
                                    # srcDoc=plot_11(),
                                    style={
                                        "border-width": "0",
                                        "width": "100%",
                                        "height": "60vh",
                                    },
                                ),
                            ],
                            width=7,
                        ),
                        

                        dbc.Col(
                            [
                                html.H2("Select a salary range:",                             
                                        style={"color":"black", "font-size": "12px"}
                                        ),
                                dcc.RangeSlider(
                                    id="xslider_1",
                                    min=0,
                                    max=500000,
                                    value=[0, 500000],
                                    marks={
                                        i: str(si_format(i, precision=1)) for i in range(0, 550_000, 80_000)
                                    },
                                ),
                                
                                html.Iframe(
                                    id="salary_heatmap",
                                    # srcDoc=plot_13(DS_identity=['Yes', 'No', 'Sort of (Explain more)']),
                                    style={
                                        "border-width": "0",
                                        "width": "100%",
                                        "height": "52vh",
                                    },
                                ),
                            ],
                            width=5,
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Iframe(
                                    id="gender-boxplot",
                                    style={
                                        "border-width": "0",
                                        "width": "100%",
                                        "height": "32vh",
                                        "display": "block",
                                    },
                                ),
                            ],
                            width=7,
                        ),
                        dbc.Col(
                            [
                                html.Iframe(
                                    id="edu_histogram",
                                    style={
                                        "border-width": "0",
                                        "width": "100%",
                                        "height": "32vh",
                                    },
                                ),
                            ],
                            width=5,
                        ),
                    ]
                ),
            ]
        ),
        
        dbc.Col(
            [sidebar],
            width=3,
        )
    ],
    style=CONTENT_STYLE,
)
