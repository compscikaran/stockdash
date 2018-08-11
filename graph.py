
import dash_core_components as dcc
import dash_html_components as html


def plot_graph(app, xvalues, yvalues, title):
    app.layout = html.Div(children=[
        html.H1(title + ' Close Prices'),
        dcc.Graph(id='stock_close',
                figure={
                    'data': [
                        {
                            'x': xvalues,
                            'y': yvalues,
                            'type': 'line',
                            'name': title
                        }
                    ]
                })
    ])
