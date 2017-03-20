import io
import pickle
import base64
import random
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.misc import imresize


agg = pd.read_csv('emitrausedata.csv')
agg['instance'] = 1
with open('image_classifier.pickle', 'rb') as fl:
    image_classifier = pickle.load(fl)

def get_amounts_string():
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
    return string_amounts

def get_usage_string():
    ###########Plotting usages:
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
    return string_usage


def get_prediction(feature):
    X = [feature]
    with open('seedclassifier.pickle', 'rb') as fl:
        est = pickle.load(fl)
    p = est.predict_proba(X)
    classes = ['Kama', 'Rosa', 'Canadian']
    a, b, c = p[0]
    if a > b:
        if a > c:
            return 'Kama', a
        elif a <= c:
            return 'Canadian', c
    elif a <= b:
        if b > c:
            return 'Rosa', b
        elif b <= c:
            return 'Canadian', c

def get_image_classification(image):
    shape = (50, 72)
    image = imresize(image, shape)
    x = [image.flatten()]
    probas = image_classifier.predict_proba(x)
    a, b = probas[0]
    if a > b:
        return 'rice', a
    elif a < b:
        return 'wheat', b
    else:
        return ['rice', 'wheat'], [a, b]
