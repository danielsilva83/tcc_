
import glob

import os
import numpy as np

import pandas as pd
from django.shortcuts import render
from myapp.models import  Experimento




def seek_file_original(all_files_original, file_seek):
    for file_original in all_files_original:
        path_original = os.path.basename(file_original).split('.')
        path_file_seek = os.path.basename(file_seek).split('.')
        if path_original[0] == path_file_seek[0]:
            original_file = file_original
            return original_file




def analise_experimento_reducao_geral(request,nome):
    list_medidas_variantes_head = []
    list_medidas_constantes_head = []
    list_medidas_variantes_tail = []
    list_medidas_constantes_tail = []
    list_medidas_variantes_head_ =  pd.DataFrame()
    list_medidas_constantes_head_ =  pd.DataFrame()
    list_medidas_variantes_tail_ =  pd.DataFrame()
    list_medidas_constantes_tail_ =  pd.DataFrame()
    nome = str(nome)

    experimentos = Experimento.objects.filter(nome=nome).values()
    list_medidas_variantes_head.clear(),list_medidas_constantes_head.clear() 
    list_medidas_variantes_tail.clear(),list_medidas_constantes_tail.clear() 
    for experimento  in experimentos:

          
        data_orig = experimento['salvarDf_O']
    
        data_orig = data_orig.split('../../')
    
     
        
        data_reduc = experimento['salvarDf_R']
    
        data_reduc = data_reduc.split('../../')

        # pegando os paths onde estao os arquivos
        data_list = data_reduc[1] #os.path.join(data_path,data_reduc)
        print(data_list)
        #print(data_orig[0]['salvarDf_O'])                
        #os.path.join(data_path, 'resultados','resultados tcc')
        data_list_original = data_orig[1] #os.path.join(data_path,data_orig)

        #listando os arquivos
        all_files_resultado = glob.glob(data_list)

        all_files_original = glob.glob(data_list_original)
       
        df_union_df = pd.DataFrame()
        lista_med_constantes_head = ""
        lista_med_constantes_tail = ""
        lista_med_variaram_head = ""
        lista_med_variaram_tail = ""
        #iterando sobre todos os resultados
        for file_  in all_files_resultado:
            #encontrando arquivos originais relativos aos arquivos de resultado
            file_original = seek_file_original(all_files_original,file_)
            
             #lendo resultados
            df = pd.read_csv(file_, sep = '\t')
            #limpando resultados
            df = df.drop(['Unnamed: 0', 'id_experimento'], axis=1)
            #tirando a media das medidas de todas as repeticoes
            df.loc['0'] = df.mean()
            #tirando o desvios padrao da medias de todas as repeticoes
           
            #criando daframe com as medias das medidas
            df_media = pd.DataFrame(df.loc['0'])
           
            #transpondo o dataframe
            df_media = df_media.T
         
           
            df =    df.drop(['0'], axis=0)
            
            df1_ = df.groupby(by=['reducao'],as_index=False ).mean()
            df2_ = df.groupby(by=['reducao'],as_index=False ).std()
            df1 = pd.DataFrame(df1_)
            df2 = pd.DataFrame(df2_)
            #print(df1)
            df_reduc = pd.DataFrame(df1_)
            df_reduc = df_reduc.values.tolist()
            
            #lendo medidas originais
            df_original = pd.read_csv(file_original, sep = '\t')
            #limpando originais
            df_original = df_original.drop(['id'], axis=1)
            df_original = df_original.drop(['Unnamed: 0'], axis=1)
        
            
            #lista de medidas
            medidas=['attr_conc.max', 'attr_conc.mean', 'attr_conc.median', 'attr_conc.min', 'attr_conc.sd', 'attr_ent.max', 'attr_ent.mean', 'attr_ent.median', 'attr_ent.min', 'attr_ent.sd', 'attr_to_inst', 'cat_to_num', 'cor.max', 'cor.mean', 'cor.median', 'cor.min', 'cor.sd', 'cov.max', 'cov.mean', 'cov.median', 'cov.min', 'cov.sd', 'eigenvalues.max', 'eigenvalues.mean', 'eigenvalues.median', 'eigenvalues.min', 'eigenvalues.sd', 'g_mean.max', 'g_mean.mean', 'g_mean.median', 'g_mean.min', 'g_mean.sd', 'h_mean.max', 'h_mean.mean', 'h_mean.median', 'h_mean.min', 'h_mean.sd', 'inst_to_attr', 'iq_range.max', 'iq_range.mean', 'iq_range.median', 'iq_range.min', 'iq_range.sd', 'kurtosis.max', 'kurtosis.mean', 'kurtosis.median', 'kurtosis.min', 'kurtosis.sd', 'mad.max', 'mad.mean', 'mad.median', 'mad.min', 'mad.sd', 'max.max', 'max.mean', 'max.median', 'max.min', 'max.sd', 'mean.max', 'mean.mean', 'mean.median', 'mean.min', 'mean.sd', 'median.max', 'median.mean', 'median.median', 'median.min', 'median.sd', 'min.max', 'min.mean', 'min.median', 'min.min', 'min.sd', 'nr_attr', 'nr_bin', 'nr_cat', 'nr_cor_attr', 'nr_inst', 'nr_norm', 'nr_num', 'nr_outliers', 'num_to_cat', 'range.max', 'range.mean', 'range.median', 'range.min', 'range.sd', 'sd.max', 'sd.mean', 'sd.median', 'sd.min', 'sd.sd', 'skewness.max', 'skewness.mean', 'skewness.median', 'skewness.min', 'skewness.sd', 'sparsity.max', 'sparsity.mean', 'sparsity.median', 'sparsity.min', 'sparsity.sd', 't_mean.max', 't_mean.mean', 't_mean.median', 't_mean.min', 't_mean.sd', 'var.max', 'var.mean', 'var.median', 'var.min', 'var.sd']
            # pegando nome do arquivo original
            namefile = os.path.basename(file_original).split('.')[0]
            # criando dataframe com as medidas constantes
            lista_med_constantes = pd.DataFrame(columns = ['medida','valor_da_medida','reducao'])
            # criando dataframe com as medidas variantes
            lista_med_variaram = pd.DataFrame(columns = ['reducao_em_%','medida','média_medida','std_medida','cv_medida_em_%'])
            
        
            #iterando as medidas para comparar o valor da medida do resultado com a medida do original
            lin = 0
            for medida in medidas:
                ii=0
                for nreducao in df_reduc:
                
                    #caso medida do resultado igual a medida do original, signigica que a medida se manteve constante
                    if df_media[medida].values == df_original[medida].values:
                        #adicionando medida no dataframe de medidas constantes
                        lista_med_constantes.loc[lin] = df_original[medida].name, df_original[medida][0], nreducao[0]
                    #caso medida do resultado seja diferente da medida do original, signigica que a medida teve variacao
                    if df_media[medida].values != df_original[medida].values:
                        #adicionando medida no dataframe de medidas variantes
                    
                        mean = df1[medida][0]
                  
                        mean = round(mean, 1)
                        
                        std= df2[medida][0]
                      
                        std = round(std, 1)
                      
                        cv_medida = (mean/std)
                  
                        cv_medida = round(cv_medida, 1)
                        lista_med_variaram.loc[lin] = nreducao[0]*100,df1[medida].name, mean, std,\
                        cv_medida
                    ii=ii+1
                    #contador de linhas para o dataframe
                    lin = lin + 1
            #gera rank medidas variantes por desvio padrao rank_std  e tamanho de reducao
            #lista_med_variaram['rank_std'] = lista_med_variaram['cv_medida'].rank()
            #organiza medidas contastantes por valor da medida
            #lista_med_constantes = lista_med_constantes.sort_values(by='valor_da_medida',ascending=False)
            #elimina os NANs da medidas variantes
            lista_med_variaram = lista_med_variaram.dropna()
            #organiza medidas variantes por rank de desvio padrao
            lista_med_variaram = lista_med_variaram.sort_values(by='medida',ascending=False)
            
            #adiciona lista de medidas variantes pir 

            lista_med_variaram = lista_med_variaram.reset_index(drop=True)
            #####################
            #df_union_variaram_head = pd.concat([df_union_variaram_head, lista_med_variaram], ignore_index=True)
            lista_med_variaram_head = lista_med_variaram
            lista_med_variaram_tail = lista_med_variaram
            
            
            #organiza lista de medidas constantes por valor da medida 
            lista_med_constantes = lista_med_constantes.sort_values(by='medida',ascending=False)
            lista_med_constantes = lista_med_constantes.reset_index(drop=True)
            #####################
            #df_union_df = pd.concat([df_union_df, lista_med_variaram], ignore_index=True)
            lista_med_constantes_head = lista_med_constantes
        
            lista_med_constantes_tail = lista_med_constantes

            #Cria lista com as medidas constantes por dataset
        list_medidas_constantes_head.append(lista_med_constantes_head)
        list_medidas_variantes_head.append(lista_med_variaram_head)
        list_medidas_constantes_tail.append(lista_med_constantes_tail)
        list_medidas_variantes_tail.append(lista_med_variaram_tail)


       
    for constantes_head  in list_medidas_constantes_head:
        #list_medidas_constantes_head_ = pd.concat([list_medidas_constantes_head_, constantes_head], ignore_index=True)
        list_medidas_constantes_head_ = list_medidas_constantes_head_.append(constantes_head, ignore_index=True)
    list_medidas_constantes_head_['mean'] = list_medidas_constantes_head_.mean(axis=1)
    list_medidas_constantes_head_['std'] = list_medidas_constantes_head_.std(axis=1)
    list_medidas_constantes_head_['cv_geral'] = list_medidas_constantes_head_['mean']/ list_medidas_constantes_head_['std'].round(2)

  
    list_medidas_constantes_head_['rank_cv_geral'] = list_medidas_constantes_head_['cv_geral'].rank()
    list_medidas_constantes_head_ = list_medidas_constantes_head_.sort_values(by='medida',ascending=False)
   
    list_medidas_constantes_head_ = list_medidas_constantes_head_.head(100).to_html()
   
    for variantes_head  in list_medidas_variantes_head:
        #list_medidas_variantes_head_ = pd.concat([list_medidas_variantes_head_, variantes_head])
        list_medidas_variantes_head_ = list_medidas_variantes_head_.append(variantes_head, ignore_index=False)
    list_medidas_variantes_head_ = list_medidas_variantes_head_.groupby(by=['medida','reducao_em_%'],sort=False,as_index=False ).sum()
    #print(list_medidas_variantes_head_)
    list_medidas_variantes_head_['mean'] = list_medidas_variantes_head_.mean(axis=1).round(2)
    list_medidas_variantes_head_['std'] = list_medidas_variantes_head_.std(axis=1).round(2)
    list_medidas_variantes_head_['cv_geral'] = (list_medidas_variantes_head_['mean']/ list_medidas_variantes_head_['std'] ).round(2)
    list_medidas_variantes_head_['cv_geral'] = list_medidas_variantes_head_['cv_geral'].apply(lambda x: '{:,.2f}'.format(x))
    list_medidas_variantes_head_=list_medidas_variantes_head_.drop(['média_medida','std_medida',	'cv_medida_em_%'], axis=1)
    list_medidas_variantes_head_['rank_cv_geral'] = list_medidas_variantes_head_['cv_geral'].rank()
    list_medidas_variantes_head_ = list_medidas_variantes_head_.dropna(axis=0,subset=['std'])
    list_medidas_variantes_head_ = list_medidas_variantes_head_.sort_values(by=['rank_cv_geral','medida'],ascending=True)
    list_medidas_variantes_head_ = list_medidas_variantes_head_.to_html()

    for variantes_tail  in list_medidas_variantes_tail:
        #list_medidas_variantes_tail_ = pd.concat([list_medidas_variantes_tail_, variantes_tail])
        list_medidas_variantes_tail_ = list_medidas_variantes_tail_.append(variantes_tail, ignore_index=False)
    list_medidas_variantes_tail_ = list_medidas_variantes_tail_.groupby(by=['medida','reducao_em_%'],sort=False,as_index=False ).sum()
    list_medidas_variantes_tail_['mean'] = list_medidas_variantes_tail_.mean(axis=1).round(2)
    list_medidas_variantes_tail_['std'] = list_medidas_variantes_tail_.std(axis=1).round(2)
    list_medidas_variantes_tail_['cv_geral'] = (list_medidas_variantes_tail_['mean']/ list_medidas_variantes_tail_['std']).round(2)
    list_medidas_variantes_tail_=list_medidas_variantes_tail_.drop(['média_medida','std_medida',	'cv_medida_em_%'], axis=1)
    list_medidas_variantes_tail_['rank_cv_geral'] = list_medidas_variantes_tail_['cv_geral'].rank()
    list_medidas_variantes_tail_ = list_medidas_variantes_tail_.dropna(axis=0,subset=['std'])
    list_medidas_variantes_tail_ = list_medidas_variantes_tail_.sort_values(by=['rank_cv_geral'],ascending=True)
    
 
    list_medidas_variantes_tail_ = list_medidas_variantes_tail_.to_html()
        
    
    list_medidas_variantes_head.clear(),list_medidas_constantes_head.clear() 
    list_medidas_variantes_tail.clear(),list_medidas_constantes_tail.clear() 

    list_medidas_constantes_head.append(list_medidas_constantes_head_)
    list_medidas_variantes_head.append(list_medidas_variantes_head_)
    list_medidas_constantes_tail.append(list_medidas_variantes_tail_)
    list_medidas_variantes_tail.append(list_medidas_variantes_tail_)
        
    #list_medidas_constantes = [entry for entry in list_medidas_constantes]
    #list_medidas_variantes = [entry for entry in list_medidas_variantes]
        

   
    context = {'list_medidas_variantes_head': list_medidas_variantes_head, 
               'list_medidas_constantes_head': list_medidas_constantes_head,
               'list_medidas_variantes_tail': list_medidas_variantes_tail, 
               'list_medidas_constantes_tail': list_medidas_constantes_tail}
    
   
    
    return  render(request,'analiselistreducaogeral.html',context)

