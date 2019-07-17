import cx_Oracle
class Herramienta:
    def comvertirNotasString(self,numeroFila,numeroColumna,consulta):
        matriz = [None] * numeroFila
        for i in range(numeroFila):
            matriz[i] = [i] * numeroColumna
        for i in range(numeroFila):
            for j in range(numeroColumna):
                matriz[i][j] = consulta['NOTA_'+str(j+1)][i]
        

        for i in range(numeroFila):
            for j in range(numeroColumna):
                if matriz[i][j] < 10.5:
                    matriz[i][j] = 'DESAPROBADO'
                else:
                    matriz[i][j] = 'APROBADO'
        return matriz
# if __name__=="__main__":
    #nexo = conect()
    #for fila in nexo.sentenciaCompuesta("select ID_ALUMNO, PROCEDENCIA_ALUMNO  from alumno"):
        #print(fila)
