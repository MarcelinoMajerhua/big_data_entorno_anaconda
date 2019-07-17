# big_data_entorno_anaconda
consulta =pd.read_sql_query('select ID_ALUMNO, PROCEDENCIA_ALUMNO  from alumno',conexion)
si ponemos consulta.shape nos devuelve el tamaño de la matriz
------------------------------------------------------------
es como ponerle un alias
d={'FORANEO':'F','LOCAL':'L'}
consulta['PROCEDENCIA_ALUMNO']=consulta['PROCEDENCIA_ALUMNO'].apply(lambda x:d[x])
----------------------------------------------------------------------
mustra los indicadores estadisitcos ccomo la media 
print(consulta.describe())