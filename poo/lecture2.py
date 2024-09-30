class personaje:
    #atrivutos
    def __init__(self,nombre,edad,usuario,bando,raza):
        self.nombre=nombre
        self.edad=edad
        self.usuario=usuario
        self.bando=bando
        self.raza=raza
    def mostrar_personaje(self):
        return {

        "nombre":self.nombre,
        "edad":self.edad,
        "usuario":self.usuario,
        "bando":self.bando,
        "raza":self.raza
        }
    
    
luffy=personaje("luffy",18,"gomu gomu no mi","pirata","humano")
cobby=personaje("cobby",16,"no","sword","humano")
king=personaje("king",40,"no mi","pirata","lunaria")