from Hilillo import Hilillo
from threading import RLock

#Clase para administrar hilillos
class TCB:

    def __init__(self):
        self.tcb = []
        self.candadoTCB = RLock()

    #Agrega un hilillo al TCB
    def agregarHilillo(self, identificador):
        hilillo = Hilillo(identificador)
        self.tcb.append(hilillo)

    #Pide un hilillo que este sin usar al TCB
    #Devuelve el hilillo sin usar o None en caso de que ya no queden disponibles
    def pedirHilillo(self, nucleo):
        hilillo = None
        self.candadoTCB.acquire()
        for h in self.tcb:
            if h.getEstado() == -1:
                h.setEstado(nucleo)
                h.setNucleo(nucleo)
                hilillo = h
                break
        self.candadoTCB.release()
        return hilillo


    #Metodo que modifica la dirección de un hilillo en el tcb
    #Recibe el identificador del hilillo y la dirección donde esta ubicado
    #en memoria principal area de instrucciones
    def modificarDireccionHilillo(self, identificador, direccion):
        for hilillo in self.tcb:
            if hilillo.getIdentificador() == identificador:
                hilillo.setDireccion(direccion)

    # Metodo que modifica el estado de un hilillo en el tcb
    # Recibe el identificador del hilillo y el estado nuevo del hilillo
    def modificarEstadoHilillo(self, identificador, estado):
        for hilillo in self.tcb:
            if hilillo.getIdentificador() == identificador:
                hilillo.setEstado(estado)

    # Metodo que modifica los registros de un hilillo en el tcb
    # Recibe el identificador del hilillo y los nuevos registros del hilillo
    def modificarRegistrosHilillo(self, identificador, registros):
        for hilillo in self.tcb:
            if hilillo.getIdentificador() == identificador:
                hilillo.setRegistros(registros)
                break

    # Metodo que modifica el reloj de un hilillo en el tcb
    # Recibe el identificador del hilillo y el nuevo reloj del hilillo
    def modificarRelojHilillo(self, identificador, reloj):
        for hilillo in self.tcb:
            if hilillo.getIdentificador() == identificador:
                hilillo.setReloj(reloj)

    # Método que retorna la direccion de un hilllo en tcb
    # Recibe el identificador del hilillo
    def obtenerDireccionHilillo(self, identificador):
        for hilillo in self.tcb:
            if hilillo.getIdentificador() == identificador:
                return hilillo.getDireccion()

    # Método que retorna los registros de un hilllo en tcb
    # Recibe el identificador del hilillo
    def obtenerRegistrosHilillo(self, identificador):
        for hilillo in self.tcb:
            if hilillo.getIdentificador() == identificador:
                return hilillo.getRegistros()

    # Método que retorna el reloj de un hilllo en tcb
    # Recibe el identificador del hilillo
    def obtenerRelojHilillo(self, identificador):
        for hilillo in self.tcb:
            if hilillo.getIdentificador() == identificador:
                return hilillo.getReloj()

    #Imprime los datos de cada hilillo en el TCB
    def imprimir(self):
        relleno = 0
        print("Id", end= self.calcularRellenoID(self.maxID()))
        print("Núcleo", end=self.calcularRellenoNucleo(self.maxNucleo()))
        print("Estado", end=self.calcularRellenoEstado(self.maxEstado()))
        print("Dirección", end=self.calcularRellenoDireccion(self.maxDireccion()))
        print("Reloj", end=self.calcularRellenoReloj(self.maxReloj()))
        print("Registros")
        for hilillo in self.tcb:
            print(hilillo.getIdentificador(), end=self.calcularRellenoIDDato(self.maxID()))
            print(hilillo.getNucleo(), end=self.calcularRellenoNucleoDato(self.maxNucleo()))
            print(hilillo.getEstado(), end=self.calcularRellenoEstadoDato(self.maxEstado()))
            print(hilillo.getDireccion(), end=self.calcularRellenoDireccionDato(self.maxDireccion()))
            print(hilillo.getReloj(), end=self.calcularRellenoRelojDato(self.maxReloj()))
            r = hilillo.getRegistros()
            for i in range(32):
                if i == 31:
                    print("X" + str(i) + "=" + str(r[i]))
                else:
                    print("X" + str(i) + "=" + str(r[i]), end=' ')

    def maxID(self):
        max = 0
        for hilillo in self.tcb:
            if hilillo.sizeID() > max:
                max = hilillo.sizeID()
        return max

    def calcularRellenoID(self, max):
        relleno = " "
        if max > 2:
            for x in range(2, max):
                relleno += " "
        return relleno

    def calcularRellenoIDDato(self, max):
        relleno = " "
        if max < 2:
            relleno = "  "
        return relleno

    def maxNucleo(self):
        max = 0
        for hilillo in self.tcb:
            if hilillo.sizeID() > max:
                max = hilillo.sizeNucleo()
        return max

    def calcularRellenoNucleo(self, max):
        relleno = " "
        return relleno

    def calcularRellenoNucleoDato(self, max):
        relleno = "      "
        return relleno

    def maxEstado(self):
        max = 0
        for hilillo in self.tcb:
            if hilillo.sizeID() > max:
                max = hilillo.sizeEstado()
        return max

    def calcularRellenoEstado(self, max):
        relleno = "         "
        if max < 2:
            relleno = " "
        return relleno

    def calcularRellenoEstadoDato(self, max):
        relleno = " "

        return relleno

    def maxDireccion(self):
        max = 0
        for hilillo in self.tcb:
            if hilillo.sizeID() > max:
                max = hilillo.sizeDireccion()
        return max

    def calcularRellenoDireccion(self, max):
        relleno = " "

        return relleno

    def calcularRellenoDireccionDato(self, max):
        relleno = "       "

        return relleno

    def maxReloj(self):
        max = 0
        for hilillo in self.tcb:
            if hilillo.sizeID() > max:
                max = hilillo.sizeReloj()
        return max

    def calcularRellenoReloj(self, max):
        relleno = " "

        return relleno

    def calcularRellenoRelojDato(self, max):
        relleno = "    "

        return relleno