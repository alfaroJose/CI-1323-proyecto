#Clase que representa una cache de instrucciones
class CacheInstrucciones:

    def __init__(self):
        self.instrucciones = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def imprimir(self):
        for i in range(len(self.instrucciones)):
            for j in range(len(self.instrucciones[i])):
                print(self.instrucciones[i][j], end=' ')
            print()
