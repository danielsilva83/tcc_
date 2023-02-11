import sqlite3

from django.shortcuts import render
from myapp.models import Document, Experimento


def list_process_id(request, id):
    id = str(id)
    id_experimento = id

    documents = Document.objects.all()
    experimento = Experimento.objects.filter(id=id).values()
    #medidasx = {'cor.max', 'cor.mean', 'cor.median', 'cor.min', 'cor.sd', 'cov.max', 'cov.mean', 'cov.median', 'cov.min', 'cov.sd', 'eigenvalues.max', 'eigenvalues.mean', 'eigenvalues.median', 'eigenvalues.min', 'eigenvalues.sd', 'g_mean.max', 'g_mean.mean', 'g_mean.median', 'g_mean.min', 'g_mean.sd', 'h_mean.max', 'h_mean.mean', 'h_mean.median', 'h_mean.min', 'h_mean.sd', 'iq_range.max', 'iq_range.mean', 'iq_range.median', 'iq_range.min', 'iq_range.sd', 'kurtosis.max', 'kurtosis.mean', 'kurtosis.median', 'kurtosis.min', 'kurtosis.sd', 'mad.max', 'mad.mean', 'mad.median', 'mad.min', 'mad.sd', 'max.max', 'max.mean', 'max.median', 'max.min', 'max.sd', 'mean.max', 'mean.mean', 'mean.median', 'mean.min', 'mean.sd', 'median.max', 'median.mean', 'median.median', 'median.min', 'median.sd', 'min.max', 'min.mean', 'min.median', 'min.min', 'min.sd', 'nr_cor_attr', 'nr_norm', 'nr_outliers', 'range.max', 'range.mean', 'range.median', 'range.min', 'range.sd', 'sd.max', 'sd.mean', 'sd.median', 'sd.min', 'sd.sd', 'skewness.max', 'skewness.mean', 'skewness.median', 'skewness.min', 'skewness.sd', 'sparsity.max', 'sparsity.mean', 'sparsity.median', 'sparsity.min', 'sparsity.sd', 't_mean.max', 't_mean.mean', 't_mean.median', 't_mean.min', 't_mean.sd', 'var.max', 'var.mean', 'var.median', 'var.min', 'var.sd'}
    #, columns=['attr_conc.max', 'attr_conc.mean', 'attr_conc.median', 'attr_conc.min', 'attr_conc.sd', 'attr_ent.max', 'attr_ent.mean', 'attr_ent.median', 'attr_ent.min', 'attr_ent.sd', 'attr_to_inst', 'cat_to_num', 'cor.max', 'cor.mean', 'cor.median', 'cor.min', 'cor.sd', 'cov.max', 'cov.mean', 'cov.median', 'cov.min', 'cov.sd', 'eigenvalues.max', 'eigenvalues.mean', 'eigenvalues.median', 'eigenvalues.min', 'eigenvalues.sd', 'g_mean.max', 'g_mean.mean', 'g_mean.median', 'g_mean.min', 'g_mean.sd', 'h_mean.max', 'h_mean.mean', 'h_mean.median', 'h_mean.min', 'h_mean.sd', 'inst_to_attr', 'iq_range.max', 'iq_range.mean', 'iq_range.median', 'iq_range.min', 'iq_range.sd', 'kurtosis.max', 'kurtosis.mean', 'kurtosis.median', 'kurtosis.min', 'kurtosis.sd', 'mad.max', 'mad.mean', 'mad.median', 'mad.min', 'mad.sd', 'max.max', 'max.mean', 'max.median', 'max.min', 'max.sd', 'mean.max', 'mean.mean', 'mean.median', 'mean.min', 'mean.sd', 'median.max', 'median.mean', 'median.median', 'median.min', 'median.sd', 'min.max', 'min.mean', 'min.median', 'min.min', 'min.sd', 'nr_attr', 'nr_bin', 'nr_cat', 'nr_cor_attr', 'nr_inst', 'nr_norm', 'nr_num', 'nr_outliers', 'num_to_cat', 'range.max', 'range.mean', 'range.median', 'range.min', 'range.sd', 'sd.max', 'sd.mean', 'sd.median', 'sd.min', 'sd.sd', 'skewness.max', 'skewness.mean', 'skewness.median', 'skewness.min', 'skewness.sd', 'sparsity.max', 'sparsity.mean', 'sparsity.median', 'sparsity.min', 'sparsity.sd', 't_mean.max', 't_mean.mean', 't_mean.median', 't_mean.min', 't_mean.sd', 'var.max', 'var.mean', 'var.median', 'var.min', 'var.sd','tamanhoReducao']
    medidas = ['attr_conc.max', 'attr_conc.mean', 'attr_conc.median', 'attr_conc.min', 'attr_conc.sd', \
            'attr_ent.max', 'attr_ent.mean', 'attr_ent.median', 'attr_ent.min', 'attr_ent.sd', \
            'attr_to_inst', 'cat_to_num', 'cor.max', 'cor.mean', 'cor.median', 'cor.min', 'cor.sd', \
            'cov.max', 'cov.mean', 'cov.median', 'cov.min', 'cov.sd', 'eigenvalues.max', \
            'eigenvalues.mean', 'eigenvalues.median', 'eigenvalues.min', 'eigenvalues.sd', \
            'g_mean.max', 'g_mean.mean', 'g_mean.median', 'g_mean.min', 'g_mean.sd', 'h_mean.max', \
            'h_mean.mean', 'h_mean.median', 'h_mean.min', 'h_mean.sd', 'inst_to_attr', 'iq_range.max', \
            'iq_range.mean', 'iq_range.median', 'iq_range.min', 'iq_range.sd', 'kurtosis.max',\
            'kurtosis.mean', 'kurtosis.median', 'kurtosis.min', 'kurtosis.sd', 'mad.max', 'mad.mean', \
            'mad.median', 'mad.min', 'mad.sd', 'max.max', 'max.mean', 'max.median', 'max.min',\
            'max.sd', 'mean.max', 'mean.mean', 'mean.median', 'mean.min', 'mean.sd', \
            'median.max', 'median.mean', 'median.median', 'median.min', 'median.sd', 'min.max',\
            'min.mean', 'min.median', 'min.min', 'min.sd', 'nr_attr', 'nr_bin', 'nr_cat', \
            'nr_cor_attr', 'nr_inst', 'nr_norm', 'nr_num', 'nr_outliers', 'num_to_cat', 'range.max',\
            'range.mean', 'range.median', 'range.min', 'range.sd', 'sd.max', 'sd.mean', \
            'sd.median', 'sd.min', 'sd.sd', 'skewness.max', 'skewness.mean', 'skewness.median', \
            'skewness.min', 'skewness.sd', 'sparsity.max', 'sparsity.mean', 'sparsity.median', \
            'sparsity.min', 'sparsity.sd', 't_mean.max', 't_mean.mean', 't_mean.median', 't_mean.min',\
            't_mean.sd', 'var.max', 'var.mean', 'var.median', 'var.min', 'var.sd','tamanhoReducao']
    originals =  sqlite3.connect('db.sqlite3').execute('select * from original where id=?',[id]).fetchall()
    originals = [list(i) for i in originals]
    original = []
    for i in originals:
        for j in i: 
            original.append(j)
  
    originals = dict(zip(medidas, original))
    #res = [i for j in map(None, original, medidas)   
    #                   for i in j if i is not None]
    resultadosx =  sqlite3.connect('db.sqlite3').execute('select * from resultados where id_experimento = ?',  [id_experimento]).fetchall()
    resultados = [list(i) for i in resultadosx]
    resultado = []
    resultado1 = []
    for i in resultados:
    
            resultado.append(i)
   
    for i in resultados:
        resultado1.append(dict(zip(medidas, i)) )
    
    context = {'context': experimento, 'original': originals, 'resultados': resultados, 'doc': documents}
    list_process_id.resultados = resultado1
    list_process_id.resultado = resultado
    list_process_id.context = context
    list_process_id.medidas = medidas
    list_process_id.original = original
    list_process_id.originals = originals
    list_process_id.experimento = experimento
    return render(request,'listexperimento.html', context)