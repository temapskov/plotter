import sys
import datetime
from units.reader import ReadCsv

import dash
from dash.dependencies import Input, Output
from dash import dcc, html
import plotly.express as px


app = dash.Dash(__name__)

csv = ReadCsv(sys.argv[1])


def serve_layout():
    csv.update()
    groups = csv.get_groups()
    return html.Div([
        html.P("Выберите групппу для файла"),
        dcc.Dropdown(
            id="groups",
            value=1,
            options=groups,
            clearable=False,
        ),
        dcc.Graph(id="graph"),
        'Текущее время: ' + str(datetime.datetime.now())
        ])


app.layout = serve_layout


@app.callback(
    Output("graph", 'figure'),
    Input("groups", "value"))
def display_group(group_id: int):
    csv.update()
    df = csv.read_group(group_id)
    if df.get('z') is not None:
        return px.scatter_3d(
                df,
                x=df['x'],
                y=df['y'],
                z=df['z'],
                title=f'График для группы {group_id}'
            )
    return px.scatter(
        x=df['x'],
        y=df['y'],
        title=f'График для группы {group_id}'
        )


if __name__ == '__main__':
    for param in sys.argv:
        print(param)
    app.run_server(debug=False)
