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
        return self.cacheInstrucciones.getInstruccion(programCounter, self.nucleoPadre)

    def liberar_bus_instrucciones(self):
        self.cacheInstrucciones.liberar_bus_instrucciones(self.nucleoPadre)

    def getDato(self, dirLogica):
        return self.cacheDatos.getDato(dirLogica, self.nucleoPadre, True)

    def setDato(self, dirLogica, dato, bloquearEjecucion = False):
        return self.cacheDatos.setDato(dirLogica, dato, self.nucleoPadre, bloquearEjecucion)

    def liberar_bus_datos(self):
        if self.cacheDatos.memoriaPrincipal.liberarBusDatos():
            self.nucleoPadre.barrera.wait()
            self.nucleoPadre.reloj += 1

    def bloquearCacheDatos(self, bloquearEjecucion = False):
        return self.cacheDatos.bloquearCache(bloquearEjecucion)

    def liberarCacheDatos(self):
        return self.cacheDatos.liberarCache()