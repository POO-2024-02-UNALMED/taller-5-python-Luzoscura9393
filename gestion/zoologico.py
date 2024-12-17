class Zoologico:
    def __init__(self, nombre="", ubicacion=""):
        self._nombre=nombre
        self._ubicacion=ubicacion
        self._zonas=[]

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nuevoNombre):
        self._nombre=nuevoNombre


    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self, ubicacionNueva):
        self._ubicacion=ubicacionNueva

    def getZona(self):
        return self._zonas
    
    def setZona(self, zonaNueva):
        self._zonas=zonaNueva
        zonaNueva.setZoo(self)



    def agregarZonas(self, zonaPorAgregar):
        self._zonas.append(zonaPorAgregar)
        zonaPorAgregar.setZoo(self)

    def cantidadTotalAnimales(self):
        return sum(zona.cantidadAnimales() for zona in self._zonas)