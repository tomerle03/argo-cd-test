from flask import Flask

app = Flask(__name__)

names = "tomer leibovitch\nliad mizrahi\nitay shitrit\nron limor\nshaked stern"
@app.route("/")
def hello_world():
    return names
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')