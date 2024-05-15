#primer ejercicio
dato=int(input("ingrese su edad:"))
if dato >=18:
 print("eres mayor de edad")
else:
 print("eres menor de edad")

#segundo ejercicio

contraseña_guardada="contraseña"
contraseña_ingresada=input("ingresa la contraseña:")
if contraseña_ingresada == "contraseña" or contraseña_ingresada =="CONTRASEÑA":
 print("la contraseña es correcta")
else:
 print("la contraseña es incorrecta")

 #tercero ejercicio
numero=int(input("ingrese un numero entero positivo:"))
if numero >0:
  print(*range(numero,-1,-1),sep=",")
else:
  print("el numero ingrsado es incorrecto" )
 
 
 
 
 
 

# ejercisio
edad_usuario:int=int(input("engrese sus edad:"))
for edad in range(1,edad_usuario+1):
 print(edad)

# ejercicio 
ultima_letra:str=""
for _ in range(3):
    nombre:str=input("escribe tu nombre->")
    letras:str=nombre[-1]
    ultima_letra+=letras
    print(ultima_letra)
   
  #ejercicio
for i,l in enumerate("aeiou"):
    print(l*(i+1))
