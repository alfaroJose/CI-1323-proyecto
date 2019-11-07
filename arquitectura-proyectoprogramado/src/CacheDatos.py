#Clase que representa una cache de datos de un núcleo
class CacheDatos:

    def __init__(self):
        self.datos = [[0, 0, 0, 0, -1, 'C'],
                      [0, 0, 0, 0, -1, 'C'],
                      [0, 0, 0, 0, -1, 'C'],
                      [0, 0, 0, 0, -1, 'C']]

    def imprimir(self):
        for i in range(len(self.datos)):
            for j in range(len(self.datos[i])):
                print(self.datos[i][j], end=' ')
            print()