import dash_bootstrap_components as dbc
from dash import Dash, dcc, html
import plotly.graph_objs as go


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.layout = html.Div(
    children=[
        html.H1("x-y Axis with Line x=y"),
        dcc.Graph(
            id="xy-axis",
            figure={
                "data": [
                    go.Scatter(
                        x=[0, 1],
                        y=[0, 1],
                        mode="lines",
                        name="x=y"
                    )
                ],
                "layout": go.Layout(
                    xaxis={"title": "X-axis"},
                    yaxis={"title": "Y-axis"},
                    margin={"l": 40, "b": 40, "t": 40, "r": 10},
                    showlegend=True
                )
            }
        )
    ]
)