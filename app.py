from dash import Dash, Output, Input, callback, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

data = pd.read_csv('./data/pink_morsel_sales.csv')
data = data.rename(columns={'date': 'Date', 'sales': 'Sales', 'region': 'Region'})

radio = dcc.RadioItems(options=['north', 'east', 'south', 'west', 'all'], value='all', inline=True, id='region-picker')

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales Trend'),

    html.Div(children='''
    Price increase to pink morsels happen on the 15th of January 2021
    '''),

    radio,

    dcc.Graph(
        id='sales-trend-graph'
    ),

    html.Div(children='''
    Based on the graph, it is obvious to see that the price increase from the 15th of January 2021 onwards shows an drastic increase in sales.
    ''')
])

@callback(
        Output('sales-trend-graph', 'figure'),
        Input('region-picker', 'value'))
def update_figure(selected_region):
    if selected_region == "all":
        fig = px.line(data, x="Date", y="Sales", color="Region") 
        fig.update_layout(transition_duration=500)

        return fig
    else:
        fig = px.line(data[data['Region'] == selected_region], x="Date", y="Sales", color="Region") 
        fig.update_layout(transition_duration=500)

        return fig

if __name__ == '__main__':
    app.run(debug=True)

