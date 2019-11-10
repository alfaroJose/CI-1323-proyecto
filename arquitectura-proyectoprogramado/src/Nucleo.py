from Cache import Cache

#Clase para representar un nlucleo de un procesador
class Nucleo:

    def __init__(self):
        self.cache = Cache()
        self.programCounter = 0
        self.registros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    #Metodo que analiza una instrucción, la identifica y ejecuta su función correspondiente
    def ejecutarInstruccion(self):
        instruccion = self.cache.getInstruccion(self.programCounter)
        #Falta revisar que los parametros vengan bien!!!!!!!!!!!!!!!
        if instruccion[0] == 5: # lw
            return 0
        elif instruccion[0] == 19: # addi
                self.addi(instruccion[1], instruccion[2], instruccion[3])
        elif instruccion[0] == 37: # sw
            return 0
        elif instruccion[0] == 56: # div
            self.div(instruccion[1], instruccion[2], instruccion[3])
        elif instruccion[0] == 71: # add
            self.add(instruccion[1], instruccion[2], instruccion[3])
        elif instruccion[0] == 72: # mul
            self.mul(instruccion[1], instruccion[2], instruccion[3])
        elif instruccion[0] == 83: # sub
            self.sub(instruccion[1], instruccion[2], instruccion[3])
        elif instruccion[0] == 99: # beq
            return 0
        elif instruccion[0] == 100: # bne
            return 0
        elif instruccion[0] == 103: # jalr
            return 0
        elif instruccion[0] == 111: # jal
            return 0
        elif instruccion[0] == 999: # FIN
            return 0
        else:
            print("Instrucción no reconocida")
        self.programCounter += 4

    # Función que ejecuta la operación addi, la cual suma el contenido de x2 con un inmediato y lo almacena en x1
    def addi(self, x1, x2, n):
        self.registros[x1] = self.registros[x2] + n

    # Función que ejecuta la operación add, la cual suma el contenido de x2 con x3 y lo almacena en x1
    def add(self, x1, x2, x3):
        self.registros[x1] = self.registros[x2] + self.registros[x3]

    # Función que ejecuta la operación sub, la cual resta el contenido de x2 con x3 y lo almacena en x1
    def sub(self, x1, x2, x3):
        self.registros[x1] = self.registros[x2] - self.registros[x3]

    # Función que ejecuta la operación mul, la cual multiplica el contenido de x2 con x3 y lo almacena en x1
    def mul(self, x1, x2, x3):
        self.registros[x1] = self.registros[x2] * self.registros[x3]

    # Función que ejecuta la operación div, la cual divide el contenido de x2 entre x3 y lo almacena en x1
    def div(self, x1, x2, x3):
        self.registros[x1] = self.registros[x2] / self.registros[x3]


