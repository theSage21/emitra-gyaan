from bottle import Bottle, route, get, post, run

def template(name):
    with open('templates/'+name) as fl:
        text = fl.read()
    return text

app = Bottle()

###############################

@app.route('/')
def home():
    html = template('home.html')
    return html

###############################
app.run(host='localhost', port=8080, debug=True)
