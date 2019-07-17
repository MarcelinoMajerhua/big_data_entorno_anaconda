import cx_Oracle as cx
import numpy as np
import matplotlib.pyplot as plt
from coneccion import Herramienta
import math as mt
conectar=Herramienta()
import pandas as  pd
host="localhost"
user="ADMINDATO"
password="root"
tsname="orcl"
conexion = cx.connect(user, password,host+"/"+tsname)
consultaNota =pd.read_sql_query('select ca.NOTA_1, co.NOMBRE_COLEGIO from calificacion ca inner join colegio co on ca.id_alumno = co.id_alumno',conexion)
nota=consultaNota['NOTA_1']
#values=consultaNota['NOMBRE_COLEGIO']
#fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
#axs[0].bar(names, values)
h = plt.hist(nota)
#axs[1].scatter(names, values)
#axs[2].plot(names, values)
#fig.suptitle('Categorical Plotting')
