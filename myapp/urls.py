from django.urls import path, include
from myapp.api import viewsets as ExperimentoViewSet

from rest_framework import routers
from .views import graf_medida, list_process_id, load_files
from .views import build_process
from .views import build_process1
from .views import list_process
from .views import list_experimento

urlpatterns = [
    path('', load_files, name='my-view'),
    path('result/gerar', build_process, name='build-process'),
    path('result/listar',  list_process, name='list-process'),
    path('result/listar',  list_experimento),
    path('result/result/<int:id>',  list_process_id),
    path('result/result/grafic',  graf_medida, name='graf-medida'),
    path('result/result', build_process1, name='build-process1'),

]

