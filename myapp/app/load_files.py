from django.shortcuts import redirect, render

from myapp.forms import DocumentForm
from myapp.models import Document

    
def load_files(request):
    print(f"Excelente! Você está usando o Python 3.6+. Se você falhar aqui, use a versão correta.")
    message = 'Carregue novos arquivos no formato .csv!'
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])

            newdoc.save()

            # Redirect to the document list after POST
            return redirect('my-view')
        else:
            message = 'O formulário não é válido. Corrija o seguinte erro:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'list.html', context)