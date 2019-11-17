from CacheDatos import CacheDatos
from CacheInstrucciones import CacheInstrucciones

#Clase controladora de cachés
class Cache:

    def __init__(self, nucleo, memoriaPrincipal, cacheHermana):
        self.nucleoPadre = nucleo
        self.cacheHermana = cacheHermana
        if(self.cacheHermana):
            self.cacheDatos = CacheDatos(memoriaPrincipal, self.cacheHermana.cacheDatos)
        else:
            self.cacheDatos = CacheDatos(memoriaPrincipal)
        self.cacheInstrucciones = CacheInstrucciones(memoriaPrincipal)

    def imprimirCacheDatos(self):
        self.cacheDatos.imprimir()

    def imprimirCacheInstrucciones(self):
        self.cacheInstrucciones.imprimir()

    def setCacheHermana(self, cachehermana):
        self.cacheHermana = cachehermana
        self.cacheDatos.cacheHermana = self.cacheHermana.cacheDatos

    def getInstruccion(self, programCounter):
        return self.cacheInstrucciones.getInstruccion(programCounter)

    def getDato(self, dirLogica, bloquearEjecucion = False):
        return self.cacheDatos.getDato(dirLogica, bloquearEjecucion)

    def setDato(self, dirLogica, dato, bloquearEjecucion = False):
        return self.cacheDatos.setDato(dirLogica, dato, bloquearEjecucion)

    def bloquearCacheDatos(self, bloquearEjecucion = False):
        return self.cacheDatos.bloquearCache(bloquearEjecucion)

    def liberarCacheDatos(self):
        return self.cacheDatos.liberarCache()