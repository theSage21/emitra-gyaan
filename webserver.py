from bottle import Bottle, route, get, post, run, template, static_file

def render(name, data={}):
    with open('templates/'+name) as fl:
        text = fl.read()
    text = template(text, **data)
    return text

app = Bottle()

###############################

@app.route('/')
def home():
    html = render('home.html')
    return html


###############################
@app.get('/static/<path:path>')
def callback(path):
    return static_file(path, root='/home/arjoonn/dev/kaggle/jaipur/website/static')
app.run(host='localhost', port=8080, debug=True)
