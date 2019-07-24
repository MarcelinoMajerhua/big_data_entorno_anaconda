
import matplotlib.pyplot as plt
import numpy as np
import cx_Oracle
import random

valores = [[1,2], [3,4]]
etiquetas_fil = ('x', 'y')
etiquetas_col = (u'Máximo', u'Mínimo')

plt.table(cellText=valores, rowLabels=etiquetas_fil,colLabels = etiquetas_col, colWidths = [0.3],loc='upper center')