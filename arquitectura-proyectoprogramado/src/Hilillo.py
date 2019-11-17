# Clase para guardar la información de un hilillo
class Hilillo:

    def __init__(self, identificador):
        self.identificador = identificador
        self.estado = 0
        self.nucleo = None
        self.direccion = -1
        self.reloj = 0 # Almacena el número de ciclo en el que el hilillo terminó
        self.registros = []
        for i in range(32):
            self.registros.append(0)

    def getIdentificador(self):
        return self.identificador

    #Cambia el estado de un hilillo, 0 para no usado, 1 para usado y 2 para terminado.
    def setEstado(self, estado):
        self.estado = estado

    def getEstado(self):
        return self.estado

    # Guarda el número de núcleo que lo ejecutará
    def setNucleo(self, nucleo):
        self.nucleo = nucleo

    def getNucleo(self):
        return self.nucleo

    def setDireccion(self, direccion):
        self.direccion = direccion

    def getDireccion(self):
        return self.direccion

    def setReloj(self, reloj):
        self.reloj = reloj

    #Calcula los ciclos de reloj que tardo ejecutandose el hilillo y lo almacena en reloj
    def calcularCiclosDeReloj(self, reloj):
        self.reloj = reloj - self.reloj

    def getReloj(self):
        return self.reloj

    def setRegistros(self, registros):
        self.registros = registros

    def getRegistros(self):
        return self.registros

    def imprimir(self):
        print(self.identificador, end=' ')
        print(self.nucleo, end='      ')
        print(self.estado, end='    ')
        print(self.direccion, end=' ')
        print(self.reloj, end='      ')
        for i in range(32):
            if i == 31:
                print(self.registros[i])
            else:
                print(self.registros[i], end=',')

