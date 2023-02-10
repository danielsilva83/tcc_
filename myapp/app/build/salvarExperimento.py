import sqlite3

from myapp.models import Experimento


def salvarExperimentos(idexp, nome, arquivo, numero_repeticoes, tamanhos_reducao, salvarDf_O, salvarDf_R):
    
    conn = sqlite3.connect('db.sqlite3')
    experimentos = Experimento(idexp, nome, arquivo, numero_repeticoes, tamanhos_reducao, salvarDf_O, salvarDf_R)

    experimentos.save()

    conn.close()