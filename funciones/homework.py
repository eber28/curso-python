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

# crear uan lista de alumnos con ls siguientes campos 
# nombre ,apellidos , edada, celular, email
# 1 actualizar  los registros de un campo mas todos tendran el campo de programa de estudios de enfermeria
# 2 buscar el segundo registro y actualizar su edad a 50 años

lista_alumnos=[
{
         "nombre":"manuel",
        "apellido":"santander",
        "edad":45,
        "celular":987589445,
        "email":"mannuel15@gmail.com"
    },
    {
    
          
             "nombre":"betsy",
             "apellido":"flores",
             "edad":19,
            "celula":961973098,
            "Email":"betsyflores@gemail.com"
         },
         {   
         
             
             "nombre":"kiara",
             "apellido":"galindo",
             "edad":20,
            "celula":961765098,
            "Email":"kiaragalindo@gemail.com" 
        },
        {
        
              
             "nombre":"zara",
             "apellido":"roman",
             "edad":25,
            "celula":961973098,
            "Email":"zara25@gemail.com" , 
       }
       
]
def objeto(a):
    a["programa_estudios"]="Enfermeria"
    return [
        a
    ]
otra_lista=list(map(objeto,lista_alumnos))
print(otra_lista)



print("**SEGUNDO REGUISTRO CAMBIO DE EDAD**")

def objeto(e):
        e["edad"]=50
        return [e]



lista=list(filter(objeto,lista_alumnos))
print(otra_lista[1])