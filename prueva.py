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