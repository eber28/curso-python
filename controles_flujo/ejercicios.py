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