# crear uan funcion que reciva por argumentos n numeros y retorne una lista con los numeros pares
def num(*args):
    lista_pares=[]
    for n in args:
        if n%2==0:
            lista_pares.append(n)
    return lista_pares
print(num(2,58,74,6,4,4,5,48,7,8,89,))

# por compresion
def num(*args):
    return [n for n in args]
    print(num(2,58,74,6,4,4,5,48,7,8,89,))


#crear tres funciones para los siguientes casos
#calcular el numero menor
#calcular el numero mayor
#calcular la suma de todos los numeros
#se le pasara por argumento n numeros
def min(*args):
    menor=args[0]
    for n in args:
        if n<menor:
            menor=n
    return menor

def max(*args):
    mayor=args[0]
    for n in args:
        if n>mayor:
            mayor=n
    return mayor

def sum(*args):
    suma=0
    for n in args:
        if n:
            suma+=n
    return suma
