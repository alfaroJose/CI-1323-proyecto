from CacheDatos import CacheDatos
from CacheInstrucciones import CacheInstrucciones

#Clase controladora de cachés
class Cache:

    def __init__(self):
        self.cacheDatos = CacheDatos()
        self.cacheInstrucciones = CacheInstrucciones()

    def imprimirCacheDatos(self):
        self.cacheDatos.imprimir()

    def imprimirCacheInstrucciones(self):
        self.cacheInstrucciones.imprimir()