from CacheDatos import CacheDatos
from CacheInstrucciones import CacheInstrucciones

#Clase controladora de cachés
class Cache:

    def __init__(self, memoriaPrincipal):
        self.cacheDatos = CacheDatos(memoriaPrincipal)
        self.cacheInstrucciones = CacheInstrucciones(memoriaPrincipal)

    def imprimirCacheDatos(self):
        self.cacheDatos.imprimir()

    def imprimirCacheInstrucciones(self):
        self.cacheInstrucciones.imprimir()

    def getInstruccion(self, programCounter):
        return self.cacheInstrucciones.getInstruccion(programCounter)
    def getDato(self, programCounter):
        return self.cacheDatos.getDato(programCounter)