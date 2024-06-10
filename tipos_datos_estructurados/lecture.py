

# DATO ESTRUCTURADO
#lista_original=[1,2,3,4]
#copia_lista=lista_original
#lista_original[-1]=15
#print(copia_lista)



#crear una lista de numeros enteros del siguiente texto
texto="1,2,3,4,5,"
nueva_lista=[]
for n in texto.split(","):
    nueva_lista.append(int(n))
print(nueva_lista)

#aplicando la tecnica vlc valor bucle y condicion
texto="1,4,8,9,6"
nueva_lista=[int(n) for n in texto.split(",") if int(n)%2==0]
print(nueva_lista)

#diccionario por comprencion
lista_amigos=["abel","antony","edith","ruth"]
diccionario={}
for _,v in enumerate(lista_amigos):
    diccionario[v]=len(v)
print(diccionario)

#aplicando el vlc
lista_amigos=["abel","antony","edith","ruth"]
diccionario={amigo:len(amigo) for amigo in lista_amigos}
print(diccionario)


























































































