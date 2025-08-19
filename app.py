from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

data = pd.read_csv('./data/pink_morsel_sales.csv')

fig = px.line(data, x="date", y="sales", color="region") 

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales Trend'),

    html.Div(children='''
    Price increase to pink morsels happen on the 15th of January 2021
    '''),

    dcc.Graph(
        id='sales-trend-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)

