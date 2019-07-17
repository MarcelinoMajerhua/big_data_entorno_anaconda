import cx_Oracle as cx
import numpy as np
from coneccion import Herramienta
import math as mt
conectar=Herramienta()
import pandas as  pd
host="localhost"
user="ADMINDATO"
password="root"
tsname="orcl"
conexion = cx.connect(user, password,host+"/"+tsname)
consultaNota =pd.read_sql_query('select NOTA_1,NOTA_2,NOTA_3,NOTA_4 FROM CALIFICACION ',conexion)




#print(conectar.comvertirNotasString(consulta.shape[0],consulta.shape[1],consulta))
        