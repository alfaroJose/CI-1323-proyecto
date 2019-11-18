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

    # Método que obtiene un dato para la caché de datos de memoria principal, se encarga de la coherencia de caché y bloqueos necesarios
    def getDato(self, dirLogica, nucleo_padre, bloquearEjecucion=False):
        dirFisica = int(dirLogica / 4)
        numBloque = int(dirFisica / 4)
        indexCache = int(numBloque % 4)

        bloqueCache = []
        bloque = []
        dato = None

        while dato is None:
            if not self.bloquearCache(True): #Intenta bloquear propia caché
                nucleo_padre.barrera.wait()
                nucleo_padre.reloj += 1
                continue
            bloqueCache = self.datos[indexCache]
            bloque = bloqueCache[0]
            if numBloque != bloqueCache[1] or 'C' != bloqueCache[2]:
                if not self.memoriaPrincipal.bloquearBusDatos(): #Intenta bloquear bus de datos
                    self.liberarCache()
                    nucleo_padre.barrera.wait()
                    nucleo_padre.reloj += 1
                    continue
                bloque = self.memoriaPrincipal.leerBloqueDatos(dirFisica)
                self.datos[indexCache][0] = bloque
                self.datos[indexCache][1] = numBloque
                self.datos[indexCache][2] = 'C'
                for ciclo in range(20): #Espera para actualizar el reloj correspondientemente
                    nucleo_padre.barrera.wait()
                    nucleo_padre.reloj += 1
            dato = bloque[int(dirFisica - (numBloque * 4))]
        return dato

    # Método que guarda un dato en memoria de la caché de datos se encarga de la coherencia de caché y bloqueos necesarios
    def setDato(self, dirLogica, dato, nucleo_padre, bloquearEjecucion=False):
        numBloque = int(dirLogica / 4 / 4)
        indexCache = int(numBloque % 4)
        dirFisica = int(dirLogica / 4)
        datoGuardado = False

        while not datoGuardado:
            if not self.bloquearCache(False): #Intenta bloquear propia caché
                nucleo_padre.barrera.wait()
                nucleo_padre.reloj += 1
                continue
            if not self.memoriaPrincipal.bloquearBusDatos(): #Intenta bloquear bus de datos
                self.liberarCache()
                nucleo_padre.barrera.wait()
                nucleo_padre.reloj += 1
                continue
            if not self.cacheHermana.bloquearCache(): #Intenta bloquear caché del otro núcleo
                self.memoriaPrincipal.liberarBusDatos()
                self.liberarCache()
                nucleo_padre.barrera.wait()
                nucleo_padre.reloj += 1
                continue
            bloqueCache = self.datos[indexCache]
            #Coherencia de las cachés
            if numBloque == bloqueCache[1] and 'C' == bloqueCache[2]:
                self.datos[indexCache][0][int(dirFisica - int(numBloque * 4))] = dato
            if numBloque == self.cacheHermana.datos[indexCache]:
                self.cacheHermana.datos[indexCache][2] = 'I'
                nucleo_padre.barrera.wait()
                nucleo_padre.reloj += 1
            self.cacheHermana.liberarCache()
            self.memoriaPrincipal.guardarDato(dato, dirFisica)
            for ciclo in range(5):#Ciclo para simular espera en coclos de reloj
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
        except:
            liberada = False
        return liberada
