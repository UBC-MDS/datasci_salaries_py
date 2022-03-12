import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

### plot and layout
import pandas as pd
import altair as alt
import geopandas as gpd
from si_prefix import si_format

data = pd.read_csv("./data/processed/cleaned_salaries.csv")

scale_plots = 0.8


def plot_salary_heatmap(xmax, xcon):

    source = data.copy()
    source = source[(source["Age"] > 0) & (source["Salary_USD"] <= xmax[1])]
    if xcon is not None:
        source = source[source["Country"] == xcon]
    else:
        xcon = 'the World'
        
    x_bin_num = max(int((source.shape[0]/6)**0.65), 6)
    y_bin_num = max(int((source.shape[0]/6)**0.65), 6)   
    
        
    chart = (
        alt.Chart(source)
        .mark_rect()
        .encode(
            x=alt.X("Age:Q", bin=alt.Bin(maxbins=x_bin_num), title=None),
            y=alt.Y(
                "Salary_USD:Q",
                bin=alt.Bin(maxbins=y_bin_num),
                title="Salary in USD",
                axis=alt.Axis(format="~s"),
            ),
            tooltip="count()",
            color=alt.Color(
                "count()",
                scale=alt.Scale(scheme="greenblue"),
                legend=alt.Legend(title="Counts"),
            ),
        )
        .properties(
            title=f"Heatmap of {xcon}",
            width=scale_plots * 300,
            height=scale_plots* 200,
        )
    )

    bar = (
        alt.Chart(source)
        .mark_bar()
        .encode(
            x=alt.X("Age:Q"),
            y=alt.Y("count()", title="Counts"),
        )
        .properties(
            width=scale_plots * 300,
            height=scale_plots * 130,
        )
    )

    fchart = alt.vconcat(chart, bar, spacing=0)

    return fchart.to_html()


def plot_gender_boxplot(xcon):

    source = data.copy()
    source = source.dropna(subset=["GenderSelect"])
    source["GenderSelect"] = source["GenderSelect"].replace(
        "Non-binary, genderqueer, or gender non-conforming", "A different identity"
    )

    if xcon is not None:
        source = source[source["Country"] == xcon]
    else:
        xcon = 'the World'

    chart = (
        alt.Chart(source)
        .mark_boxplot()
        .encode(
            x=alt.X(
                "Salary_USD:Q",
                title="Salary in USD",
                axis=alt.Axis(format="~s"),
                scale=alt.Scale(zero=False),
            ),
            y=alt.Y("GenderSelect", title="Gender"),
            tooltip="count()",
            color=alt.Color("GenderSelect", title="Gender"),
        )
        .configure_legend(orient="bottom")
        .properties(title=f"Boxplot by gender in {xcon}", width=scale_plots* 420, height=scale_plots * 120)
        .interactive()
    )

    return chart.to_html()


def plot_edu_histo(xcon):

    education_order = [
        "Less than bachelor's degree",
        "Bachelor's degree",
        "Master's degree",
        "Doctoral degree",
    ]

    source = data.copy()
    if xcon is not None:
        source = source.query("Country == @xcon")
    else:
        xcon = 'the World'

    for idx, i in enumerate(source["FormalEducation"]):
        if i in education_order[1:]:
            continue
        else:
            source["FormalEducation"].iloc[idx] = "Less than bachelor's degree"

    chart = (
        alt.Chart(source)
        .mark_bar()
        .encode(
            x=alt.X("Salary_USD", axis=alt.Axis(format="~s"), bin=alt.Bin(maxbins=20), title="Salary in USD"),
            y=alt.Y("count()", title="Counts"),
            color=alt.Color(
                "FormalEducation", sort=education_order, title="Education level", legend=alt.Legend(columns=2)
            ),
            order=alt.Order("education_order:Q"),
        )
        .configure_legend(orient="bottom", titleFontSize=11, labelFontSize=11)
        .properties(
            title=f"Histogram of {xcon}",
            width=scale_plots*300,
            height=scale_plots*120,
        )
        .configure_axis(labelFontSize=12)
    )

    return chart.to_html()


def plot_map(xcon):

    world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
    world["name"] = world["name"].apply(
        lambda x: str.lower(" ".join(x.split(" ")[0:2]))
    )
    world = world.loc[world["name"] != "antarctica"]
    world.rename({"name": "Country"}, axis=1, inplace=True)

    source = data.copy()
    source = source[["Country", "Salary_USD"]].groupby("Country").median().reset_index()
    source["Country"] = source["Country"].apply(lambda x: str.lower(x))

    datamap = pd.merge(world, source, how="left")
    datamap['Salary_USD'] = datamap['Salary_USD'].fillna(0)
    datamap["Country"] = datamap["Country"].apply(lambda x: str.capitalize(x))
    
    chart = (
        alt.Chart(datamap).mark_geoshape(stroke='gray')
        .project(type="mercator", scale=40, translate=[185, 120])
        .encode(
            color=alt.Color(
                field="Salary_USD",
                type="quantitative",
                # scale=alt.Scale(type="sqrt"),
                legend=alt.Legend(
                    title="Salary in USD",
                    labelFontSize=10,
                    symbolSize=10,
                    titleFontSize=10,
                    format="~s"
                ),
            ),
            tooltip=["Country:N", "Salary_USD"],
        )
    )

    if xcon is not None:
        datamap["alpha"] = 1
        datamap.loc[datamap["Country"] == xcon, "alpha"] = 100
        chart = chart.encode(
            opacity=alt.Opacity(field="alpha", type="quantitative", legend=None),
        )
    else:
        xcon = 'the World'

    chart = chart.properties(
        title=f"Median Salary of {xcon}",
        width=350,
        height=175,
    ).configure_axis(labelFontSize=10)

    return chart.to_html()


def plot_sidebar(DS_identity=["Yes", "No", "Sort of (Explain more)"], df=data.copy()):
    # Clean data
    df = df.dropna(subset=["Salary_USD", "Tenure"])
    df = df.query("Salary_USD < 400_000")
    df = df[df["Tenure"] != "I don't write code to analyze data"]

    # Filter data
    if DS_identity == None:
        DS_identity = ["Yes", "No", "Sort of (Explain more)"]
    if not isinstance(DS_identity, list):
        DS_identity = list(DS_identity)
    df = df[df["DataScienceIdentitySelect"].isin(DS_identity)]

    # alt.themes.enable("dark")

    # Create Plot
    brush = alt.selection_interval()
    click = alt.selection_multi(fields=["Tenure"])

    points = (
        alt.Chart(df, title="Interactive window for coding experience count")
        .mark_circle()
        .encode(
            y=alt.Y("Country", title=None),
            x=alt.X("Salary_USD", axis=alt.Axis(format="~s"), title="Salary in USD"),
            color=alt.condition(
                brush,
                alt.Color("Tenure:N", legend=None),
                alt.value("lightgray"),
            ),
            opacity=alt.condition(click, alt.value(1.0), alt.value(0.1)),
            tooltip="EmployerIndustry",
        )
        .add_selection(brush)
    ).properties(width=scale_plots*250, height=scale_plots*490)

    bars = (
        alt.Chart(df, title="Click to filter the above plot!")
        .mark_bar()
        .encode(
            x=alt.X("count()", title="Counts"),
            y=alt.Y(
                "Tenure",
                title="Coding Experience",
                sort=[
                    "More than 10 years",
                    "6 to 10 years",
                    "3 to 5 years",
                    "1 to 2 years",
                    "Less than a year",
                ],
            ),
            color="Tenure",
            opacity=alt.condition(click, alt.value(0.9), alt.value(0.2)),
        )
    ).properties(width=scale_plots*250, height=scale_plots*100).transform_filter(brush)

    overall_plot = (
        alt.vconcat(points, bars, spacing=1)
        .configure(background="#2c2c2c")
        .configure_axisX(
            titleColor="white", titleFontSize=10, labelColor="white", labelFontSize=8
        )
        .configure_axisY(
            titleColor="white", titleFontSize=10, labelColor="white", labelFontSize=8
        )
        .configure_title(fontSize=13, color="white")
        .add_selection(click)
    )

    return overall_plot.to_html()


SIDEBAR_STYLE = {
    "position": "fixed",
    "top": "0rem",
    "right": 0,
    "bottom": 0,
    "width": 380,
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
                            style={"color": "white", "font-size": "14px"},
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
                        width=6,
                        style={"height": "3vh"},
                    ),
                    style={"height": "3vh"},
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                             dbc.Row(
                                html.Iframe(
                                    # srcDoc=plot_11(),
                                    style={
                                        "border-width": "0",
                                        "width": "100%",
                                        "height": "13vh",
                                    },
                                ),
                             ), 
                             dbc.Row(
                                html.Iframe(
                                    id="world_map",
                                    # srcDoc=plot_11(),
                                    style={
                                        "border-width": "0",
                                        "width": "100%",
                                        "height": "35vh",
                                    },
                                ),
                             ),
                             dbc.Row(
                                html.Iframe(
                                    style={
                                        "border-width": "0",
                                        "width": "100%",
                                        "height": "13vh",
                                    },
                                ),
                             ),                            ],
                            width=6,
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
                                        i: str(si_format(i, precision=0)).replace(" ", "") for i in range(0, 550_000, 50_000)
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
                            width=6,
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

app = dash.Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP, "/css/button.css"]
)

app.title = "Data Science Salaries"
server = app.server

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        topbar,
        content,
        # sidebar,
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
    app.run_server('localhost:8000', debug=False)
