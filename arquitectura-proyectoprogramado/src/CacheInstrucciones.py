from MemoriaPrincipal import MemoriaPrincipal
# Clase que representa una cache de instrucciones
class CacheInstrucciones:

    def __init__(self, memoriaPrincipal):
        # Arreglo donde cada elemento tiene el formato: [[bloque], número de bloque, estado]
        self.instrucciones = [
            [[], -1],
            [[], -1],
            [[], -1],
            [[], -1]
        ]
        self.memoriaPrincipal = memoriaPrincipal

    def imprimir(self):
        for i in range(len(self.instrucciones)):
            for j in range(len(self.instrucciones[i])):
                print(self.instrucciones[i][j], end=' ')
            print()

    def getInstruccion(self, programCounter):
        numBloque = int(programCounter / 4 / 4)
        indexCache = int(numBloque % 4)
        bloqueCache = self.instrucciones[indexCache]
        bloque = bloqueCache[0]
        if(numBloque != bloqueCache[1]):
            self.memoriaPrincipal.bloquearBusInstrucciones()
            bloque = self.memoriaPrincipal.leerBloqueInstrucciones(programCounter)
            self.memoriaPrincipal.liberarBusInstrucciones()
            self.instrucciones[indexCache][0] = bloque
            self.instrucciones[indexCache][1] = numBloque
        instruccion = bloque[int((programCounter - (numBloque * 4 * 4)) / 4)]
        return instruccion
