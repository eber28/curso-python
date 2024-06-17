# return devuelve valores que podre hacer uso 
# crear una funcion que retorno el numero 10, y muestre por terminal si es par 
# siempre que el valor 
def diez():
    return 10
if diez()%2==0:
    print("es par")
else:
    print("es impar ") 
# print solo muestra por terminal

# return cuando keremos que nuestra funcion devuelva o tetorne un tipo de dato o un tipo de dato estructurado

#crear una funcion  que muestre el producto dde dos numeros
def producto(a,b):
    return a*b

#crear una funcion que me retorne una lista de tres numeros
def lista_numeros():
    return [3,2,6]
#print usaremos cada vez que nuestra funcion retorne un mensaje
# crear una funcion  que por parametro reciba un nombre y retorne un mensaje de bienvenida con el nombre.
def mensaje(nombre):
    print(f"hola,{nombre}, bienvenido al chongo")

#crear una funcion que reciba pr parametro una lista de numeros y devuelva el numero menor,mostrar por terminal el valor retornado por la funcion 
lista=[4,3,5,6,7,2,3,9,]
def min(l):
    minimo=l[0]
    for n in l:
        if n < minimo:
            minimo=n
    return minimo
print(min(lista))

# crear una funcion que reciva como parametro el nombre y la edad de personas mi funcion debera retornar un diccionario con los datos, luegp mostrar por terminal el valor de retorno de mi funcion
nombre="abel"
edad=19
def persona(nombre,edad):
    return {
        "nombre":nombre,
        "edad":edad
    }
print(persona(nombre,edad))

# empaqueta y desempaqueta de argumentos nominales
def alumnos(**kwargs):
    kwargs["nombre"]="abel"
    print(kwargs)
alumnos(nombre="miguel",apellido="largo",edad=30)