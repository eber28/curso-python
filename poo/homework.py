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

