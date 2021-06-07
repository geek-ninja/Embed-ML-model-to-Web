# Embed-ML-model-to-Web
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

<h2>This is a simple web based ML mode</h2>
<p>Aim of the model is to get the weightage of the elements as input for the type glass and predict the type of glass usage</p>
<br><br>
<p>The Model folder contains the ML program in python which is converted to .sav using joblib python module.</p>
<p>That .sav file is used in django to integrate with the website</p>
<br><br>
<p>The djangoMl folder contains the django files which using put it in your django virtual environment and add the path (urls.py)to this folder</p>
<p>The ml folder contains the template of the website in html format (home.html for input) and (result.html for output)</p>
<p>Adjust the setting.py file in django so that you can integrate the template with the django view.py </p>
<p>Similar way you can add your model and adjust the webiste too.</p>

<h3>Important python module</h3>
<p>joblib</p>
<p> pip3 install joblib</p>
<p>This module will convert the python Ml model to sav file which can be further used in django-website to predict result</p>
<br><br>

<h2>Machine Learning mode used</h2>
<p>random forest</p>

```python

import numpy as np
import pandas as pd
import joblib

dataset = pd.read_csv('glass.csv')

x = dataset.iloc[:,:-1]
y = dataset.iloc[:,9]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.20,random_state = 42)

from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)

from sklearn.ensemble import RandomForestClassifier

clss = RandomForestClassifier(criterion='entropy',n_estimators=300,random_state=42)
clss.fit(x_train,y_train)

print('accuracy is ', clss.score(x_test,y_test)*100,'%')

#saving the model
filename = 'finalized_model.sav'
joblib.dump(clss,filename)
```

<h2>Code Snippet used in django views</h2>
<p>view.py</p>

```python

from django.shortcuts import render
import joblib
# Create your views here.
def home_view(request):
    return render(request,"ml/home.html")

def result_view(request):
    clss = joblib.load('model/finalized_model.sav')
    lis = []
    lis.append(request.GET['RI'])
    lis.append(request.GET['Na'])
    lis.append(request.GET['Mg'])
    lis.append(request.GET['Al'])
    lis.append(request.GET['Si'])
    lis.append(request.GET['K'])
    lis.append(request.GET['Ca'])
    lis.append(request.GET['Ba'])
    lis.append(request.GET['Fe'])
    
    ans = clss.predict([lis])
    
    usage = [
        'building windows float processed',
        'building windows non float processed',
        'vehicle windows  float processed',
        'vehicle windows float processed (none in this dataset)',
        'containers',
        'tableware',
        'headlamps'
    ]
    
    return render(request,"ml/result.html",{'ans':usage[ans[0] - 1]})
```

<h2>Screenshot</h2>
<h3>Input page</h3>


![](1.png)

<h3>Result page </h3>

![](2.png)
