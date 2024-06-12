
class TablaHash:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.tabla = [None] * tamaño

    def funcion_hash(self, clave): 
        return hash(clave) % self.tamaño

    def insertar(self, clave, valor):
        indice = self.funcion_hash(clave)
        if self.tabla[indice] is None:
            self.tabla[indice] = [(clave, valor)]
        else:
            for par in self.tabla[indice]:
                if par[0] == clave:
                    par = (clave, valor)
                    return
            self.tabla[indice].append((clave, valor))

    def recuperar(self, clave):
        indice = self.funcion_hash(clave)
        if self.tabla[indice] is None:
            return None
        for par in self.tabla[indice]:
            if par[0] == clave:
                return par[1]
        return None

    def eliminar(self, clave):
        indice = self.funcion_hash(clave)
        if self.tabla[indice] is None:
            return
        for i, par in enumerate(self.tabla[indice]):
            if par[0] == clave:
                del self.tabla[indice][i]
                return
            
            
#Desarrollar un algoritmo que implemente una tabla hash para una guía de teléfono, los datos
#que se conocen son número de teléfono, apellido, nombre y dirección de la persona. El campo
#clave debe ser el número de teléfono.

TablaHash = TablaHash(10)
i = 0
while i<10:
    print ("ingrese numero de telefono")
    numero = (input)
    print = ("ingrese apellido")
    apellido = input
    print ("ingrese su nombre")
    nombre= input
    print ("ingrese la direccion")
    direccion = input
    TablaHash.insertar(numero, apellido, nombre, direccion)

print (TablaHash)