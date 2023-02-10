import sqlite3
from turtle import pd

from multiprocessing.sharedctypes import Value

from django.shortcuts import redirect, render
import sqlite3
import pandas as pd
import pymfe
from pymfe.mfe import MFE
from myapp.app.build.salvarDf_Original import salvarDf_Original
from myapp.app.build.salvarDf_Reduc import salvarDf_Reduc
from myapp.app.build.salvarExperimento import salvarExperimentos
from myapp.app.build.salvarOriginal import salvarOriginal
from myapp.app.build.salvarResultados import salvarResultados
from myapp.models import  Experimento
        

def build_list(nvezes_, nreduce, nome, documents, form):
  
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
        name_file = file
        urlsaida = '../export'+name_file
        
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        c.execute(f'SELECT * FROM myapp_experimento')
        countex = len(c.fetchall())
        idexp = countex+1
        c.close()
        nomef=''
        nomef = nome+'_'+ file
     
      
        #salvarExperimentos(idexp, nomef, file, nvezes_, nreduce)
        # os.path.join(data_path, file) #data = Pasta local onde se encontra os dataset, arquivos .csv 
        #all_files = glob.glob(r) #fazendo o carregamento dos datasets da pasta 'data' com os arquivos .csv
        
        mfe = MFE( groups=["general", "statistical", "info-theory"], summary=["mean", "sd", "min", "median", "max"]) # MFE Groups, passando 'ALL' com parametro para todos 
        #os grupos de medidas e sumarizando por ["mean", "sd", "min", "median", "max"]


        #files = [] # vetor para armazenar os Dataframes com os dados de cada dataset carregados
        files = pd.read_csv(url,encoding = "UTF8", decimal=",", header=0)
        nfiles = nfiles+1 #contando os arquivos
        print("\nArquivo numero: ",nfiles) #printando o numero do arquivo 
        print('Número de instâncias: {}\nNúmero de atributos: {}\n'.format(len(files), len(files.columns))) #printando informação sobre o daframe numero de instancias e atributos
        list_df_origin = files.values.tolist() # transformando o dataframe em uma lista para passar para o MFE
        mfe.fit(list_df_origin) # passando a lista de dados para o MFE opção Group (All)
        try:
            ft = mfe.extract() # extraindo as metricas do MFE Group (All)
      
        except pymfe.mfe.MFEError:
                print("Erro no arquivo: ", file)
                continue
            
        print('\nMFE - Groups (ALL) - DF Original ',"\n") #mostrando o parametro Groups= All passado para o MFE
        df_ft_ = pd.DataFrame (ft, columns=['attr_conc.max', 'attr_conc.mean', 'attr_conc.median', 'attr_conc.min', 'attr_conc.sd', 'attr_ent.max', 'attr_ent.mean', 'attr_ent.median', 'attr_ent.min', 'attr_ent.sd', 'attr_to_inst', 'cat_to_num', 'cor.max', 'cor.mean', 'cor.median', 'cor.min', 'cor.sd', 'cov.max', 'cov.mean', 'cov.median', 'cov.min', 'cov.sd', 'eigenvalues.max', 'eigenvalues.mean', 'eigenvalues.median', 'eigenvalues.min', 'eigenvalues.sd', 'g_mean.max', 'g_mean.mean', 'g_mean.median', 'g_mean.min', 'g_mean.sd', 'h_mean.max', 'h_mean.mean', 'h_mean.median', 'h_mean.min', 'h_mean.sd', 'inst_to_attr', 'iq_range.max', 'iq_range.mean', 'iq_range.median', 'iq_range.min', 'iq_range.sd', 'kurtosis.max', 'kurtosis.mean', 'kurtosis.median', 'kurtosis.min', 'kurtosis.sd', 'mad.max', 'mad.mean', 'mad.median', 'mad.min', 'mad.sd', 'max.max', 'max.mean', 'max.median', 'max.min', 'max.sd', 'mean.max', 'mean.mean', 'mean.median', 'mean.min', 'mean.sd', 'median.max', 'median.mean', 'median.median', 'median.min', 'median.sd', 'min.max', 'min.mean', 'min.median', 'min.min', 'min.sd', 'nr_attr', 'nr_bin', 'nr_cat', 'nr_cor_attr', 'nr_inst', 'nr_norm', 'nr_num', 'nr_outliers', 'num_to_cat', 'range.max', 'range.mean', 'range.median', 'range.min', 'range.sd', 'sd.max', 'sd.mean', 'sd.median', 'sd.min', 'sd.sd', 'skewness.max', 'skewness.mean', 'skewness.median', 'skewness.min', 'skewness.sd', 'sparsity.max', 'sparsity.mean', 'sparsity.median', 'sparsity.min', 'sparsity.sd', 't_mean.max', 't_mean.mean', 't_mean.median', 't_mean.min', 't_mean.sd', 'var.max', 'var.mean', 'var.median', 'var.min', 'var.sd'])  #transformando a saida do MFE em um dataframe)
        #, columns=['attr_conc.max', 'attr_conc.mean', 'attr_conc.median', 'attr_conc.min', 'attr_conc.sd', 'attr_ent.max', 'attr_ent.mean', 'attr_ent.median', 'attr_ent.min', 'attr_ent.sd', 'attr_to_inst', 'cat_to_num', 'cor.max', 'cor.mean', 'cor.median', 'cor.min', 'cor.sd', 'cov.max', 'cov.mean', 'cov.median', 'cov.min', 'cov.sd', 'eigenvalues.max', 'eigenvalues.mean', 'eigenvalues.median', 'eigenvalues.min', 'eigenvalues.sd', 'g_mean.max', 'g_mean.mean', 'g_mean.median', 'g_mean.min', 'g_mean.sd', 'h_mean.max', 'h_mean.mean', 'h_mean.median', 'h_mean.min', 'h_mean.sd', 'inst_to_attr', 'iq_range.max', 'iq_range.mean', 'iq_range.median', 'iq_range.min', 'iq_range.sd', 'kurtosis.max', 'kurtosis.mean', 'kurtosis.median', 'kurtosis.min', 'kurtosis.sd', 'mad.max', 'mad.mean', 'mad.median', 'mad.min', 'mad.sd', 'max.max', 'max.mean', 'max.median', 'max.min', 'max.sd', 'mean.max', 'mean.mean', 'mean.median', 'mean.min', 'mean.sd', 'median.max', 'median.mean', 'median.median', 'median.min', 'median.sd', 'min.max', 'min.mean', 'min.median', 'min.min', 'min.sd', 'nr_attr', 'nr_bin', 'nr_cat', 'nr_cor_attr', 'nr_inst', 'nr_norm', 'nr_num', 'nr_outliers', 'num_to_cat', 'range.max', 'range.mean', 'range.median', 'range.min', 'range.sd', 'sd.max', 'sd.mean', 'sd.median', 'sd.min', 'sd.sd', 'skewness.max', 'skewness.mean', 'skewness.median', 'skewness.min', 'skewness.sd', 'sparsity.max', 'sparsity.mean', 'sparsity.median', 'sparsity.min', 'sparsity.sd', 't_mean.max', 't_mean.mean', 't_mean.median', 't_mean.min', 't_mean.sd', 'var.max', 'var.mean', 'var.median', 'var.min', 'var.sd']
        origformat=df_ft_.drop(index = 0)
        origformat['id'] = idexp
        #resultados = salvarResultados(reducformat)) #transformando a saida do MFE em um dataframe
        salvarOriginal(origformat )
        salvarDf_O = salvarDf_Original(origformat, nome,name_file )
        
        #df_ft_b = df_ft_.to_sql () #passando o dataframe para o banco de dados
        #print(df_ft_b)
        print(df_ft_,"\n") #mostrando o DataFrame de saida do MFE opção Groups All
        df_ft = df_ft_.to_dict()
        df_ft = pd.DataFrame.from_dict(df_ft)
        df_ft = df_ft.to_json()
        
        #df_ft.to_sql(name='mfe_ft', con=engine, if_exists='replace', index=False)
        
        list_df_ft.insert(1,df_ft)
        listreducformat = []
        for i in range(nvezes): #laço para repetir o experimento n vezes

        ########################## inicio processamento dos datasets originais no MFE ######################################
           
            for reduce in nreduce: #laço para realizar a redução de dados a partir dos datasets originais nreduce =  valor em porcento das reduções
            ########################## inicio processamento dos datasets Reduzidos no MFE ######################################
               
            
                print("\n tamanho da Redução: ", reduce)# mostrando o tamanho da redução
                random_df = files.sample(frac=reduce) #realizando a redução aleatoria do dataset
                list_df_reduce = random_df.values.tolist() # transformando o dataframe em lista para enviar para o MFE

                mfe.fit(list_df_reduce) # passando a lista de dados para o MFE opção Group (All)
                #ft1 = mfe.extract() # extraindo as metricas do MFE Group (All)
                try:
                    ft1 = mfe.extract() # extraindo as metricas do MFE Group (All)
            
                except pymfe.mfe.MFEError:
                        print("Erro no arquivo: ", file)
                        continue
            
                print('\nMFE - Groups (ALL) - DF Reduzido ',"\n") #mostrando o parametro Groups= All passado para o MFE
                print(ft1 ,"\n") #mostrando o DataFrame de saida do MFE opção Groups All
                df_ft_reduce = pd.DataFrame (ft1, columns=['attr_conc.max', 'attr_conc.mean', 'attr_conc.median', 'attr_conc.min', 'attr_conc.sd', 'attr_ent.max', 'attr_ent.mean', 'attr_ent.median', 'attr_ent.min', 'attr_ent.sd', 'attr_to_inst', 'cat_to_num', 'cor.max', 'cor.mean', 'cor.median', 'cor.min', 'cor.sd', 'cov.max', 'cov.mean', 'cov.median', 'cov.min', 'cov.sd', 'eigenvalues.max', 'eigenvalues.mean', 'eigenvalues.median', 'eigenvalues.min', 'eigenvalues.sd', 'g_mean.max', 'g_mean.mean', 'g_mean.median', 'g_mean.min', 'g_mean.sd', 'h_mean.max', 'h_mean.mean', 'h_mean.median', 'h_mean.min', 'h_mean.sd', 'inst_to_attr', 'iq_range.max', 'iq_range.mean', 'iq_range.median', 'iq_range.min', 'iq_range.sd', 'kurtosis.max', 'kurtosis.mean', 'kurtosis.median', 'kurtosis.min', 'kurtosis.sd', 'mad.max', 'mad.mean', 'mad.median', 'mad.min', 'mad.sd', 'max.max', 'max.mean', 'max.median', 'max.min', 'max.sd', 'mean.max', 'mean.mean', 'mean.median', 'mean.min', 'mean.sd', 'median.max', 'median.mean', 'median.median', 'median.min', 'median.sd', 'min.max', 'min.mean', 'min.median', 'min.min', 'min.sd', 'nr_attr', 'nr_bin', 'nr_cat', 'nr_cor_attr', 'nr_inst', 'nr_norm', 'nr_num', 'nr_outliers', 'num_to_cat', 'range.max', 'range.mean', 'range.median', 'range.min', 'range.sd', 'sd.max', 'sd.mean', 'sd.median', 'sd.min', 'sd.sd', 'skewness.max', 'skewness.mean', 'skewness.median', 'skewness.min', 'skewness.sd', 'sparsity.max', 'sparsity.mean', 'sparsity.median', 'sparsity.min', 'sparsity.sd', 't_mean.max', 't_mean.mean', 't_mean.median', 't_mean.min', 't_mean.sd', 'var.max', 'var.mean', 'var.median', 'var.min', 'var.sd'])  #transformando a saida do MFE em um dataframe)
                #, columns=['attr_conc.max', 'attr_conc.mean', 'attr_conc.median', 'attr_conc.min', 'attr_conc.sd', 'attr_ent.max', 'attr_ent.mean', 'attr_ent.median', 'attr_ent.min', 'attr_ent.sd', 'attr_to_inst', 'cat_to_num', 'cor.max', 'cor.mean', 'cor.median', 'cor.min', 'cor.sd', 'cov.max', 'cov.mean', 'cov.median', 'cov.min', 'cov.sd', 'eigenvalues.max', 'eigenvalues.mean', 'eigenvalues.median', 'eigenvalues.min', 'eigenvalues.sd', 'g_mean.max', 'g_mean.mean', 'g_mean.median', 'g_mean.min', 'g_mean.sd', 'h_mean.max', 'h_mean.mean', 'h_mean.median', 'h_mean.min', 'h_mean.sd', 'inst_to_attr', 'iq_range.max', 'iq_range.mean', 'iq_range.median', 'iq_range.min', 'iq_range.sd', 'kurtosis.max', 'kurtosis.mean', 'kurtosis.median', 'kurtosis.min', 'kurtosis.sd', 'mad.max', 'mad.mean', 'mad.median', 'mad.min', 'mad.sd', 'max.max', 'max.mean', 'max.median', 'max.min', 'max.sd', 'mean.max', 'mean.mean', 'mean.median', 'mean.min', 'mean.sd', 'median.max', 'median.mean', 'median.median', 'median.min', 'median.sd', 'min.max', 'min.mean', 'min.median', 'min.min', 'min.sd', 'nr_attr', 'nr_bin', 'nr_cat', 'nr_cor_attr', 'nr_inst', 'nr_norm', 'nr_num', 'nr_outliers', 'num_to_cat', 'range.max', 'range.mean', 'range.median', 'range.min', 'range.sd', 'sd.max', 'sd.mean', 'sd.median', 'sd.min', 'sd.sd', 'skewness.max', 'skewness.mean', 'skewness.median', 'skewness.min', 'skewness.sd', 'sparsity.max', 'sparsity.mean', 'sparsity.median', 'sparsity.min', 'sparsity.sd', 't_mean.max', 't_mean.mean', 't_mean.median', 't_mean.min', 't_mean.sd', 'var.max', 'var.mean', 'var.median', 'var.min', 'var.sd'])
                reducformat=df_ft_reduce.drop(index = 0)
                reducformat['id_experimento'] = idexp
                reducformat['reducao'] = reduce
                salvarResultados(reducformat) 
               
                listreducformat.append(reducformat)
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
        urlreduc = urlsaida
        salvarDf_R = salvarDf_Reduc(listreducformat,nome, name_file)
        salvarExperimentos(idexp, nomef, file, nvezes_, nreduce, salvarDf_O, salvarDf_R)
   
    #id_original, id_resultados)

    context = {'documents': documents, 'form': form, 'list_df_ft': list_df_ft, 'list_df_red': list_reduce, 'list': listo,
               'nreduc': nreduce, 'nfiles': nfiles , 'nvezes': nvezes , 'nome': nome}
    build_list.retorno = context
    return build_list

