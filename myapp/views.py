from django.shortcuts import redirect, render
from .models import Document
from .forms import DocumentForm


def my_view(request):
    print(f"Excelente! Você está usando o Python 3.6+. Se você falhar aqui, use a versão correta.")
    message = 'Carregue quantos arquivos desejar!!'
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
