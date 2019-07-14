import cx_Oracle as cx
import pandas as  pd
host="localhost"
user="ADMINDATO"
password="root"
tsname="orcl"
conexion = cx.connect(user, password,host+"/"+tsname)
consulta =pd.read_sql_query('select ID_ALUMNO, PROCEDENCIA_ALUMNO  from alumno',conexion)
print(consulta.count)