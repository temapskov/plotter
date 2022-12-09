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
            value=groups[0],
            # disabled=True,
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
            groups.index()
            return groups[-1]
        else:
            return groups[groups.index(group)-1]
    elif "btn-next-click" == ctx.triggered_id:
        if group == groups[-1]:
            return groups[0]
        else:
            return groups[groups.index(group)+1]
    else:
        return group
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
    # print(df[0])
    labels = list(df.columns)
    if len(labels) > 3:
        return px.scatter_3d(
                df,
                            # 2.9937e-95;3.70795e-95;5.53932e-95;20101
                            # 3.83699e-91;4.75244e-91;7.09968e-91;20101
                            # 4.75912e-87;5.89457e-87;8.80592e-87;20101
                            # 5.70212e-83;7.06257e-83;1.05508e-82;20101
                            # 6.58665e-79;8.15813e-79;1.21874e-78;20101
                            # 7.31929e-75;9.06556e-75;1.3543e-74;20101
                # x=[2.9937e-95,3.83699e-91,4.75912e-87,5.70212e-83,6.58665e-79],
                # y=[3.70795e-95,4.75244e-91,5.89457e-87,7.06257e-83,8.15813e-79],
                # z=[3.70795e-95,4.75244e-91,5.89457e-87,7.06257e-83,8.15813e-79],
                # x = [1,2,3],
                # y = [2,3,4],
                # z = [5,2,1],
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
    app.run_server(debug=True)
