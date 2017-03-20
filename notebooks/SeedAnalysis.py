
# coding: utf-8

# In[39]:

import pandas as pd
import pickle

from sklearn.ensemble import RandomForestClassifier


# In[18]:

df = pd.read_csv('../seeds.txt')
df.info()


# In[41]:

X, y = df.drop('targetClass', axis=1), df.targetClass

est = RandomForestClassifier(n_jobs=-1, n_estimators=50)
grid = dict(max_depth=[2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, None],
            max_features=[1, 2, 3, 4, 5, 6, 7],
            min_samples_split=[2, 3, 4, 5, 6, 7, 8, 9, 10]
           )
#gscv = GridSearchCV(est, param_grid=grid, cv=5)


# In[42]:

#gscv.fit(X, y)


# In[43]:

#gscv.best_params_, gscv.best_score_


# In[45]:

rf = RandomForestClassifier(n_jobs=-1, n_estimators=100, max_depth=6, max_features=7)


# In[48]:

rf.fit(X, y)


# In[50]:

with open('../seedclassifier.pickle', 'wb') as fl:
    pickle.dump(rf, fl)

