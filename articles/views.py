from django.shortcuts import render

from articles.models import Hello, Articles


def about(request):
    salom=Hello.objects.all()
    art=Articles.objects.all()

    ctx={
        'salom':salom,
        'art':art,
    }

    return render(request,'index.html',ctx)