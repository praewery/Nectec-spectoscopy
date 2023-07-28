from django.urls import path
from app import views
from app.chart import test2

urlpatterns = [
    path('', views.index, name='index'),
    path('charts.html', views.charts, name='charts'),
    path('index.html', views.index, name='index'),
]

