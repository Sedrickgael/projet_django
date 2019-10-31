from django.shortcuts import render
from django.db.models import Max, Min, Avg, Sum
from . import models

# Create your views here.

def home(request):
    pop=models.Population.objects.all().order_by('-nb_hbts')
    print(pop)
    datas={
        'population':pop
    }
    return render(request,'index.html', datas)

def stat(request):
    pop=models.Population.objects.all().order_by('-nb_hbts')
    # maxi=models.Population.objects.all().order_by('-nb_hbts')[:1]
    # mini=models.Population.objects.all().order_by('nb_hbts')[:1]
    maxi=models.Population.objects.aggregate(Max('nb_hbts'))
    mini=models.Population.objects.aggregate(Min('nb_hbts'))
    mini=models.Population.objects.aggregate(Min('nb_hbts'))
    moyen=models.Population.objects.values('nom', 'nb_hbts').aggregate(Avg('nb_hbts'))
    
    print(moyen)
    datas={
        'population':pop,
        'maxim':maxi,
        'minim':mini,
        'moyenn':moyen
    }
    return render(request,'stat.html', datas)