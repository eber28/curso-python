















### 5  comapracon  de listas 
podemos hacer uso de los operadores de comparacion para comparar listas
**ejm:**
```python
compara=[1,2,3]>[1,2,4]
print(compara)
# salida:
```
###6. cuidado con las copias


### 7. fe de erratas (actualizar listas)
```python
lista=[1,2,3,4,5,6]
lista[0]=2
print(lista)
alumnos=[
    {
        "nombre":"abel",
        "edad":15
    },
    {
        "nombre":"antony",
        "edad":29

    }
]
alumnos[0]["edad"]=30
alumnos[0]={"nombre":"mafer","edad":15}
alumnos[1]["sexo"]="por definir"
print(alumnos)
```

# METODOS EN PYTHON 
#  ## NUMEROS
```python
len(1234567)
```
*devuelve una cantidad de digitos que seria  ->  7 digitos
# ##  TEXTO

#  ## DE LISTAS 
#  ## DE TEXTO
#  ## de tuplas 
#  ## de diciionario

### fe de erratas (actualizar listas)

### 8. listas y diccionario por comprencion
es una tecnica pythonica que nos permite crear listas y diccionaros en una sola linea conbinando bucles y decisiones 
[¡note]
**vlc** value looop condicio  - valor bucle condicion
```python
# lista por comprencion
texto="1,4,8,9,6"
nueva_lista=[int(n) for n in texto.split(",") if int(n)%2==0]
print(nueva_lista)
# diccionario por comprencion
lista_amigos=["abel","antony","edith","ruth"]
diccionario={amigo:len(amigo) for amigo in lista_amigos}
print(diccionario)
```