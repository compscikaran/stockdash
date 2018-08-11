from dash import Dash
from flask import Flask, redirect, render_template, request
from analysis import get_stock_value
from graph import plot_graph
import dash_html_components as html

server = Flask(__name__)
app = Dash(__name__, server=server, url_base_pathname='/graph')
app.layout = html.Div('Welcome to Stock Dashboard')


@server.route('/')
def home():
    return render_template('index.html')


@server.route('/get_data')
def entry_point():
    name = request.args.get('lname')
    yvals, xvals = get_stock_value(name)
    plot_graph(app, xvals, yvals, name)
    return redirect('/graph')


if __name__ == '__main__':
    server.run(debug=True)
