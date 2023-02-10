
from django.shortcuts import render


def graf_medida1(request):
    if request.method == 'GET':
        form = [list(i) for i in request]
    #result = list_process_id(request, id)
    #print(result)
    contexts = form
    context = {'medida': form}
    return render(request,'medidas.html', context)