from django.urls import path

from .views import team,home

urlpatterns={
    path('',team),
    path('',home)
}