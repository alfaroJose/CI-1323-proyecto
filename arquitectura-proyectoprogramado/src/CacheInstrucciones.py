from MemoriaPrincipal import MemoriaPrincipal
# Clase que representa una cache de instrucciones
class CacheInstrucciones:

    def __init__(self, memoriaPrincipal):
        # Arreglo donde cada elemento tiene el formato: [[bloque], número de bloque, estado]
        self.instrucciones = [
            [[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 24, 'I'],
            [[], -1, 'C'],
            [[], -1, 'C'],
            [[], -1, 'C']
        ]
        self.memoriaPrincipal = memoriaPrincipal

    def imprimir(self):
        for i in range(len(self.instrucciones)):
            for j in range(len(self.instrucciones[i])):
                print(self.instrucciones[i][j], end=' ')
            print()

    # aquí hay que implementar el bloqueo del bus
    def getInstruccion(self, programCounter):
        numBloque = int(programCounter / 4 / 4)
        indexCache = int(numBloque % 4)
        bloqueCache = self.instrucciones[indexCache]
        bloque = bloqueCache[0]
        if(numBloque != bloqueCache[1] or 'C' != bloqueCache[2]):
            bloque = self.memoriaPrincipal.leerBloqueInstrucciones(programCounter)
            self.instrucciones[indexCache][0] = bloque
            self.instrucciones[indexCache][1] = numBloque
            self.instrucciones[indexCache][2] = 'C'
        instruccion = bloque[int((programCounter - (numBloque * 4 * 4)) / 4)]
        return instruccion
