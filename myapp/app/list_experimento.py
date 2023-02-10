from django.shortcuts import render

from myapp.app.build.build_list import build_list


def list_experimento(request):
   
    return render(request, 'listexperimento.html', build_list.retorno)