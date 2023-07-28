
import dash_core_components as dcc
import dash_html_components as html
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('/Users/ppraew/Desktop/Nectec_Internship/deploydjango/app/chart/dataset/cleaned_No_X,Y.csv') # noqa

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='SPECTROSCOPY BY PRAEW', style={'textAlign ': 'center'}),
    dcc.Dropdown(df.concen.unique(), '0', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])


@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.concen == value]
    return px.line(dff, x='Wave', y='Intensity')

