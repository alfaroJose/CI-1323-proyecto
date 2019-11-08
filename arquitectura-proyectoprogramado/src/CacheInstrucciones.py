# Clase que representa una cache de instrucciones
class CacheInstrucciones:

    def __init__(self):
        self.instrucciones = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 'C'],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 'C'],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 'C'],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 'C']]

    def imprimir(self):
        for i in range(len(self.instrucciones)):
            for j in range(len(self.instrucciones[i])):
                print(self.instrucciones[i][j], end=' ')
            print()

    def getInstruccion(self, programCounter):
        bloque = self.instrucciones[(programCounter % 16) % 4];
        if((programCounter % 16) ==bloque[16] and 'C' == bloque[17]):
            return self.instrucciones[(programCounter % 16) % 4]
