import sqlite3


def salvarResultados(dataframeResultados):
   
    conn = sqlite3.connect('db.sqlite3')
    dataframeResultados.to_sql('resultados', conn, if_exists = 'append', index=True)
    conn.close()