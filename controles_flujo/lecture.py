variable:str=input("escriba dos o mas operaciobnes separados por  comas:")
contador:int=0
for indice,letra in enumerate(variable):
    if letra == ",":
        print(f"su indice es {indice}")
        contador+=1
print(f"la cantidad de comas es {contador}")