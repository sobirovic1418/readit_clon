from django.shortcuts import render
from .models import Team,Home

def team(request):
    team=Team.objects.all()
    home=Home.objects.all()


    ctx={
        'team':team,
        'home': home,
    }

    return render(request,'index.html',ctx)
