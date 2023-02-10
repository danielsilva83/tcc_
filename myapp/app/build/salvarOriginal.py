
import sqlite3


def salvarOriginal(dataframeOriginal):
   
    conn = sqlite3.connect('db.sqlite3')
    dataframeOriginal.to_sql('original', conn, if_exists='append', index = True) #replace #append
    conn.close()