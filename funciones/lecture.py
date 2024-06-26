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

# ejemplos de lambda
saludo=lambda n,a:f"hola, {n} , {a}"
print(saludo("ruth","castillo"))

#crear un programa anonimo que reciva como parametro una ista de 5 mnumeros y retorne 2 listas una con los numeros pares y otra con numeros impares
lista=[4,5,6,7,8,9,3,2,45,]


# map
lista=[6,6,4,8,12,3,5,7]
nueva_lista=list(map(lambda x:x+1,lista)) #por defecto retorna una lista
print(nueva_lista)

#tengo una lista der lumnos que todos ellos aprobaron y pasan al tercer semestre,
#problema en mi lista todos estan con el segundo semestre por lo que tendremos que crear una solucion que cambie el campo de semestre de 2 a 3
lista_alumnos=[
    {
        "nombre":"abel",
        "edad":36,
        "semestre":2
    },{
         "nombre":"antony",
        "edad":40,
        "semestre":2
    },{
         "nombre":"edith",
        "edad":50,
        "semestre":2
    }
]
def objeto(e):
    if "semestre" in e:
        e["semestre"]=e["semestre"]+1
    return [e]
lista_cambiada=list(map(objeto,lista_alumnos))
print(lista_cambiada) 
 
# para agregar algo a un objeto

def objeto(e):
    e["especialidad"]="APSTI"
    return [e]

#FILTER ->  devuelbe los numeros o letraz que necsitas

# devolver los numeros pares d3e una lista
lista=[4,8,5,2,1,6,5,7,9,45,25,4,6,47,8,5]
nueva_list=list(filter(lambda x:x%2==0,lista))
print(nueva_list)

#devuelve solo losmenores de 50 de edad
lista_alumnos=[
    {
        "nombre":"abel",
        "edad":36,
        "semestre":2
    },{
         "nombre":"antony",
        "edad":40,
        "semestre":2
    },{
         "nombre":"edith",
        "edad":50,
        "semestre":2
    }
]
menores=list(filter(lambda x:x["edad"]<50,lista_alumnos))
print(menores)