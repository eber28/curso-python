# crear una clase banco
# atributos seran  nombre, apellidos, dni, numero de cuenta y saldo inicial
# metodos podremos hacer deposito retirar dinero y ver estado de cuenta.
class banco:
    def __init__(self,nombre,apellido,dni,numero_cuenta,saldo_inicial,banco="PICHINCHA"):
       self.nombre=nombre
       self.apellido=apellido
       self.dni=dni
       self.numero_cuenta=numero_cuenta
       self.saldo_inicial=saldo_inicial
       self.banco=banco

    # metodos
    def deposito(self):
        print("realizando deposito")
    def retirar(self):
        print("realizando retiro")
    def estado(self):
        print("estado normal")

jesus=banco("jesus","cabana",67367673,8734872364879328477,10000)
jesus.deposito(200)
jesus.retirar(100)
jesus.ver()

#2  crear una clase agencia
# con sus atributos nombre ,apellido, dni , numero de haciento, fecha de viaje
# sus metodos seran ingresar origen ingresar destino cancelar viaje, ver estado de pasaje
class Agencia:
    def __init__(self, nombre, apellido, dni, numero_asiento, fecha_viaje):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.numero_asiento = numero_asiento
        self.fecha_viaje = fecha_viaje
        self.origen = None
        self.destino = None
        self.estado = "Pendiente"

    def ingresar_origen(self, origen):
        self.origen = origen
        self.estado = "En curso"

    def ingresar_destino(self, destino):
        self.destino = destino
        self.estado = "Confirmado"

    def cancelar(self):
        self.estado = "Cancelado"
        print("boleto cancelado")

    def ver_estado_de_pasaje(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"DNI: {self.dni}")
        print(f"Número de asiento: {self.numero_asiento}")
        print(f"Fecha de viaje: {self.fecha_viaje}")
        print(f"Origen: {self.origen}")
        print(f"Destino: {self.destino}")
        print(f"Estado: {self.estado}")

# Ejemplo de uso
pasajero1 = Agencia("eber", "roman", "12345678A", 18, "2023-12-25")
pasajero1.ingresar_origen("puquio")
pasajero1.ingresar_destino("san pedro")
pasajero1.ver_estado_de_pasaje()
