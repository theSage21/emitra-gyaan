from bottle import Bottle, route, get, post, run, template, static_file
import io
import base64
import random
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def render(name, data={}):
    with open('templates/'+name) as fl:
        text = fl.read()
    text = template(text, **data)
    return text

app = Bottle()
agg = pd.read_csv('emitrausedata.csv')
agg['instance'] = 1

#########Plotting amounts
order = [(v, k) for k, v in dict(agg.groupby('hq')['BillAmount'].mean()).items()]
order.sort(key=lambda x: x[0], reverse=True)
order = [i[1] for i in order]
order[:10]

plt.figure(figsize=(10, 7))
sns.barplot(x='BillAmount', y='hq', data=agg, order=order)
plt.title('Average Bill amounts in Rajasthan Districts')
plt.xlabel('Average Bill Amount in Rs')
plt.ylabel('Districts')

buf = io.BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)
string_amounts = base64.b64encode(buf.getvalue())
plt.close()

###########Plotting usages
order = [(v, k) for k, v in dict(agg.groupby('hq')['instance'].count()).items()]
order.sort(key=lambda x: x[0], reverse=True)
order = [i[1] for i in order]
order[:10]

plt.figure(figsize=(10, 7))
sns.countplot(agg.hq, order=order)
ax = plt.gca()
ax.set_xticklabels(ax.xaxis.get_majorticklabels(), rotation=90)
plt.xlabel('District')
plt.ylabel('Usage count')
plt.title('e-Mitra Usage in the districts of Rajasthan')

buf = io.BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)
string_usage = base64.b64encode(buf.getvalue())
plt.close()
###############################

@app.route('/')
def home():
    html = render('home.html')
    return html

@app.get('/analytics')
def analytics():
    data = dict(amounts=string_amounts,
            usage=string_usage)
    html = render('analytics.html', data)
    return html

###############################
@app.get('/static/<path:path>')
def callback(path):
    return static_file(path, root='/home/arjoonn/dev/kaggle/jaipur/website/static')
app.run(host='localhost', port=8080, debug=True)
