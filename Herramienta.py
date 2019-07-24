import matplotlib.pyplot as plt
import numpy as np
import cx_Oracle
import random
class Herramienta:
    
    def graficarFuncionLinea(self,consulta):
        listaColores=['y','m','c','g','b']
        tipoTraso=[ '-', '-.', '--', '-.', '--']
        for i in range (1,5):
            plt.subplot(2,2,i)
            plt.stem(consulta['NOTA_'+str(i)], consulta['IDCOLEGIO'], listaColores[i]+tipoTraso[i])
            plt.ylabel('idColegio')
            plt.yticks(np.arange(21),consulta['IDCOLEGIO']-1)
            plt.xlabel('NOTA_'+str(i))
            plt.grid()
        plt.show() 
        
    def graficarFuncionBoxes(self,consulta,titulo):
        plt.boxplot([consulta['NOTA_1'], consulta['NOTA_2'], consulta['NOTA_3'],consulta['NOTA_4']], sym = 'ko', whis = 5.5)  
        plt.xticks([1,2,3,4], ['PRIMER_EXAMEN', 'SEGUNDO_EXAMEN', 'TERCERO_EXAMEN','CUARTO_EXAMEN'], size = 'small', color = 'k') 
        plt.ylabel(titulo)
        plt.grid()
        plt.show()

  

    def graficarQueso(self,consulta,titulo):
        facultad=consulta['NOMBRE_FACULTAD']
        slices=consulta['NUMERO_ALUMNO']
        valores=[0.1,0,0,0,0,0,0,0,0]
        plt.rcParams['toolbar']='none'
        _,_, texto=plt.pie(slices,labels=facultad, autopct='%1.1f%%',explode=valores)
        for text in texto:
            text.set_color('white')
        plt.title(titulo)
        plt.axis('equal')
        plt.show()
    def graficarDesempenioTipoColegio(self,consulta,titulo):
        tipocolegio=consulta['TIPOCOLEGIO']
        promedio1=consulta['NOTA_1']
        promedio2=consulta['NOTA_2']
        promedio3=consulta['NOTA_3']
        promedio4=consulta['NOTA_4']
        plt.plot(tipocolegio,promedio1,'r--')
        plt.plot(tipocolegio,promedio2,'b-.')
        plt.plot(tipocolegio,promedio3,'g--')
        plt.plot(tipocolegio,promedio4,'k-.')
        plt.grid()
        plt.title(titulo)
        plt.legend(['PROMEDIO NOTAS NRO 1','PROMEDIO NOTAS NRO 2','PROMEDIO NOTAS NRO 3','PROMEDIO NOTAS NRO 4'])
        plt.show()

    def graficarEdadPromedio(self,consulta,titulo):
        edad=consulta['EDAD_ALUMNO']
        promedio1=consulta['PROMEDIO_1']
        promedio2=consulta['PROMEDIO_2']
        promedio3=consulta['PROMEDIO_3']
        promedio4=consulta['PROMEDIO_4']
        plt.plot(edad,promedio1,'r')
        plt.plot(edad,promedio2,'b')
        plt.plot(edad,promedio3,'g')
        plt.plot(edad,promedio4,'k')
        plt.grid()
        plt.title(titulo)
        plt.ylabel('PROMEDIO NOTAS')
        plt.xlabel('EDAD')
        plt.legend(['PROMEDIO NOTAS NRO 1','PROMEDIO NOTAS NRO 2','PROMEDIO NOTAS NRO 3','PROMEDIO NOTAS NRO 4'])
        plt.show()
    