from coneccion import Coneccion as cx
import numpy as np
import matplotlib.pyplot as plt
import math as mt
import pandas as  pd
conexion=cx.coneccionBD(cx)
consultaNota =pd.read_sql_query('select NOTA_1,NOTA_2,NOTA_3,NOTA_4 from ADMINDATO.CALIFICACION',conexion)
print(((consultaNota.describe())['NOTA_1'])[1])

nota1=consultaNota['NOTA_1']
nota2=consultaNota['NOTA_2']
nota3=consultaNota['NOTA_3']
nota4=consultaNota['NOTA_4']

#consultaNota =pd.read_sql_query('select IDCOLEGIO,NOMBRECOLEGIO from ADMINDATO.COLEGIO',conexion)
#print(consultaNota)