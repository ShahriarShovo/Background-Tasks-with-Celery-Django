from django.urls import path
from a_meessageboard.views import *


urlpatterns = [
    path('', messageboard_view, name='messageboard'),
    path('subscribe/', subscribe, name="subscribe"),
    
    path('newsletter/', newsletter, name="newsletter"),
]

