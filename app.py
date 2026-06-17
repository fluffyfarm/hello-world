from dash import Dash, html

app = Dash()

app.layout = [html.Div(children=[
    html.H1(children="Hello World")
    ])
]

server = app.server

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050)