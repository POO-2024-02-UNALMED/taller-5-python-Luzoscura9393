from .animal import Animal

class Mamifero(Animal):
    contador = 0 
    caballos = 0
    leones = 0
    listado = [] 

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas, zona=None, zoo=None):
        super().__init__(nombre, edad, habitat, genero, zona, zoo)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.contador += 1
        Mamifero.listado.append(self)

    @classmethod
    def contar(cls):
        return cls.contador

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        cls.caballos += 1
        return cls(nombre, edad, "pradera", genero, pelaje=True, patas=4)

    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        cls.leones += 1
        return cls(nombre, edad, "selva", genero, pelaje=True, patas=4)

    @classmethod
    def cantidadMamiferos(cls):
        return cls.contador
    
    def isPelaje(self):
        return self._pelaje

    def movimiento(self):
        return "desplazarse"

    def getPelaje(self):
        return self._pelaje

    def getPatas(self):
        return self._patas

    def setPelaje(self, pelaje):
        self._pelaje = pelaje

    def setPatas(self, patas):
        self._patas = patas