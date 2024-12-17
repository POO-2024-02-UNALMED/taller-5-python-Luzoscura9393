class Animal:
    totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero, zona="", zoo=""):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        self.zoo = zoo
        Animal.totalAnimales += 1  

    @classmethod
    def totalPorTipo(cls):
        from .mamifero import Mamifero
        from .ave import Ave
        from .reptil import Reptil
        from .pez import Pez
        from .anfibio import Anfibio

        return (
            f"Mamiferos : {Mamifero.contar()}\n"
            f"Aves : {Ave.contar()}\n"
            f"Reptiles : {Reptil.contar()}\n"
            f"Peces : {Pez.contar()}\n"
            f"Anfibios : {Anfibio.contar()}"
        )




    def toString(self):
        if self.zona and self.zoo:
            return f"Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()}, habito en {self.getHabitat()} y mi género es {self.getGenero()}, la zona en la que me ubico es {self.zona.nombre}, en el {self.zoo.nombre}."
        else:
            return f"Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()}, habito en {self.getHabitat()} y mi género es {self.getGenero()}."

    def movimiento(self):
        return "desplazarse"
    
    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getHabitat(self):
        return self._habitat

    def getGenero(self):
        return self._genero

    def setNombre(self, nombre):
        self._nombre = nombre

    def setEdad(self, edad):
        self._edad = edad

    def setHabitat(self, habitat):
        self._habitat = habitat

    def setGenero(self, genero):
        self._genero = genero
    
    def setZona(self, zona):
        self._zona = zona
