import yfinance as yf
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import plotly.express as px

from typing import Dict

app = Dash(__name__)

# get historical data of S&P 500 from Yahoo API
historical_data: dict = yf.Ticker("^GSPC").history(period='5d')

app.layout = html.Div([
    html.H1("Historical tock prices of S&P 500"),
    dcc.Graph(id="time-series-chart"),
    html.P("Select period:"),
    dcc.Dropdown(
        id="period",
        options=historical_data["validRanges"],
        value="5d",
        clearable=False,
    ),
])


@app.callback(
    Output(component_id="time-series-chart", component_property="figure"),
    Input(component_id="period", component_property="value"))
def display_time_series(input_period):
    df = historical_data["tradingPeriods"]
    fig = px.line(df, x='start', y='end')
    return fig


app.run_server(debug=True)
