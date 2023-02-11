from threading import Thread

from myapp.app.build.build_list import build_list
from myapp.forms import DocumentForm
from myapp.models import Document


async def build_start(request):
    form = DocumentForm()  
    documents = Document.objects.all()
    nvezes_ = request.POST.get('numero')
    nreduce1 =  request.POST.get('reduce')
    nreduce1 = nreduce1.split(',')
    nreduce = ([float(x) for x in nreduce1])
    nome_ = request.POST.get('nome')
    # create 

    t = Thread(target=build_list, args=(nvezes_, nreduce, nome_, documents, form))

    # start the threads
    t.start()
    t.join()
    
    return build_list