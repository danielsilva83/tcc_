from myapp import models
from  rest_framework import viewsets
from myapp.api import serializers

class ExperimentoViewSet(viewsets.ModelViewSet):
    queryset = models.Experimentos.objects.all()
    serializer_class = serializers.ExperimetoSerializer

class OriginalViewSet(viewsets.ModelViewSet):
    queryset = models.Original.objects.all()
    serializer_class = serializers.OriginalSerializer
    
class ResultadoViewSet(viewsets.ModelViewSet):
    queryset = models.Resultados.objects.all()
    serializer_class = serializers.ResultadoSerializer