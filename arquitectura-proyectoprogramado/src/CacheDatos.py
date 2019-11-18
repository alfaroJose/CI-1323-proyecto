from threading import RLock


# Clase que representa una cache de datos de un núcleo
class CacheDatos:

    def __init__(self, memoriaPrincipal, cacheHermana=None):
        # Arreglo donde cada elemento tiene el formato: [[bloque], número de bloque, estado]
        self.datos = [
            [[], -1, 'C'],
            [[], -1, 'C'],
            [[], -1, 'C'],
            [[], -1, 'C']
        ]
        self.cacheHermana = cacheHermana
        self.candadoCache = RLock()
        self.memoriaPrincipal = memoriaPrincipal

    def imprimir(self):
        for i in range(len(self.datos)):
            for j in range(len(self.datos[i])):
                print(self.datos[i][j], end=' ')
            print()

    # Método que se encarga de la coherencia de caché de datos a la hora de obtener un de esta
    def getDato(self, dirLogica, nucleo_padre, bloquearEjecucion=False):
        dirFisica = int(dirLogica / 4)
        numBloque = int(dirFisica / 4)
        indexCache = int(numBloque % 4)

        bloqueCache = []
        bloque = []
        dato = None

        while dato is None:
            if not self.bloquearCache(True):
                nucleo_padre.barrera.wait()
                nucleo_padre.reloj += 1
                continue
            bloqueCache = self.datos[indexCache]
            bloque = bloqueCache[0]
            if numBloque != bloqueCache[1] or 'C' != bloqueCache[2]:
                if not self.memoriaPrincipal.bloquearBusDatos():
                    self.liberarCache()
                    nucleo_padre.barrera.wait()
                    nucleo_padre.reloj += 1
                    continue
                bloque = self.memoriaPrincipal.leerBloqueDatos(dirFisica)
                #self.memoriaPrincipal.liberarBusDatos()
                self.datos[indexCache][0] = bloque
                self.datos[indexCache][1] = numBloque
                self.datos[indexCache][2] = 'C'
                for ciclo in range(20):
                    nucleo_padre.barrera.wait()
                    nucleo_padre.reloj += 1
                #self.liberarCache()
            dato = bloque[int(dirFisica - (numBloque * 4))]
            #self.liberarCache()
        return dato

    # aquí hay que implementar el bloqueo del bus y cachés
    def setDato(self, dirLogica, dato, nucleo_padre, bloquearEjecucion=False):
        numBloque = int(dirLogica / 4 / 4)
        indexCache = int(numBloque % 4)
        dirFisica = int(dirLogica / 4)
        datoGuardado = False

        while not datoGuardado:
            if not self.bloquearCache(False):
                nucleo_padre.barrera.wait()
                nucleo_padre.reloj += 1
                continue
            if not self.memoriaPrincipal.bloquearBusDatos():
                self.liberarCache()
                nucleo_padre.barrera.wait()
                nucleo_padre.reloj += 1
                continue
            if not self.cacheHermana.bloquearCache():
                self.memoriaPrincipal.liberarBusDatos()
                self.liberarCache()
                nucleo_padre.barrera.wait()
                nucleo_padre.reloj += 1
                continue
            bloqueCache = self.datos[indexCache]

            if numBloque == bloqueCache[1] and 'C' == bloqueCache[2]:
                self.datos[indexCache][0][int(dirFisica - int(numBloque * 4))] = dato
            if numBloque == self.cacheHermana.datos[indexCache]:
                self.cacheHermana.datos[indexCache][2] = 'I'
                nucleo_padre.barrera.wait()
                nucleo_padre.reloj += 1
            self.cacheHermana.liberarCache()
            # print(dirFisica, end='\n')
            self.memoriaPrincipal.guardarDato(dato, dirFisica)
            for ciclo in range(5):
                nucleo_padre.barrera.wait()
                nucleo_padre.reloj += 1
            self.memoriaPrincipal.liberarBusDatos()
            self.liberarCache()
            nucleo_padre.barrera.wait()
            nucleo_padre.reloj += 1
            datoGuardado = True
        return True

    # Método que le permite a la caché intentar un bloqueo de su estructura interna
    def bloquearCache(self, bloquearEjecucion=False):
        return self.candadoCache.acquire(bloquearEjecucion)  # Con False, el método no bloquea la ejecución, esto para evitar DeadLocks

    # Método que le permite a las cachés liberar el bus de datos
    def liberarCache(self):
        liberada = True
        try:
            self.candadoCache.release()
            # self.busDatos.release()
        except:
            liberada = False
        return liberada
