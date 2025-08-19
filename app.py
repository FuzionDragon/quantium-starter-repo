from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

data = pd.read_csv('./data/pink_morsel_sales.csv')
data = data.rename(columns={'date': 'Date', 'sales': 'Sales', 'region': 'Region'})

fig = px.line(data, x="Date", y="Sales", color="Region") 

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales Trend'),

    html.Div(children='''
    Price increase to pink morsels happen on the 15th of January 2021
    '''),

    dcc.Graph(
        id='sales-trend-graph',
        figure=fig
    ),

    html.Div(children='''
    Based on the graph, it is obvious to see that the price increase from the 15th of January 2021 onwards shows an drastic increase in sales.
    ''')
])

if __name__ == '__main__':
    app.run(debug=True)

