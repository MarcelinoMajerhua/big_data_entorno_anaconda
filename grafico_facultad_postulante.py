from matplotlib import pyplot
from Herramienta import Herramienta
from coneccion import Coneccion as cx
import pandas as pd
conexion = cx.coneccionBD(cx)
consulta =pd.read_sql_query('''SELECT (FA.NOMBREFACULTAD)NOMBRE_FACULTAD, (COUNT(AL.IDALUMNO))NUMERO_ALUMNO
FROM FACULTAD FA INNER JOIN ALUMNO AL 
ON FA.IDFACULTAD = AL.IDFACULTAD
GROUP BY FA.NOMBREFACULTAD''',conexion)
Herramienta.graficarQueso(Herramienta,consulta,'NUMERO ALUMNO POR FACULTAD')
