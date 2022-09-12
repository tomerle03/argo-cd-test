import flask

app = flask.Flask(__name__)

names = "tomer leibovitch\nliad mizrahi\nitay shitrit\nron limor\nshaked stern"

@app.route('/check')
def returnNames():
    return names

if __name__ == "__main__":
    app.run()