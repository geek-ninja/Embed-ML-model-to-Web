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