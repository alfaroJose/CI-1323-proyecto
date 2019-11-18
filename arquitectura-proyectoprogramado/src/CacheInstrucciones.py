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

    #Retorna la instrucción correspondiente, además se encarga de los accesos a esta según el bus de instrucciones
    def getInstruccion(self, programCounter, nucleoPadre):
        numBloque = int(programCounter / 4 / 4)
        indexCache = int(numBloque % 4)
        bloqueCache = self.instrucciones[indexCache]
        bloque = bloqueCache[0]
        if numBloque != bloqueCache[1]:
            while not self.memoriaPrincipal.bloquearBusInstrucciones():
                nucleoPadre.barrera.wait()
                nucleoPadre.reloj += 1
            bloque = self.memoriaPrincipal.leerBloqueInstrucciones(programCounter)
            for ciclo in range(10):
                nucleoPadre.barrera.wait()
                nucleoPadre.reloj += 1
            self.instrucciones[indexCache][0] = bloque
            self.instrucciones[indexCache][1] = numBloque
        instruccion = bloque[int((programCounter - (numBloque * 4 * 4)) / 4)]
        return instruccion

    #Libera el bus de instrucciones, espera a que el otro núcleo alcance este punto y actualiza reloj
    def liberar_bus_instrucciones(self, nucleo_padre):
        if self.memoriaPrincipal.liberarBusInstrucciones():
            nucleo_padre.barrera.wait()
            nucleo_padre.reloj += 1
