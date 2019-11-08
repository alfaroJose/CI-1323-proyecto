from Cache import Cache

#Clase para representar un nlucleo de un procesador
class Nucleo:

    def __init__(self):
        self.cache = Cache()
        self.programCounter = 0
        self.registros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def ejecutarInstruccion(self):
        return 1

    def intructionFetch(self):
        return self.cache.getInstruccion(self)

    #en proceso
    def intructionDecode(self, instruccion):
        return instruccion

    def intructionExec(self, instruccion):
        return instruccion

    def intructionMem(self, instruccion):
        return instruccion

    def intructionWB(self, instruccion):
        return instruccion
