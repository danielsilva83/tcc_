from django.urls import path
from .views import my_view
from .views import my_result

urlpatterns = [
    path('', my_view, name='my-view'),
    path('result', my_result, name='my-result')
   
]

