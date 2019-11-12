from threading import RLock
# Clase que representa una cache de datos de un núcleo
class CacheDatos:

    def __init__(self, memoriaPrincipal):
        # Arreglo donde cada elemento tiene el formato: [[bloque], número de bloque, estado]
        self.datos = [
            [[], -1, 'C'],
            [[], -1, 'C'],
            [[], -1, 'C'],
            [[], -1, 'C']
        ]
        self.candadoCache = RLock()
        self.memoriaPrincipal = memoriaPrincipal

    def imprimir(self):
        for i in range(len(self.datos)):
            for j in range(len(self.datos[i])):
                print(self.datos[i][j], end=' ')
            print()

    # aquí hay que implementar el bloqueo del bus y cachés
    def getDato(self, dirLogica, bloquearEjecucion = False):
        numBloque = int(dirLogica / 4 / 4)
        indexCache = int(numBloque % 4)
        bloqueCache = self.datos[indexCache]
        bloque = bloqueCache[0]

        self.bloquearCache(bloquearEjecucion)
        if numBloque != bloqueCache[1] or 'C' != bloqueCache[2]:
            bloque = self.memoriaPrincipal.leerBloqueDatos(dirLogica)
            self.datos[indexCache][0] = bloque
            self.datos[indexCache][1] = numBloque
            self.datos[indexCache][2] = 'C'
        dato = bloque[int((dirLogica / 4) - (numBloque * 4))]
        self.liberarCache()
        return dato

    # aquí hay que implementar el bloqueo del bus y cachés
    def setDato(self, dirLogica, dato, bloquearEjecucion = False):
        numBloque = int(dirLogica / 4 / 4)
        indexCache = int(numBloque % 4)
        bloqueCache = self.datos[indexCache]
        dirFisica = int(dirLogica / 4)

        self.bloquearCache(bloquearEjecucion)
        if numBloque == bloqueCache[1] and 'C' == bloqueCache[2]:
            self.datos[indexCache][0][int(dirFisica - int(numBloque * 4))] = dato
        self.memoriaPrincipal.guardarDato(dato, dirFisica)
        self.liberarCache()
        return True

    #Método que le permite a la caché intentar un bloqueo de su estructura interna
    def bloquearCache(self, bloquearEjecucion = False):
        return self.candadoCache.acquire(bloquearEjecucion) # Con False, el método no bloquea la ejecución, esto para evitar DeadLocks

    #Método que le permite a las cachés liberar el bus de datos
    def liberarCache(self):
        liberada = True
        try:
            self.candadoCache.release()
            #self.busDatos.release()
        except:
            liberada = False
        return liberada