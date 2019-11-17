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
            if h.getEstado() == 0:
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
        for hilillo in self.tcb:
            hilillo.imprimir()
