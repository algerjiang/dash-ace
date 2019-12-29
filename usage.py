import dash
import dash_ace
import dash_html_components as html
import flask
from flask import request, jsonify
from flask_cors import CORS

server = flask.Flask(__name__)
CORS(server)

app = dash.Dash(__name__,
                server=server,
                routes_pathname_prefix='/dash/'
                )

app.layout = html.Div([
    dash_ace.DashAceEditor(
        id='input',
        value='test(a: Integer) -> String := \n'
              '    return f"value is {a}"',
        theme='github',
        mode='norm',
        tabSize=2,
        enableBasicAutocompletion=True,
        enableLiveAutocompletion=True,
        autocompleter='/autocompleter?prefix=',
        prefixLine=True,
        triggerWords=[':', '\\.', '::'],
        placeholder='Norm code ...'
    ),
    html.Div(id='output')
])


@server.route('/autocompleter', methods=['GET'])
def autocompleter():
    return jsonify([{"name": "Completed", "value": "Completed", "score": 300, "meta": "test"}])


if __name__ == '__main__':
    app.run_server(debug=True)
