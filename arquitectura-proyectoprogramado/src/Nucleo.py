from Cache import Cache

#Clase para representar un nlucleo de un procesador
class Nucleo:

    def __init__(self):
        self.cache = Cache()
        self.programCounter = 0
        self.registros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def ejecutarInstruccion(self):
        instruccion = self.cache.getInstruccion(self.programCounter)
        if( instruccion == 19 ):
            return 0
        elif( instruccion == 71 ):
            return 0
        elif (instruccion == 83 ):
            return 0
        elif (instruccion == 72 ):
            return 0
        elif (instruccion == 56 ):
            return 0
        elif (instruccion == 5 ):
            return 0
        elif (instruccion == 37 ):
            return 0
        elif (instruccion == 99 ):
            return 0
        elif (instruccion == 100 ):
            return 0
        elif (instruccion == 111 ):
            return 0
        elif (instruccion == 103 ):
            return 0
        elif (instruccion == 999 ):
            return 0
        else:
            print("Instrucción no reconocida")
        self.programCounter += 1

    def addi(self, x1, x2, n):

    def fin(self):


