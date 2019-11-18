from threading import Barrier
from threading import Barrier
from threading import RLock
from Nucleo import Nucleo
from Cache import Cache

#Clase para representar al procesador RISC-V
class Procesador:
    def __init__(self, memoriaPrincipal, tcb):
        self.totalNucleos = 2
        self.barrera = Barrier(self.totalNucleos)
        self.candadoImpresionCaches = RLock()
        #print(self.barrera)
        self.memoriaPrincipal = memoriaPrincipal
        self.tcb = tcb
        self.nucleo0 = Nucleo(0, self.memoriaPrincipal, tcb, self.barrera)
        self.nucleo1 = Nucleo(1, self.memoriaPrincipal, tcb, self.barrera, self.nucleo0.cache)
        self.nucleo0.cache.setCacheHermana(self.nucleo1.cache)
        self.nucleo0.set_nucleo_hermano(self.nucleo1)
        self.nucleo1.set_nucleo_hermano(self.nucleo0)
        self.cache = self.iniciar()

    def iniciar(self):
        self.nucleo0.start()
        self.nucleo1.start()
        self.nucleo0.join()
        self.nucleo1.join()

    def imprimirCachesDatos(self):
        print("Núcleo 0")
        self.nucleo0.cache.imprimirCacheDatos()
        print(end='\n')
        print("Núcleo 1")
        self.nucleo1.cache.imprimirCacheDatos()
        print(end='\n')

    def imprimirCachesInstrucciones(self):
        print("Núcleo 0")
        self.nucleo0.cache.imprimirCacheInstrucciones()
        print(end='\n')
        print("Núcleo 1")
        self.nucleo1.cache.imprimirCacheInstrucciones()
