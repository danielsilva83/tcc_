import pandas as pd


def salvarDf_Reduc (dataframeReduzido, file_name, name_file):
    name_file = name_file.replace("/", "_")
    name_file = name_file.replace("media", "")
    name_file = name_file.replace("documents", "")
    file_name_= '../../exports/'+file_name+name_file+'_reduzido_'+'.csv'
    file_name_1= 'exports/'+file_name+name_file+'_reduzido_'+'.csv'
    print(file_name_)
    
    dataexport1 = pd.DataFrame()
    for dataframeReduz in dataframeReduzido:
        dataexport1 = pd.concat([dataexport1,dataframeReduz])
        dataexport = pd.DataFrame(dataexport1)
    dataexport.to_csv(file_name_1, sep='\t')
    
    return file_name_