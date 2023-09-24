
# Import statements
import base64
import dash
from dash import dcc, html, Input, Output, callback 
import plotly.graph_objs as go
import numpy as np
import skimage
from dash import Dash
import os

# List of images to show
img_names = [i for i in os.listdir("MNIST_data") if i.endswith(".jpeg")]

# Import slicer image
vol = skimage.io.imread("assets/attention-mri.tif")
volume = vol.T
r, c = volume[0].shape

# Creating the figure and defining the frames
fig = go.Figure(
    frames=[
        go.Frame(
            data=go.Surface(
                z=(6.7 - k * 0.1) * np.ones((r, c)),
                surfacecolor=np.flipud(volume[67 - k]),
                cmin=0, 
                cmax=200
            ),
        name=str(k)) for k in range(68)
    ]
)

# Add data to be displayed before animation starts
fig.add_trace(go.Surface(
    z=6.7 * np.ones((r, c)),
    surfacecolor=np.flipud(volume[67]),
    colorscale='Gray',
    cmin=0, cmax=200,
    colorbar=dict(thickness=20, ticklen=4),
))
fig.update_traces(hoverinfo="none", hovertemplate=None)

def frame_args(duration):
    return {
        "frame": {"duration": duration},
        "mode": "immediate",
        "fromcurrent": True,
        "transition": {"duration": duration, "easing": "linear"},
    }



# Pause/play buttons
sliders = [
    {
        "pad": {"b": 10, "t": 60},
        "len": 0.9,
        "x": 0.1,
        "y": 0,
        "steps": [
            {
                "args": [[f.name], frame_args(0)],
                "label": str(k),
                "method": "animate",
            }
            for k, f in enumerate(fig.frames)
        ],
    }
]




# Layout
fig.update_layout(
    title='Slices in volumetric data',
    width=600,
    height=600,
    scene=dict(
        zaxis=dict(range=[-0.1, 6.8], autorange=False),
        aspectratio=dict(x=1, y=1, z=1),
    ),
    updatemenus=[
        {
            "buttons": [
                {
                    "args": [None, frame_args(50)],
                    "label": "&#9654;",  # play symbol
                    "method": "animate",
                },
                {
                    "args": [[None], frame_args(0)],
                    "label": "&#9724;",  # pause symbol
                    "method": "animate",
                },
            ],
            "direction": "left",
            "pad": {"r": 10, "t": 70},
            "type": "buttons",
            "x": 0.1,
            "y": 0,
        }
    ],
    sliders=sliders
)

# Creating the Dash app
app = Dash(__name__)

# Creating the app layout
app.layout = html.Div([
    dcc.Graph(id="surface", figure=fig, clear_on_unhover=True),
    dcc.Tooltip(id="tooltip"),
])

# calling function to update images in tooltip
@callback(
    Output("tooltip", "show"),
    Output("tooltip", "bbox"),
    Output("tooltip", "children"),
    Input("surface", "hoverData")
)

# Tooltip image displays 
def display_tooltip(hover_data):
    if hover_data is None:
        return False, dash.no_update, dash.no_update
    
    pt = hover_data["points"][0]

    # Accessing the image with index corresponding to x
    img_name = img_names[pt["x"]]

    with open(f"MNIST_data/{img_name}", "rb") as image_file:
        image_data = base64.b64encode(image_file.read()) 
        image_data = image_data.decode() 
        image_data = "{}{}".format("data:image/jpg;base64, ", image_data)

# Tooltip text display   
    bbox = pt["bbox"]
    random_number = np.random.normal(size=(c, r))
    children = [
        html.Div([
            html.Img(src=image_data, style={"width": "100%"}),
            html.P(f"x = {pt['x']}"),
            html.P(f"y = {pt['y']}"),
            html.P(f"z = {pt['z']}"),
            html.P(f"Random Number: {random_number[0][0]}")
        ], style={"width": "200px", "white-space": "normal"})
    ]
    return True, bbox, children


server = app.server


if __name__ == "__main__":
    app.run_server(debug=True)


