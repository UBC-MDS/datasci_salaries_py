import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import sys

sys.path.append("/app/")
from .layout import *
from plot import *

app = dash.Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP, "/css/button.css"]
)

server = app.server

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        topbar,
        content,
        sidebar,
    ]
)


@app.callback(Output("scatter", "srcDoc"), Input("data_scientist", "value"))
def update(DS_identity):
    rst = plot_sidebar(DS_identity)
    return rst


@app.callback(Output("world_map", "srcDoc"), [Input("select-country", "value")])
def update(xcon):
    return plot_map(xcon)


@app.callback(
    Output("salary_heatmap", "srcDoc"),
    [Input("xslider_1", "value"), Input("select-country", "value")],
)
def update(xmax, xcon):
    return plot_salary_heatmap(xmax, xcon)


@app.callback(Output("gender-boxplot", "srcDoc"), [Input("select-country", "value")])
def update(xcon):
    return plot_gender_boxplot(xcon)


@app.callback(Output("edu_histogram", "srcDoc"), [Input("select-country", "value")])
def update(xcon):
    return plot_edu_histo(xcon)


if __name__ == "__main__":
    app.run_server(debug=True)
