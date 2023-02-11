from  rest_framework import serializers
from myapp import models

class ExperimetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Experimentos
        fields = '__all__'
        

class OriginalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Original
        fields = '__all__'

class ResultadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Resultados
        fields = '__all__'