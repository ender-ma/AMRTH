from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("create/", views.create, name="create"),

]

"""path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path("<str:name>/", views.index, name="index"),"""