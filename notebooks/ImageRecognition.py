
# coding: utf-8

# In[1]:

import pandas as pd
import bs4
import requests
import os
from scipy.misc import imresize
from bleedml.classifiers import CascadeForest
from bleedml.utils import multi2Dscan, scan2D
from sklearn.model_selection import cross_val_score
import pickle
from sklearn.ensemble import RandomForestClassifier
from importlib import reload
from scipy.misc import imread, imsave, imresize
import numpy as np


# In[2]:

def get_image_links(search, limit=100):
    link = 'https://www.google.com/search?q={search}&oq={search}&start={start}'
    start = 0
    links = []
    while len(links) < limit:
        print(start)
        page = requests.get(link.format(search=search, start=0))
        if page.status_code == 200:
            soup = bs4.BeautifulSoup(page.text, 'html5lib')
            newlinks = [i.get('src') for i in soup.find_all('img')]
            start += len(newlinks)
            links.extend(newlinks)
        else:
            print('error in link')
    return links


# In[3]:

if not os.path.exists('wheatlinks'):
    links = get_image_links('wheat')
    links = list(set(links))
    with open('wheatlinks', 'w') as fl:
        fl.write('\n'.join(links))


# In[4]:

if not os.path.exists('ricelinks'):
    links = get_image_links('rice')
    links = list(set(links))
    with open('ricelinks', 'w') as fl:
        fl.write('\n'.join(links))



# ### Creating training dataset

# In[5]:

wheat_paths = []
for fl in os.listdir('../images/wheat/'):
    path = '../images/wheat/' + fl
    wheat_paths.append(path)


# In[6]:

rice_paths = []
for fl in os.listdir('../images/rice/'):
    path = '../images/rice/' + fl
    rice_paths.append(path)


# In[7]:

wx, wy = set(), set()
for path in wheat_paths:
    x, y, _  = imread(path).shape
    wx.add(x); wy.add(y)


# In[8]:

for path in rice_paths:
    x, y, _  = imread(path).shape
    wx.add(x); wy.add(y)
wx = list(sorted(wx))
wy = list(sorted(wy))
wx[0], wy[0]


# In[9]:

images, labels = [], []
for path in rice_paths:
    image = imresize(imread(path), (wx[0], wy[0]))
    images.append(image)
    labels.append('rice')
for path in wheat_paths:
    image = imresize(imread(path), (wx[0], wy[0]))
    images.append(image)
    labels.append('wheat')
mask = np.random.random(len(labels)) < 1
images = np.array(images)[mask]
labels = np.array(labels)[mask]

print(len(labels))
print(images.shape)


# In[10]:

X, y = [i.flatten() for i in images], labels
scores = cross_val_score(RandomForestClassifier(n_jobs=-1), X, y, cv=3)
print(scores)


# In[11]:

est = RandomForestClassifier(n_jobs=-1)
est.fit(X, y)


# In[12]:

with open('../image_classifier.pickle', 'wb') as fl:
    pickle.dump(est, fl)


# In[13]:

est.classes_

