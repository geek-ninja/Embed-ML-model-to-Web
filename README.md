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

<h2>Screenshot</h2>
<h3>Input page</h3>


![](1.png)

<h3>Result page </h3>

![](2.png)
