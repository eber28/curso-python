















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