from django.shortcuts import render
from .models import Contact

def contact(request):
    contact=Contact.objects.all()

    ctx={
        'contact':contact,
    }

    return render(request,'index.html',ctx)


