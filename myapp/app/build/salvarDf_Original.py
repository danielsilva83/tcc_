def salvarDf_Original (dataframeOriginal,file_name, name_file ):
    
    name_file = name_file.replace("/", "_")
    name_file = name_file.replace("media", "")
    name_file = name_file.replace("documents", "")
    file_name_ = '../../media/documents/exports/'+name_file+'_original_'+'.csv'
    file_name_1 = 'media/documents/exports/'+name_file+'_original_'+'.csv'
    #print(file_name_+'_original_'+'.csv')
    dataframeOriginal.to_csv(file_name_1, sep='\t')
    return file_name_