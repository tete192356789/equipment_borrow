from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('api/all-faculties/',all_faculties),
    path('api/all-items/',all_items),
    
]