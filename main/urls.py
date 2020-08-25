# ---------------------------------------- [edit] ---------------------------------------- #
from django.urls import path

from . import views



app_name = 'main'


# ---------------------------------------------------------------------------------------- #
urlpatterns = [
    # ---------------------------------------- [edit] ---------------------------------------- #
    path('', views.to_main, name='to_main'),
    path('main/', views.index, name='index'),]