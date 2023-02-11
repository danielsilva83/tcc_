from django.urls import path, include
from myapp.api import viewsets as ExperimentoViewSet
from .app.load_files import load_files
from rest_framework import routers
from .app.list_process_id import list_process_id
from .app.graf_medida import graf_medida
from .app.build.build_process import build_process
from .app.start_build_process import start_build_process
from .app.list_process import list_process
from .app.list_experimento import list_experimento

urlpatterns = [
    path('', load_files, name='my-view'),
    path('result/gerar', build_process, name='build-process'),
    path('result/listar',  list_process, name='list-process'),
    path('result/listar',  list_experimento),
    path('result/result/<int:id>',  list_process_id),
    path('result/result/grafic',  graf_medida, name='graf-medida'),
    path('result/result', start_build_process, name='start-build-process'),

]

