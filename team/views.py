from django.shortcuts import render
from .models import Team,HappyClients

def team(request):
    team=Team.objects.all()
    home=HappyClients.objects.all()


    ctx={
        'team':team,
        'home': home,
    }

    return render(request,'index.html',ctx)
