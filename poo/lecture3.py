# crear una clase de alumnos con los atributos que usted crea por conveniente
# luego instanciara a 4 alumnos

class alumnos:
    def __init__(self,nombre,edad,dni,apellido,genero,programa_de_estudio="APSTI"):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni
        self.apellido=apellido
        self.genero=genero
        self.programa_de_estudio=programa_de_estudio
        
    #metodos
    def escribir(self):
        print("estoy escribiendo")
    def tarea(self):
        print("haciendo tarea")
    def terminar_tarea(self):
        print("terminando tarea anterior")

eber=alumnos("eber",18,75174258,"roman","masculino")
jesus=alumnos("jesus",19,75674258,"cabana","masculino")
alex=alumnos("alex",28,75104258,"flores","masculino")
flor=alumnos("flor",18,75179258,"lucana","femenino")

