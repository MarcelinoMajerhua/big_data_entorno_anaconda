import matplotlib.pyplot as plt
import numpy as np
from coneccion import Coneccion as  cx
import pandas as pd
from Herramienta import Herramienta
conexion = cx.coneccionBD(cx)
consulta =pd.read_sql_query('''SELECT (CO.IDCOLEGIO)IDCOLEGIO, ROUND(AVG(CA.NOTA_1),2)NOTA_1,ROUND(AVG(CA.NOTA_2),2)NOTA_2,
ROUND(AVG(CA.NOTA_3),2)NOTA_3,ROUND(AVG(CA.NOTA_4),2)NOTA_4
FROM CALIFICACION CA INNER JOIN ALUMNO AL
ON CA.IDCALIFICACION = AL.IDCALIFICACION INNER JOIN COLEGIO CO
ON AL.IDCOLEGIO = CO.IDCOLEGIO
GROUP BY CO.IDCOLEGIO''',conexion)
Herramienta.graficarFuncionLinea(Herramienta,consulta)