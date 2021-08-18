from django.urls import path

from .views import homepage,todo,display

urlpatterns = [
    
    path('', homepage),
    path('todo',todo,name='todo'),
    path('display',display)
]