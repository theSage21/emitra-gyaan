import math
from scipy.misc import imread
from bottle import Bottle, route, get, post, run, template, static_file, request
from utils import get_amounts_string, get_usage_string, get_prediction, get_image_classification

def render(name, data={}):
    with open('templates/'+name) as fl:
        text = fl.read()
    text = template(text, **data)
    return text

app = Bottle()
###############################   GET

@app.get('/')
def home():
    html = render('home.html')
    return html

@app.get('/about')
def about():
    html = render('about.html')
    return html

@app.get('/contact')
def contact():
    html = render('contact.html')
    return html

@app.get('/analytics')
def analytics():
    data = dict(amounts=get_amounts_string(),
            usage=get_usage_string())
    html = render('analytics.html', data)
    return html

@app.get('/services')
def services():
    data = dict()
    html = render('services.html', data)
    return html

@app.get('/jobs')
def jobs():
    data = dict()
    html = render('jobs.html', data)
    return html


###############################  POST


@app.post('/seed-classification')
def seed_classification():
    # Get the data and prediction from model
    names = 'area,perimeter,kernel_length,kernel_width,asymmetry_coef,length_of_groove'.split(',')
    area, perimeter, kl, kw, ac, gl = [float(request.POST[i]) for i in names]
    compact = 4 * math.pi * area / (perimeter ** 2)
    feature = [area,perimeter,compact,kl,kw,ac,gl]
    pred, proba = get_prediction(feature)

    data = dict(seed_label=pred,
            confidence=proba)

    html = render('seed.html', data)
    return html

@app.post('/image-seeds')
def image_seeds():
    # Get the image
    img_id = request.forms.get('id')
    img_src = request.files.get('upload')
    img_src.save(img_src.filename)
    image = imread(img_src.filename)
    # get prediction
    pred, proba = get_image_classification(image)
    data = dict(seed_label=pred,
            confidence=proba)

    html = render('imageseed.html', data)
    return html
###############################
@app.get('/static/<path:path>')
def callback(path):
    return static_file(path, root='/home/arjoonn/dev/kaggle/jaipur/website/static')
app.run(host='localhost', port=8080, debug=True)
