import cx_Oracle as cx
class Coneccion:
    def coneccionBD(self):
        host="localhost"
        user="ADMINDATO"
        password="root"
        tsname="orcl"
        conexion = cx.connect(user, password,host+"/"+tsname)
        return conexion