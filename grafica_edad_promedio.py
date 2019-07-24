import matplotlib.pyplot as plt
import numpy as np
from coneccion import Coneccion as  cx
import pandas as pd
from Herramienta import Herramienta
conexion = cx.coneccionBD(cx)
consulta =pd.read_sql_query('''SELECT (AL.EDADALUMNO)EDAD_ALUMNO, ROUND(AVG(CA.NOTA_1),2)PROMEDIO_1,ROUND(AVG(CA.NOTA_2),2)PROMEDIO_2,ROUND(AVG(CA.NOTA_3),2)PROMEDIO_3,ROUND(AVG(CA.NOTA_4),2)PROMEDIO_4
FROM ALUMNO AL INNER JOIN CALIFICACION CA
ON AL.IDCALIFICACION = CA.IDCALIFICACION
GROUP BY AL.EDADALUMNO
ORDER BY AL.EDADALUMNO ASC
''',conexion)

Herramienta.graficarEdadPromedio(Herramienta,consulta,'GRAFICO EDAD VS PROMEDIO NOTAS')