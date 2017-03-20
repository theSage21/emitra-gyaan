from bottle import Bottle, route, get, post, run

app = Bottle()

@app.route('/')
def hello():
    return "Hello World!"

app.run(host='localhost', port=8080, debug=True)
