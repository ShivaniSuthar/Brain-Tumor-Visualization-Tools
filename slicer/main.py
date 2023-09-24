import dash
from dash import dcc, html
import plotly.graph_objs as go
import numpy as np
import skimage




# Import data
vol = skimage.io.imread("assets/attention-mri.tif")
volume = vol.T
r, c = volume[0].shape


# Define frames
nb_frames = 68
frames = [go.Frame(data=go.Surface(
    z=(6.7 - k * 0.1) * np.ones((r, c)),
    surfacecolor=np.flipud(volume[67 - k]),
    cmin=0, cmax=200),
    name=str(k)  
    )
    for k in range(nb_frames)]


# Create the figure
fig = go.Figure(frames=frames)


# Add data to be displayed before animation starts
fig.add_trace(go.Surface(
    z=6.7 * np.ones((r, c)),
    surfacecolor=np.flipud(volume[67]),
    colorscale='Gray',
    cmin=0, cmax=200,
    colorbar=dict(thickness=20, ticklen=4),
    hovertext=np.random.normal(size=(c, r)),
    hovertemplate='<br>x: %{x}<br>y: %{y}<br>z: %{z}<br>random number: %{hovertext}<extra></extra>'
))






def frame_args(duration):
    return {
        "frame": {"duration": duration},
        "mode": "immediate",
        "fromcurrent": True,
        "transition": {"duration": duration, "easing": "linear"},
    }




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




# Create the Dash app
app = dash.Dash(__name__)




# Define the layout of the app
app.layout = html.Div([
    dcc.Graph(figure=fig)
])




# Defines the server attribute
server = app.server




if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
