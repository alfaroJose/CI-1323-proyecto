from CacheDatos import CacheDatos
from CacheInstrucciones import CacheInstrucciones

#Clase controladora de cachés
class Cache:

    def __init__(self, nucleo, memoriaPrincipal, cacheHermana):
        self.nucleoPadre = nucleo
        self.cacheHermana = cacheHermana #Caché del otro núcleo
        if self.cacheHermana:
            self.cacheDatos = CacheDatos(memoriaPrincipal, self.cacheHermana.cacheDatos)
        else:
            self.cacheDatos = CacheDatos(memoriaPrincipal)
        self.cacheInstrucciones = CacheInstrucciones(memoriaPrincipal)

    def imprimirCacheDatos(self):
        self.cacheDatos.imprimir()

    def imprimirCacheInstrucciones(self):
        self.cacheInstrucciones.imprimir()

    #Solución implementada para la coherencia de las cachés de ambos núcleos
    def setCacheHermana(self, cachehermana):
        self.cacheHermana = cachehermana
        self.cacheDatos.cacheHermana = self.cacheHermana.cacheDatos

    def getInstruccion(self, programCounter):
        return self.cacheInstrucciones.getInstruccion(programCounter, self.nucleoPadre)

    #Método que libera el bus de instrucciones
    def liberar_bus_instrucciones(self):
        self.cacheInstrucciones.liberar_bus_instrucciones(self.nucleoPadre)

    def getDato(self, dirLogica):
        return self.cacheDatos.getDato(dirLogica, self.nucleoPadre, True)

    def setDato(self, dirLogica, dato, bloquearEjecucion = False):
        return self.cacheDatos.setDato(dirLogica, dato, self.nucleoPadre, bloquearEjecucion)

    #Método que libera el bus de datos
    def liberar_bus_datos(self):
        if self.cacheDatos.memoriaPrincipal.liberarBusDatos():
            self.nucleoPadre.barrera.wait()
            self.nucleoPadre.reloj += 1

    #Método que coloca el candado en la caché de datos
    def bloquearCacheDatos(self, bloquearEjecucion = False):
        return self.cacheDatos.bloquearCache(bloquearEjecucion)

    #Método que libera el candado de la caché de datos
    def liberarCacheDatos(self):
        return self.cacheDatos.liberarCache()