from django.urls import path
from . import views


urlpatterns = [
    path('printLastMessage/', views.printLastMessage, name='printLastMessage'),
    path('', views.printMainPage, name = 'printMainPage'),
    path('showGraph/', views.showGraph, name = 'showGraph'),
    path('currentPoint/<slug:numPoint>', views.currentPoint, name = 'currentPoint')
]