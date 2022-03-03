from dash import html
from dash import dcc
import dash_bootstrap_components as dbc


from .plot import *

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "right": 0,
    "bottom": 0,
    "width": "36rem",
    "padding": "3rem 3rem",
    "background-color": "#2C2C2C",
}

TOPBAR_STYLE = {
    "top": 0,
    "right": 0,
    "left": 0,
    "height": "3rem",
    "margin-right": "36rem",
    "padding": "0rem 0rem",
    "background-color": "#808080",
    # "background-color": "#fffff",
}

CONTENT_STYLE = {
    "margin-left": "0rem",
    "margin-right": "36rem",
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
                            "Are you a Data Scientist?",
                            style={"color": "gray", "font-size": "16px"},
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
                        ),
                    ]
                ),
                html.Iframe(
                    id="scatter",
                    # srcDoc=plot_13(DS_identity=['Yes', 'No', 'Sort of (Explain more)']),
                    style={"border-width": "0", "width": "100%", "height": "100%"},
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
                                        "height": "580px",
                                    },
                                ),
                            ],
                            width=7,
                        ),
                        dbc.Col(
                            [
                                dcc.RangeSlider(
                                    id="xslider_1",
                                    min=0,
                                    max=2500000,
                                    value=[0, 2500000],
                                    marks={
                                        i: str(i) for i in range(0, 2_500_000, 400_000)
                                    },
                                ),
                                html.Iframe(
                                    id="salary_heatmap",
                                    # srcDoc=plot_13(DS_identity=['Yes', 'No', 'Sort of (Explain more)']),
                                    style={
                                        "border-width": "0",
                                        "width": "100%",
                                        "height": "580px",
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
                                        "height": "340px",
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
                                        "height": "340px",
                                    },
                                ),
                            ],
                            width=5,
                        ),
                    ]
                ),
            ]
        ),
    ],
    style=CONTENT_STYLE,
)
