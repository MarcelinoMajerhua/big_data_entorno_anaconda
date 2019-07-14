import cx_Oracle

class conect():
    def __init__ (self):
        host="localhost"
        user="ADMINDATO"
        password="root"
        tsname="orcl"
        try:
            self.conexion = cx_Oracle.connect(user, password,host+"/"+tsname)
        except Exception as error:
            print("no se pudo conectar a la base de datos: "+error)
        else:
            print("conexion establecida !!!")
    def sentenciaCompuesta(self, sentencia):
        cursor = self.conexion.cursor()
        cursor.execute(sentencia)
        datos=cursor.fetchall()
        cursor.close()
        return datos
    def close(self):
        self.conexion.close()

    def commint(self):
        self.conexion.commint()

if __name__=="__main__":
    nexo=conect()
    for fila in nexo.sentenciaCompuesta("select ID_ALUMNO, PROCEDENCIA_ALUMNO  from alumno"):
        print(fila)