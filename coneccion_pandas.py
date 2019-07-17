import cx_Oracle as cx
#import numpy as np
#import pylab as pl
from matplotlib import pyplot as plt
import coneccion as cn
import pandas as  pd
host="localhost"
user="ADMINDATO"
password="root"
tsname="orcl"
conexion = cx.connect(user, password,host+"/"+tsname)
consultaNota =pd.read_sql_query('select IDCOLEGIO,NOMBRECOLEGIO,TIPOCOLEGIO from ADMINDATO.COLEGIO',conexion)
f=consultaNota.shape[0]
c=consultaNota.shape[1]
print(consultaNota['IDCOLEGIO'])
#nombre_colegio=consultaNota['COLEGIO']
#promedio_notas_1=consultaNota['PROMEDIO1']
#promedio_notas_2=consultaNota['PROMEDIO2']
#promedio_notas_3=consultaNota['PROMEDIO3']
#promedio_notas_4=consultaNota['PROMEDIO4']

#promedio_general=(promedio_notas_1+promedio_notas_2+promedio_notas_3+promedio_notas_4)/4
#print(promedio_general)


#X = nombre_colegio
#Y = promedio_notas_2
#plt.plot(X,Y)
#plt.show()



#matriz=cn.Herramienta.comvertirNotasString(cn,f,c,consultaNota)
#print(matriz.describe())

#print(consulta.shape)S
#print(consulta.count)
#d={'FORANEO':'F','LOCAL':'L'}
#consulta['PROCEDENCIA_ALUMNO']=consulta['NOTA_1'].apply(lambda x:d[x])
#consulta['PROCEDENCIA_ALUMNO'].head()
#print(consulta['PROCEDENCIA_ALUMNO'])
#-----------------MATRIZ--------------------
#N=consulta.shape[1]
#def crearLista(N):
#    L = [ ]
#   for i in range(N):
#        L.append(consulta['NOTA_'+str(i+1)][i])
#    return L
#print(crearLista(N))