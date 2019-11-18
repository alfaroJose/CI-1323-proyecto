import threading
from Cache import Cache

#Clase para representar un nlucleo de un procesador
class Nucleo(threading.Thread):

    def __init__(self, nucleo, memoriaPrincipal, tcb, barrera, cacheHermana = None):
        threading.Thread.__init__(self)
        self.nucleo = nucleo
        self.name = nucleo
        self.nucleoHermano = None
        self.reloj = 0
        self.ir = [] #Instruction register
        self.cache = Cache(self, memoriaPrincipal, cacheHermana)
        self.tcb = tcb
        self.barrera = barrera
        self.programCounter = 384
        self.hililloActual = None
        self.registros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.instructionSet = {5: "lw", 19: "addi", 37: "sw", 56: "div", 71: "add", 72: "mul", 83: "sub", 99: "beq", 100: "bne", 103: "jalr", 111: "jal", 999: "FIN"}

    #Método que se ejecuta cuando se le da start al núcleo, espera que ambos núcleos estén listos para ejecutarse
    #y después empieza con su ejecición
    def run(self):
        self.barrera.wait() # Uso de la barrera para hacer que la ejecución de los núcleos inicie "al mismo tiempo"
        self.hililloActual = self.tcb.pedirHilillo(self.nucleo)
        self.iniciar()

    #inicia la ejecución del núcleo
    def iniciar(self):
        while self.hililloActual:
            resultadoEI = True  # resultado del llamado a ejecutarInstruccion()
            self.reiniciarRegistros() # Pone los registros en 0
            self.programCounter = self.hililloActual.getDireccion() #Obtiene el PC según el hilillo a ejecutar
            while True == resultadoEI:
                self.ir = self.cache.getInstruccion(self.programCounter) #Obtiene una instrucción según el PC
                self.cache.liberar_bus_instrucciones()
                # El program counter debe y es incrementado inmediatamente después de leer la instrucción
                self.programCounter += 4
                resultadoEI = self.ejecutarInstruccion()
            self.hililloActual.setEstado(self.ir)
            self.hililloActual.setReloj(self.reloj)
            self.tcb.modificarRegistrosHilillo(self.hililloActual.getIdentificador(), self.registros)
            self.hililloActual = self.tcb.pedirHilillo(self.nucleo)
        self.nucleoHermano.barrera._parties = 1
        self.barrera._parties = 1

    #Indica cuál es el núcleo que se corre en paralelo
    def set_nucleo_hermano(self, nucleoHermano):
        self.nucleoHermano = nucleoHermano

    def reiniciarRegistros(self):
        self.registros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    #Metodo que analiza una instrucción, la identifica y ejecuta su función correspondiente
    def ejecutarInstruccion(self):
        exito = True
        if not self.instructionSet[self.ir[0]]:
            exito = False
            print("La instrucción: " + str(self.ir[0]) + " no corresponde a la arquitectura del procesador RISC-V o no ha sido implementada. PC = " + str(int(self.programCounter - 4)))

        elif (4 != len(self.ir)):
            exito = False
            print("Cantidad incorrecta de parámetros para la instrucción " + str(self.ir[0]) + ": " + self.instructionSet[self.ir[0]] + ". PC = " + str(self.programCounter))

        elif 999 == self.ir[0] and (0 != self.ir[1] or 0 != self.ir[2] or 0 != self.ir[3]):
            exito = False
            print("Parámetros incorrectos para instrucción " + str(self.ir[0]) + ": " + self.instructionSet[self.ir[0]] + ". PC = " + str(self.programCounter)) +". Todos los parámetros deben de ser 0"

        elif 37 != self.ir[0] and 99 !=  self.ir[0] and 100 != self.ir[0] and 999 != self.ir[0] and 0 == self.ir[1]:
            exito = False
            print("El registro X0 es un registro destino inválido.")

        elif self.ir[0] == 5: # lw
            self.lw(self.ir[1], self.ir[2], self.ir[3])

        elif self.ir[0] == 19: # addi
            self.addi(self.ir[1], self.ir[2], self.ir[3])

        elif self.ir[0] == 37: # sw
            self.sw(self.ir[1], self.ir[2], self.ir[3])

        elif self.ir[0] == 56: # div
            self.div(self.ir[1], self.ir[2], self.ir[3])

        elif self.ir[0] == 71: # add
            self.add(self.ir[1], self.ir[2], self.ir[3])

        elif self.ir[0] == 72: # mul
            self.mul(self.ir[1], self.ir[2], self.ir[3])

        elif self.ir[0] == 83: # sub
            self.sub(self.ir[1], self.ir[2], self.ir[3])

        elif self.ir[0] == 99: # beq
            self.beq(self.ir[1], self.ir[2], self.ir[3])

        elif self.ir[0] == 100: # bne
            self.bne(self.ir[1], self.ir[2], self.ir[3])

        elif self.ir[0] == 103: # jalr
            self.jalr(self.ir[1], self.ir[2], self.ir[3])

        elif self.ir[0] == 111: # jal
            self.jal(self.ir[1], self.ir[3])

        elif self.ir[0] == 999: # FIN
            exito = 999

        return exito

    #Funcion que ejecuta la instrucción lw
    def lw(self, rd, rf1, desplazamiento):
        self.registros[rd] = self.cache.getDato(int(desplazamiento + self.registros[rf1]))
        #print("aqui", end='\n')
        self.cache.liberar_bus_datos()
        self.cache.liberarCacheDatos()

    # Función que ejecuta la operación addi, la cual suma el contenido de x2 con un inmediato y lo almacena en x1
    def addi(self, rd, rf, inmediato):
        self.registros[rd] = int(inmediato + self.registros[rf])

    # Funcion que ejecuta la instrucción sw
    def sw(self, rf1, rf2, desplazamiento):
        self.cache.setDato(int(desplazamiento + self.registros[rf1]), self.registros[rf2])

    # Función que ejecuta la operación add, la cual suma el contenido de x2 con x3 y lo almacena en x1
    def add(self, rd, rf1, rf2):
        self.registros[rd] = int(self.registros[rf1] + self.registros[rf2])

    # Función que ejecuta la operación sub, la cual resta el contenido de x2 con x3 y lo almacena en x1
    def sub(self, rd, rf1, rf2):
        self.registros[rd] = int(self.registros[rf1] - self.registros[rf2])

    # Función que ejecuta la operación mul, la cual multiplica el contenido de x2 con x3 y lo almacena en x1
    def mul(self, rd, rf1, rf2):
        self.registros[rd] = int(self.registros[rf1] * self.registros[rf2])

    # Función que ejecuta la operación div, la cual divide el contenido de x2 entre x3 y lo almacena en x1
    def div(self, rd, rf1, rf2):
        self.registros[rd] = int(self.registros[rf1] / self.registros[rf2])

    # Función que ejecuta la operación beq, la cual hace un branch modificando el pc con el tercer
    # parámetro, sumando este parametro * 4 y sumandolo al pc, en caso de que los primeros dos parámetros sean iguales
    def beq(self, rf1, rf2, etiq):
        if self.registros[rf1] == self.registros[rf2]:
            self.programCounter += int(etiq * 4)

    # Función que ejecuta la operación bne, la cual hace un branch modificando el pc con el tercer parámetro,
    # sumando este parametro * 4 y sumandolo al pc, en caso de que los primeros dos parámetros NO sean iguales
    def bne(self, rf1, rf2, etiq):
        if self.registros[rf1] != self.registros[rf2]:
            self.programCounter += int(etiq * 4)

    # Función que ejecuta la operación jal, la cual hace un jump, guardando el pc actual en un registro
    # especificado por el primer parámetro y modificandolo luego con el inmediato en el tercer parámetro
    def jal(self, rd, inmediato):
        self.registros[rd] = self.programCounter
        self.programCounter += inmediato

    # Función que ejecuta la operación jal, la cual hace un jump, guardando el pc actual en un registro
    # especificado por el primer parámetro y modificandolo luego con el inmediato en el tercer parámetro
    # sumado al valor en el registro especificado en el segundo parámetro
    def jalr(self, rd, rf1, inmediato):
        self.registros[rd] = self.programCounter
        self.programCounter = self.registros[rf1] + inmediato

    def setRegistros(self, registros):
        self.registros = registros

    def getRegistros(self):
        return self.registros

    def setProgramCounter(self, pc):
        self.programCounter = pc

    def getProgramCounter(self):
        return self.programCounter

