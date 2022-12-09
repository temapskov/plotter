import sys
from units.reader import ReadCsv

import dash
from dash.dependencies import Input, Output
from dash import dcc, html, ctx
import plotly.express as px


app = dash.Dash(__name__)

csv = ReadCsv(sys.argv[1])


def serve_layout():
    csv.update()
    groups = csv.get_groups()
    return html.Div([
        dcc.Dropdown(
            id="groups",
            value=1,
            disabled=True,
            options=groups,
            clearable=False,
        ),
        html.Button('Prev', id='btn-prev-click', n_clicks=0),
        html.Button('Next', id='btn-next-click', n_clicks=0),
        dcc.Graph(id="graph"),
        ])

app.layout = serve_layout

@app.callback(
    Output('groups', 'value'),
    Input('btn-prev-click', 'n_clicks'),
    Input('btn-next-click', 'n_clicks'),
    Input('groups', 'value'),
    Input('groups', 'options'),
)
def displayClick(btn1, btn2, group: int, groups: list):
    csv.update()
    if "btn-prev-click" == ctx.triggered_id:
        if group == groups[0]:
            return groups[-1]
        else:
            return group - 1
    elif "btn-next-click" == ctx.triggered_id:
        if group == groups[-1]:
            return groups[0]
        else:
            return group + 1
    else:
        return 1
    # elif "btn-nclicks-2" == ctx.triggered_id:
    #     msg = "Button 2 was most recently clicked"
    # elif "btn-nclicks-3" == ctx.triggered_id:
    #     msg = "Button 3 was most recently clicked"
    # return 2

@app.callback(
    Output("graph", "figure"),
    Input("groups", "value"))
def display_group(group_id: int):
    csv.update()
    df = csv.read_group(group_id)
    labels = list(df.columns)
    if len(labels) > 3:
        return px.scatter_3d(
                df,
                x=labels[0],
                y=labels[1],
                z=labels[2],
                title=f'График для группы {group_id}',
                )
    else:
        return px.scatter(
            df,
            x=labels[0],
            y=labels[1],
            title=f'График для группы {group_id}'
            )


if __name__ == '__main__':
    for param in sys.argv:
        print(param)
    app.run_server(debug=False)
