from Cache import Cache

#Clase para representar un nlucleo de un procesador
class Nucleo:

    def __init__(self, memoriaPrincipal):
        self.cache = Cache(memoriaPrincipal)
        self.programCounter = 384
        self.registros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    #Metodo que analiza una instrucción, la identifica y ejecuta su función correspondiente
    def ejecutarInstruccion(self):
        instruccion = self.cache.getInstruccion(self.programCounter)
        #Falta revisar que los parametros vengan bien!!!!!!!!!!!!!!!
        if instruccion[0] == 5: # lw
            if len(instruccion) == 4:
                return 0 #!!!!!!!!!
            else:
                print("Parámetros insuficientes para instrucción lw, código 5, PC = " + str(self.programCounter))

        elif instruccion[0] == 19: # addi
            if len(instruccion) == 4:
                self.addi(instruccion[1], instruccion[2], instruccion[3])
            else:
                print("Parámetros insuficientes para instrucción addi, código 19, PC = " + str(self.programCounter))

        elif instruccion[0] == 37: # sw
            if len(instruccion) == 4:
                return 0 #!!!!!!!!!
            else:
                print("Parámetros insuficientes para instrucción sw, código 37, PC = " + str(self.programCounter))

        elif instruccion[0] == 56: # div
            if len(instruccion) == 4:
                self.div(instruccion[1], instruccion[2], instruccion[3])
            else:
                print("Parámetros insuficientes para instrucción div, código 56, PC = " + str(self.programCounter))

        elif instruccion[0] == 71: # add
            if len(instruccion) == 4:
                self.add(instruccion[1], instruccion[2], instruccion[3])
            else:
                print("Parámetros insuficientes para instrucción add, código 71, PC = " + str(self.programCounter))

        elif instruccion[0] == 72: # mul
            if len(instruccion) == 4:
                self.mul(instruccion[1], instruccion[2], instruccion[3])
            else:
                print("Parámetros insuficientes para instrucción mul, código 72, PC = " + str(self.programCounter))

        elif instruccion[0] == 83: # sub
            if len(instruccion) == 4:
                self.sub(instruccion[1], instruccion[2], instruccion[3])
            else:
                print("Parámetros insuficientes para instrucción sub, código 83, PC = " + str(self.programCounter))

        elif instruccion[0] == 99: # beq
            if len(instruccion) == 4:
                return 0  # !!!!!!!!!
            else:
                print("Parámetros insuficientes para instrucción beq, código 99, PC = " + str(self.programCounter))

        elif instruccion[0] == 100: # bne
            if len(instruccion) == 4:
                return 0  # !!!!!!!!!
            else:
                print("Parámetros insuficientes para instrucción bne, código 100, PC = " + str(self.programCounter))

        elif instruccion[0] == 103: # jalr
            if len(instruccion) == 4:
                return 0  # !!!!!!!!!
            else:
                print("Parámetros insuficientes para instrucción jalr, código 103, PC = " + str(self.programCounter))

        elif instruccion[0] == 111: # jal
            if len(instruccion) == 4:
                if instruccion[2] == 0:
                    return 0  # !!!!!!!!!
                else:
                    print("Parámetros incorrectos para instrucción jal, código 111, PC = " + str(self.programCounter))
                    print("El segundo parametro debe ser 0, 111 31 0 16 por ejemplo")
            else:
                print("Parámetros insuficientes para instrucción jal, código 111, PC = " + str(self.programCounter))

        elif instruccion[0] == 999: # FIN
            if len(instruccion) == 4:
                if instruccion[1] == 0 and instruccion[2] == 0 and instruccion[3] == 0:
                    return 0  # !!!!!!!!!
                else:
                    print("Parámetros incorrectos para instrucción FIN, código 999, PC = " + str(self.programCounter))
                    print("Todos los parámetros deben de ser 0, 999 0 0 0")
            else:
                print("Parámetros insuficientes para instrucción FIN, código 999, PC = " + str(self.programCounter))

        else:
            print("Instrucción: " + str(instruccion[0]) + " no reconocida, PC = " + str(self.programCounter))
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

    def setRegistros(self, registros):
        self.registros = registros

    def getRegistros(self):
        return self.registros

    def setProgramCounter(self, pc):
        self.programCounter = pc

    def getProgramCounter(self):
        return self.programCounter
