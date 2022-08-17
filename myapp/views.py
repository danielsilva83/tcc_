from dataclasses import replace
from fileinput import filename
from io import BytesIO, StringIO
import json
from threading import Thread
from time import perf_counter
from typing import Literal
from urllib import request
import uuid
from django.shortcuts import redirect, render
from .models import Document
from .models import Experimento, Original, Resultados
from .forms import DocumentForm
import sqlite3
import re
import os
import sys
import pandas as pd
import pymfe
import glob
from pymfe.mfe import MFE
import requests 


    
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

def salvarOriginal(dataframeOriginal):
   
    conn = sqlite3.connect('db.sqlite3')
    dataframeOriginal.to_sql('original', conn, if_exists='append', index = True)
    conn.close()
    
def salvarResultados(dataframeResultados):
   
    conn = sqlite3.connect('db.sqlite3')
    dataframeResultados.to_sql('resultados', conn, if_exists = 'append', index=True)
    conn.close()

        
def salvarExperimentos(idexp, nome, arquivo, numero_repeticoes, tamanhos_reducao):
    
    conn = sqlite3.connect('db.sqlite3')
    experimentos = Experimento(idexp, nome, arquivo, numero_repeticoes, tamanhos_reducao)

    experimentos.save()

    conn.close()

        
def build_process(request):

    return render(request,'gerar.html')

def buld_list(nvezes_, nreduce, nome, documents, form):
  
 
    print(nvezes_)
    print(nreduce)

    nvezes_ = int(nvezes_)

    #pegar name = nome do arquivo

    #request.GET.get('nvezes')
    nvezes = nvezes_
    # #nvezes = numero de repetições do experimento para cada um dos conjuntos de dados

    list_df_ft = []
    list_reduce = []
    nfiles = 0
    for document in documents:

        listo = []
        file = document.docfile.url
        print(file)
        url = '.'+file
        
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        c.execute(f'SELECT * FROM myapp_experimento')
        countex = len(c.fetchall())
        idexp = countex+1
        c.close()
     
      
        salvarExperimentos(idexp, nome, file, nvezes_, nreduce)
        # os.path.join(data_path, file) #data = Pasta local onde se encontra os dataset, arquivos .csv 
        #all_files = glob.glob(r) #fazendo o carregamento dos datasets da pasta 'data' com os arquivos .csv

        mfe = MFE( groups=( "statistical"), summary=["mean", "sd", "min", "median", "max"]) # MFE Groups, passando 'ALL' com parametro para todos 
        #os grupos de medidas e sumarizando por ["mean", "sd", "min", "median", "max"]


        #files = [] # vetor para armazenar os Dataframes com os dados de cada dataset carregados
        files = pd.read_csv(url,encoding = "ISO-8859-1", decimal=",", header=0)
        nfiles = nfiles+1 #contando os arquivos
        print("\nArquivo numero: ",nfiles) #printando o numero do arquivo 
        print('Número de instâncias: {}\nNúmero de atributos: {}\n'.format(len(files), len(files.columns))) #printando informação sobre o daframe numero de instancias e atributos
        list_df_origin = files.values.tolist() # transformando o dataframe em uma lista para passar para o MFE
        mfe.fit(list_df_origin) # passando a lista de dados para o MFE opção Group (All)
        ft = mfe.extract() # extraindo as metricas do MFE Group (All)
        print('\nMFE - Groups (ALL) - DF Original ',"\n") #mostrando o parametro Groups= All passado para o MFE
        df_ft_ = pd.DataFrame (ft, columns=['cor.max', 'cor.mean', 'cor.median', 'cor.min', 'cor.sd', 'cov.max', 'cov.mean', 'cov.median', 'cov.min', 'cov.sd', 'eigenvalues.max', 'eigenvalues.mean', 'eigenvalues.median', 'eigenvalues.min', 'eigenvalues.sd', 'g_mean.max', 'g_mean.mean', 'g_mean.median', 'g_mean.min', 'g_mean.sd', 'h_mean.max', 'h_mean.mean', 'h_mean.median', 'h_mean.min', 'h_mean.sd', 'iq_range.max', 'iq_range.mean', 'iq_range.median', 'iq_range.min', 'iq_range.sd', 'kurtosis.max', 'kurtosis.mean', 'kurtosis.median', 'kurtosis.min', 'kurtosis.sd', 'mad.max', 'mad.mean', 'mad.median', 'mad.min', 'mad.sd', 'max.max', 'max.mean', 'max.median', 'max.min', 'max.sd', 'mean.max', 'mean.mean', 'mean.median', 'mean.min', 'mean.sd', 'median.max', 'median.mean', 'median.median', 'median.min', 'median.sd', 'min.max', 'min.mean', 'min.median', 'min.min', 'min.sd', 'nr_cor_attr', 'nr_norm', 'nr_outliers', 'range.max', 'range.mean', 'range.median', 'range.min', 'range.sd', 'sd.max', 'sd.mean', 'sd.median', 'sd.min', 'sd.sd', 'skewness.max', 'skewness.mean', 'skewness.median', 'skewness.min', 'skewness.sd', 'sparsity.max', 'sparsity.mean', 'sparsity.median', 'sparsity.min', 'sparsity.sd', 't_mean.max', 't_mean.mean', 't_mean.median', 't_mean.min', 't_mean.sd', 'var.max', 'var.mean', 'var.median', 'var.min', 'var.sd'])  #transformando a saida do MFE em um dataframe)

        origformat=df_ft_.drop(index = 0)
        origformat['id'] = idexp
        #resultados = salvarResultados(reducformat)) #transformando a saida do MFE em um dataframe
        salvarOriginal(origformat )
        
        
        #df_ft_b = df_ft_.to_sql () #passando o dataframe para o banco de dados
        #print(df_ft_b)
        print(df_ft_,"\n") #mostrando o DataFrame de saida do MFE opção Groups All
        df_ft = df_ft_.to_dict()
        df_ft = pd.DataFrame.from_dict(df_ft)
        df_ft = df_ft.to_json()
        
        #df_ft.to_sql(name='mfe_ft', con=engine, if_exists='replace', index=False)
        
        list_df_ft.insert(1,df_ft)

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
                print(ft1 ,"\n") #mostrando o DataFrame de saida do MFE opção Groups All
                df_ft_reduce = pd.DataFrame (ft1, columns=['cor.max', 'cor.mean', 'cor.median', 'cor.min', 'cor.sd', 'cov.max', 'cov.mean', 'cov.median', 'cov.min', 'cov.sd', 'eigenvalues.max', 'eigenvalues.mean', 'eigenvalues.median', 'eigenvalues.min', 'eigenvalues.sd', 'g_mean.max', 'g_mean.mean', 'g_mean.median', 'g_mean.min', 'g_mean.sd', 'h_mean.max', 'h_mean.mean', 'h_mean.median', 'h_mean.min', 'h_mean.sd', 'iq_range.max', 'iq_range.mean', 'iq_range.median', 'iq_range.min', 'iq_range.sd', 'kurtosis.max', 'kurtosis.mean', 'kurtosis.median', 'kurtosis.min', 'kurtosis.sd', 'mad.max', 'mad.mean', 'mad.median', 'mad.min', 'mad.sd', 'max.max', 'max.mean', 'max.median', 'max.min', 'max.sd', 'mean.max', 'mean.mean', 'mean.median', 'mean.min', 'mean.sd', 'median.max', 'median.mean', 'median.median', 'median.min', 'median.sd', 'min.max', 'min.mean', 'min.median', 'min.min', 'min.sd', 'nr_cor_attr', 'nr_norm', 'nr_outliers', 'range.max', 'range.mean', 'range.median', 'range.min', 'range.sd', 'sd.max', 'sd.mean', 'sd.median', 'sd.min', 'sd.sd', 'skewness.max', 'skewness.mean', 'skewness.median', 'skewness.min', 'skewness.sd', 'sparsity.max', 'sparsity.mean', 'sparsity.median', 'sparsity.min', 'sparsity.sd', 't_mean.max', 't_mean.mean', 't_mean.median', 't_mean.min', 't_mean.sd', 'var.max', 'var.mean', 'var.median', 'var.min', 'var.sd'])  #transformando a saida do MFE em um dataframe)

                reducformat=df_ft_reduce.drop(index = 0)
                reducformat['id_experimento'] = idexp
                salvarResultados(reducformat) 
                                              #id_original, id_resultados)
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

   
    #id_original, id_resultados)

    context = {'documents': documents, 'form': form, 'list_df_ft': list_df_ft, 'list_df_red': list_reduce, 'list': listo,
               'nreduc': nreduce, 'nfiles': nfiles , 'nvezes': nvezes , 'nome': nome}
    buld_list.retorno = context
   

def build(request):
    form = DocumentForm()  
    documents = Document.objects.all()
    nvezes_ = request.POST.get('numero')
    nreduce1 =  request.POST.get('reduce')
    nreduce1 = nreduce1.split(',')
    nreduce = ([float(x) for x in nreduce1])
    nome_ = request.POST.get('nome')
    # create 

    t = Thread(target=buld_list, args=(nvezes_, nreduce, nome_, documents, form))

    # start the threads
    t.start()
    t.join()
    return buld_list.retorno
   
def list_experimento(request):
   
    return render(request, 'listexperimento.html', buld_list.retorno)
#render(request, 'listexperimento.html', buld_list.retorno)

def build_process1(request):
    start_time = perf_counter()
    
  
    context = build(request)

    end_time = perf_counter()
    
    print(f'It took {end_time- start_time :0.2f} second(s) to complete.')
    
    return render(request,'list.html', context)
 
def list_process(request):
    result = Experimento.objects.all()
    list_result = [entry for entry in result]
    context = {'context': list_result}
    return render(request,'listar.html', context= context)


   