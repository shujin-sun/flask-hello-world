import dash

app = dash.Dash(compress=True)
server = app.server
app.title = "dash应用示例"
