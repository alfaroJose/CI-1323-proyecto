import threading
from Cache import Cache

#Clase para representar un nlucleo de un procesador
class Nucleo(threading.Thread):

    def __init__(self, nucleo, memoriaPrincipal, barrera, cacheDatosHermana = None):
        threading.Thread.__init__(self)
        self.nucleo = nucleo
        self.name = nucleo
        self.cache = Cache(memoriaPrincipal, cacheDatosHermana)
        self.barrera = barrera
        self.programCounter = 384
        self.registros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.instructionSet = {5: "lw", 19: "addi", 37: "sw", 56: "div", 71: "add", 72: "mul", 83: "sub", 99: "beq", 100: "bne", 103: "jalr", 111: "jal", 999: "FIN"}

    def run(self):
        self.barrera.wait() #Barrera para hacer que la ejecución de los núcleos inicie al mismo tiempo
        self.iniciar()

    #inicia la ejecución del núcleo
    def iniciar(self):
        resultadoEI = True # resultado del llamado a ejecutarInstruccion(instruccion)
        while True == resultadoEI:
            instruccion = self.cache.getInstruccion(self.programCounter)
            # El program counter debe ser incrementado inmediatamente después de leer la instrucción
            self.programCounter += 4
            resultadoEI = self.ejecutarInstruccion(instruccion)
        print(self.registros, end="Nucleo " + str(self.nucleo) + '\n')

    #Metodo que analiza una instrucción, la identifica y ejecuta su función correspondiente
    def ejecutarInstruccion(self, instruccion):
        exito = True
        if not self.instructionSet[instruccion[0]]:
            exito = False
            print("La instrucción: " + str(instruccion[0]) + " no corresponde a la arquitectura del procesador RISC-V o no ha sido implementada. PC = " + str(int(self.programCounter - 4)))

        elif (111 != instruccion[0] and 4 != len(instruccion)) or (111 == instruccion[0] and 3 != len(instruccion)):
            exito = False
            print("Cantidad incorrecta de parámetros para la instrucción " + str(instruccion[0]) + ": " + self.instructionSet[instruccion[0]] + ". PC = " + str(self.programCounter))

        elif 999 == instruccion[0] and (0 != instruccion[1] or 0 != instruccion[2] or 0 != instruccion[3]):
            exito = False
            print("Parámetros incorrectos para instrucción " + str(instruccion[0]) + ": " + self.instructionSet[instruccion[0]] + ". PC = " + str(self.programCounter)) +". Todos los parámetros deben de ser 0"

        elif 37 != instruccion[0] and 99 !=  instruccion[0] and 100 != instruccion[0] and 999 != instruccion[0] and 0 == instruccion[1]:
            exito = False
            print("El registro X0 es un registro destino inválido.")

        elif instruccion[0] == 5: # lw
            self.lw(instruccion[1], instruccion[2], instruccion[3])

        elif instruccion[0] == 19: # addi
            self.addi(instruccion[1], instruccion[2], instruccion[3])

        elif instruccion[0] == 37: # sw
            self.sw(instruccion[1], instruccion[2], instruccion[3])

        elif instruccion[0] == 56: # div
            self.div(instruccion[1], instruccion[2], instruccion[3])

        elif instruccion[0] == 71: # add
            self.add(instruccion[1], instruccion[2], instruccion[3])

        elif instruccion[0] == 72: # mul
            self.mul(instruccion[1], instruccion[2], instruccion[3])

        elif instruccion[0] == 83: # sub
            self.sub(instruccion[1], instruccion[2], instruccion[3])

        elif instruccion[0] == 99: # beq
            self.beq(instruccion[1], instruccion[2], instruccion[3])

        elif instruccion[0] == 100: # bne
            self.bne(instruccion[1], instruccion[2], instruccion[3])

        elif instruccion[0] == 103: # jalr
            self.jalr(instruccion[1], instruccion[2], instruccion[3])

        elif instruccion[0] == 111: # jal
            self.jal(instruccion[1], instruccion[3])

        elif instruccion[0] == 999: # FIN
            exito = 999

        return exito

    #Funcion que ejecuta la instrucción lw
    def lw(self, rd, rf1, desplazamiento):
        self.registros[rd] = self.cache.getDato(int(desplazamiento + rf1), True)

    # Función que ejecuta la operación addi, la cual suma el contenido de x2 con un inmediato y lo almacena en x1
    def addi(self, x1, x2, n):
        self.registros[x1] = int(self.registros[x2] + n)

    # Funcion que ejecuta la instrucción sw
    def sw(self, rf1, rf2, desplazamiento):
        self.cache.setDato(int(desplazamiento + rf1), rf2, True)

    # Función que ejecuta la operación add, la cual suma el contenido de x2 con x3 y lo almacena en x1
    def add(self, x1, x2, x3):
        self.registros[x1] = int(self.registros[x2] + self.registros[x3])

    # Función que ejecuta la operación sub, la cual resta el contenido de x2 con x3 y lo almacena en x1
    def sub(self, x1, x2, x3):
        self.registros[x1] = int(self.registros[x2] - self.registros[x3])

    # Función que ejecuta la operación mul, la cual multiplica el contenido de x2 con x3 y lo almacena en x1
    def mul(self, x1, x2, x3):
        self.registros[x1] = int(self.registros[x2] * self.registros[x3])

    # Función que ejecuta la operación div, la cual divide el contenido de x2 entre x3 y lo almacena en x1
    def div(self, x1, x2, x3):
        self.registros[x1] = int(self.registros[x2] / self.registros[x3])

    # Función que ejecuta la operación beq, la cual hace un branch modificando el pc con el tercer
    # parámetro, sumando este parametro * 4 y sumandolo al pc, en caso de que los primeros dos parámetros sean iguales
    def beq(self, x1, x2, etiq):
        if x1 == x2:
            self.programCounter += etiq*4

    # Función que ejecuta la operación bne, la cual hace un branch modificando el pc con el tercer parámetro,
    # sumando este parametro * 4 y sumandolo al pc, en caso de que los primeros dos parámetros NO sean iguales
    def bne(self, x1, x2, etiq):
        if x1 != x2:
            self.programCounter += etiq*4

    # Función que ejecuta la operación jal, la cual hace un jump, guardando el pc actual en un registro
    # especificado por el primer parámetro y modificandolo luego con el inmediato en el tercer parámetro
    def jal(self, x1, n):
        self.registros[x1] = self.programCounter
        self.programCounter += n

    # Función que ejecuta la operación jal, la cual hace un jump, guardando el pc actual en un registro
    # especificado por el primer parámetro y modificandolo luego con el inmediato en el tercer parámetro
    # sumado al valor en el registro especificado en el segundo parámetro
    def jalr(self, x1, x2, n):
        self.registros[x1] = self.programCounter
        self.programCounter = self.registros[x2] + n

    def setRegistros(self, registros):
        self.registros = registros

    def getRegistros(self):
        return self.registros

    def setProgramCounter(self, pc):
        self.programCounter = pc

    def getProgramCounter(self):
        return self.programCounter
