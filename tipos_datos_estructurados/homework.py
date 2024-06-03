













# 2.crear una lista con 4 diccionarios donde tendrann los datos de susu mascotas (nombre,edad,sexo,raza)

#tareas
# mostrar la lista de los 4 diccionarios
# editar el 3er registro y cambiarle la edad sin modificar la lista original
# mostrar la lista original y luego

#  LOS METODOS   SON ERRAMIENTAS QUW SIRVEN PARA MANIPULAR TIPOS DE DATOS ESTRUCTURADOS Y DE TIPOS DE STRING



### ejercicio del dia lunes


# yo: como el dueño 
# deseeo: ver la lista de mis autos 
# para :  para ver la cantidad de mis autos 
  
# yo: como dueño
# deseo: actualizar la lista de los autos y modificarlos
# para:  para agregar mas autos a la lista

autos=["\ntoyota:rojo",
       "toyota.verde",
       "toyota:azul",
       "ford:gris",
       "nissan:rojo",
       "hyundai:gris",
       "chevroleth:blanco",
       "nissan:blanco"]
print(f"\n tienes ->",len(autos),"autos")
for auto in autos:
    print(auto)
nuevos_autos=int(input("\ningrese la cantida de autos que kieres agregar:"))
for i in range(nuevos_autos):
    nuevo_auto=input("ingrese la descripcion del auto nuevo :->")
    autos.append(nuevo_auto)
print("\nlista actualizada de autos:")
for auto in autos:
    print(auto)





