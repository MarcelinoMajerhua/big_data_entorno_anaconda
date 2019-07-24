
from coneccion import Coneccion as  cx
from Herramienta import Herramienta as hr
import pandas as pd
conexion = cx.coneccionBD(cx)
consulta =pd.read_sql_query('''select NOTA_1,NOTA_2,NOTA_3,NOTA_4 from ADMINDATO.CALIFICACION''',conexion)
hr.graficarFuncionBoxes(hr,consulta,'PROMEDIO_NOTAS')





