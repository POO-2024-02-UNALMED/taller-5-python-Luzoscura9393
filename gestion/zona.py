class Zona:
    def __init__(self, nombre="", zoo=None):
        self._nombre=nombre
        self._zoo=zoo
        self._animales=[]

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombreNuevo):
        self._nombre=nombreNuevo

    def getZoo(self):
        return self._zoo
    
    def setZoo(self, zooNuevo):
        self._zoo=zooNuevo

    def getAnimales(self):
        return self._animales

    def setAnimales(self, animalesNuevos):
        self._animales=animalesNuevos
        animalesNuevos.setZona(self)


    
    def agregarAnimales(self, animalAgregar):
        self._animales.append(animalAgregar)
        animalAgregar.setZona(self)

    def cantidadAnimales(self):
        return len(self._animales)