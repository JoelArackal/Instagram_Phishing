from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('joku10/video/<int:id>',views.index, name='index')
]