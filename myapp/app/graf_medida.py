from django.shortcuts import render
from myapp.app.list_process_id import list_process_id


def graf_medida(request):
    def split_text(obj, substring = None, start = 0, qtd = 13):
      qtd = len(obj) if qtd is None else qtd

      if substring:
        inicio = obj.find(substring)
        return obj[inicio:inicio+qtd]
      elif not substring:
        return obj[start:start+qtd]
    formi = request.POST.get('medid')
    forma = split_text (formi, substring = "'", start = 0, qtd = 13)
    form1 = formi.split(" ")
   
    nomemedida = str(form1[1])
   
    id_experimento  = int(split_text(formi,qtd=2))
    rtam=[] 
    list_process_id(request, id_experimento)
    experimento = list_process_id.experimento
    medidas = list_process_id.medidas
    origin =  list_process_id.original
    origins =  list_process_id.originals
    result = list_process_id.resultados
    rtam = list_process_id.resultado
    
    #pegar nomemedida e procurar medidas igual
    originn =dict()
    originn['medida']=origins[nomemedida] 
    originn['tamanhoReducao']=0
   
   
    
    
    tam =  dict()
    taman=[]
    tamann=[]
    for i in rtam:
        tam= (i[-1])
        #taman.append('tamanhoReducao')
        taman.append(tam*100 )

    resultadd = [] 

    c=0
    resulta = dict()

    tama= dict()
    tamanhored =dict()
   
    for i in result:
        strmed = "{medida: "
        resulta=str ((i[nomemedida]))
        resultadd.append(strmed+resulta)
        t = str (taman[c])
        strmtam = "tamanhoReducao: "
        resultadd.append(strmtam+t+"}")
        c=c+1
    cc=0

    for i in result:
        if (cc==0):
            resultadd.append(originn)
        #print(resultadd  )
        cc=cc+1

    fin = (resultadd  )
    print(resultadd)
    context = {'experimento': experimento, 'origin': origin, 'medida' : medidas, 'result': result, 'nomemedida': nomemedida, 'origins': origins, 'dados': fin}
    return render(request,'medidas.html', context)