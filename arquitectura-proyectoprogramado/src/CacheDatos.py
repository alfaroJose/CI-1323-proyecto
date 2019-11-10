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
        self.memoriaPrincipal = memoriaPrincipal

    def imprimir(self):
        for i in range(len(self.datos)):
            for j in range(len(self.datos[i])):
                print(self.datos[i][j], end=' ')
            print()

    # aquí hay que implementar el bloqueo del bus y cachés
    def getDato(self, dirLogica):
        numBloque = int(dirLogica / 4 / 4)
        indexCache = int(numBloque % 4)
        bloqueCache = self.datos[indexCache]
        bloque = bloqueCache[0]
        if numBloque != bloqueCache[1] or 'C' != bloqueCache[2]:
            bloque = self.memoriaPrincipal.leerBloqueDatos(dirLogica)
            self.datos[indexCache][0] = bloque
            self.datos[indexCache][1] = numBloque
            self.datos[indexCache][2] = 'C'
        dato = bloque[int((dirLogica / 4) - (numBloque * 4))]
        return dato

    # aquí hay que implementar el bloqueo del bus y cachés
    def setDato(self, dirLogica, dato):
        numBloque = int(dirLogica / 4 / 4)
        indexCache = int(numBloque % 4)
        bloqueCache = self.datos[indexCache]
        if numBloque == bloqueCache[1] and 'C' == bloqueCache[2]:
            self.datos[indexCache][0][int((dirLogica / 4) - (numBloque * 4))] = dato
        return True
