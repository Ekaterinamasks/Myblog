from django.urls import path
from . import views

from blog import views
urlpatterns = [

    path("", views.all_blog, name='all_blog'),

]
