from Cache import Cache

#Clase para representar un nlucleo de un procesador
class Nucleo:

    def __init__(self):
        self.cache = Cache()
        self.programCounter = 0
        self.registros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def ejecutarInstruccion(self):
        instruccion = self.cache.getInstruccion(self.programCounter)
        #interpretar la instrucción
        return 1