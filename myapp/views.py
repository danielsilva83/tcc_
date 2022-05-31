from io import BytesIO, StringIO
import json
from typing import Literal
from django.shortcuts import redirect, render
from .models import Document
from .forms import DocumentForm
import re
import os
import sys
import pandas as pd
import pymfe
import glob
from pymfe.mfe import MFE
import requests


    
def my_view(request):
    print(f"Excelente! Você está usando o Python 3.6+. Se você falhar aqui, use a versão correta.")
    message = 'Carregue novos arquivos no formato .csv!!'
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

def my_result(request):

    form = DocumentForm()  
    documents = Document.objects.all()
    nvezes = request.GET.get('nvezes','')
    nvezes = int(nvezes)
    #2 #nvezes = numero de repetições do experimento para cada um dos conjuntos de dados
    nreduce = [0.1,0.12] #nreduce = lista com as porcentagens de redução para cada conjunto de dados
    list_df_ft = []
    list_reduce = []
    nfiles = 0
    for document in documents:
        list_reduce1 = []
        listo = []
        file = document.docfile.url
        print(file)
        url = '.'+file

        # os.path.join(data_path, file) #data = Pasta local onde se encontra os dataset, arquivos .csv 
        #all_files = glob.glob(r) #fazendo o carregamento dos datasets da pasta 'data' com os arquivos .csv

        mfe = MFE( groups=( "statistical"), summary=["mean", "sd", "min", "median", "max"]) # MFE Groups, passando 'ALL' com parametro para todos 
        #os grupos de medidas e sumarizando por ["mean", "sd", "min", "median", "max"]


        #files = [] # vetor para armazenar os Dataframes com os dados de cada dataset carregados
        files = pd.read_csv(url,encoding = "ISO-8859-1", decimal=",", header=0)
        #i = 0 # variavel contadora para contabilizar o numero de repetições do experimento
        #for file_ in r: #laço de repetição para ler todos os arquivos da pasta local 'data'
            #filepath_ = file # extraindo e armazenando o caminho e nome do arquivo .csv
        #files.append(pd.read_csv(url,encoding = "ISO-8859-1", decimal=",", header=0)) #transformando o csv e um DataFrame pandas e armazenando-o em vetor
        #print(files) #printando o caminho e os nomes dos arquivos carregados

        #nfiles = 0    #variavel contadora para armazenar o numero de arquivos carregados
        #for df in files: #laço para iterara o vetor com os datafremes que foram armazenados
        nfiles = nfiles+1 #contando os arquivos
        print("\nArquivo numero: ",nfiles) #printando o numero do arquivo 
        print('Número de instâncias: {}\nNúmero de atributos: {}\n'.format(len(files), len(files.columns))) #printando informação sobre o daframe numero de instancias e atributos
        list_df_origin = files.values.tolist() # transformando o dataframe em uma lista para passar para o MFE

        mfe.fit(list_df_origin) # passando a lista de dados para o MFE opção Group (All)
        ft = mfe.extract() # extraindo as metricas do MFE Group (All)
        print('\nMFE - Groups (ALL) - DF Original ',"\n") #mostrando o parametro Groups= All passado para o MFE
        df_ft_ = pd.DataFrame (ft) #transformando a saida do MFE em um dataframe
        print(df_ft_,"\n") #mostrando o DataFrame de saida do MFE opção Groups All
        df_ft = df_ft_.to_dict()
        df_ft = pd.DataFrame.from_dict(df_ft)
        df_ft = df_ft.to_json()
        list_df_ft.insert(1,df_ft)
        
        #list_df_ft= (by.getvalue())
        #list_df_ft=re.sub(r"'\'", '',list_df_ft)
        for i in range(nvezes): #laço para repetir o experimento n vezes

        ########################## inicio processamento dos datasets originais no MFE ######################################
 
            for reduce in nreduce: #laço para realizar a redução de dados a partir dos datasets originais nreduce =  valor em porcento das reduções
            ########################## inicio processamento dos datasets Reduzidos no MFE ######################################
                print("\n tamanho da Redução: ", reduce)# mostrando o tamanho da redução
                random_df = files.sample(frac=reduce) #realizando a redução aleatoria do dataset
                list_df_reduce = random_df.values.tolist() # transformando o dataframe em lista para enviar para o MFE

                mfe.fit(list_df_reduce) # passando a lista de dados para o MFE opção Group (All)
                ft1 = mfe.extract() # extraindo as metricas do MFE Group (All)
                print('\nMFE - Groups (ALL) - DF Reduzido ',"\n") #mostrando o parametro Groups= All passado para o MFE
                df_ft_reduce = pd.DataFrame (ft1) #transformando a saida do MFE em um dataframe
                df_ft_reduce = df_ft_reduce.append(df_ft_.loc[1],ignore_index=True)
               
                #df_ft_reduce('value1', df_ft_.loc[1])
                print(df_ft_reduce,"\n") #mostrando o DataFrame de saida do MFE opção Groups All

              
                df_ft_reduce = df_ft_reduce.to_dict()
                df_ft_reduce = pd.DataFrame.from_dict(df_ft_reduce)
                df_ft_reduce = df_ft_reduce.to_json()
                #df_ft_reduce = df_ft_reduce.to_json()

                list_reduce.append(df_ft_reduce)
                b = [list_df_ft,list_reduce]
                listo.append(b)
            
            print("**********************Numero de Repetições da Redução: ",i+1,"***********************************************************\n")

    context = {'documents': documents, 'form': form, 'list_df_ft': list_df_ft, 'list_df_red': list_reduce, 'list': listo,
               'nreduc': nreduce, 'nfiles': nfiles , 'nvezes': nvezes }
    return render(request,'result.html',context)
