from django.urls import path
from . import views


urlpatterns = [
    path('',views.predict),
    path('results',views.result)
]