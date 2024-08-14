from datetime import datetime
import pyodbc

hoje = datetime.now()
dados_conexao = ("driver=;""server=;""user=;""database=;""password=;")
cnx = pyodbc.connect(dados_conexao)
cursor = cnx.cursor()

insert = f"comando insert SQL"
cursor.execute(insert)
cursor.commit()

select = f"comando select SQL"
cursor.execute(insert)
retorno_select = cursor.fetchall()
print(retorno_select)