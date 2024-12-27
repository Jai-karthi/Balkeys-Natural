from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('/News',views.News,name='News'),
    path('/events',views.events,name='events'),
   path('/About',views.About,name='About'),
   path('Exculsive/<int:id>', views.Exclusive, name='Exculsive'),
]
