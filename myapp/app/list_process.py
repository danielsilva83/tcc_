from django.shortcuts import render
from myapp.models import Documentexp, Experimento


def list_process(request):
    result = Experimento.objects.all()
    documents = Documentexp.objects.all()
    list_documents = [entry for entry in documents]
    list_result = [entry for entry in result]
    context = {'context': list_result,  'doc': list_documents}
    return render(request,'listar.html', context= context )