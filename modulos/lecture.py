"""practicando pylint"""

nombre_alumno:str="miguel"
def suma(a:int,b:int)->int:
     """funcion para sumar"""
     return a+b
print(suma(4,7))

def resta(a,b):
     """funcion para restar dos numeros"""
     return a-b

# importacion derecta
import operaciones
suma:int=operaciones.suma(9,10)
print(suma)