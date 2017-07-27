import requests
import flask

app = flask.Flask(__name__)

STATUS = 'None'

COLORS = [("Red", (255, 0, 0, 0)),
          ("Green", (0, 255, 0, 0)),
          ("Blue", (0, 0, 255, 0)),
          ("White", (0, 0, 0, 8))]

COLOR_INDEX = 0


@app.route('/', methods=['GET'])
def statusGet():
    global COLOR_INDEX
    global COLORS
    color = COLORS[COLOR_INDEX % len(COLORS)]
    c_data = color[1]
    data = {'pattern': 'solid',
            'color': c_data}
    return flask.jsonify(data)


@app.route('/control', methods=['GET', 'POST'])
def controlHandle():
    global COLOR_INDEX
    global COLORS
    color = COLORS[COLOR_INDEX % len(COLORS)]
    c_name = color[0]

    if flask.request.method == 'POST':
        try:
            if flask.request.form['control'] == 'Cycle':
                COLOR_INDEX += 1
            return flask.redirect('/control', 302)
        except:
            return flask.redirect('/control', 302)
    elif flask.request.method == 'GET':
        return flask.render_template('control.html', status=c_name)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
