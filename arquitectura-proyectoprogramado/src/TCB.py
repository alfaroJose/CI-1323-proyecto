from Hilillo import Hilillo

#Clase para administrar hilillos
class TCB:

    def __init__(self):
        self.tcb = []

    #Agrega un hilillo al TCB
    def agregarHilillo(self, identificador):
        hilillo = Hilillo(identificador)
        self.tcb.append(hilillo)

    #Pide un hilillo que este sin usar al TCB
    #Devuelve el hilillo sin usar o None en caso de que ya no queden disponibles
    def pedirHilillo(self, reloj):
        for hilillo in self.tcb:
            if hilillo.estado == 0:
                hilillo.setEstado(1)
                return hilillo
            else:
                return None

    #Modifica un hilillo ya agregado
    #Se usa para cuando se lee una instruccion fin
    def modificarHilillo(self, modificado):
        for hilillo in self.tcb:
            if hilillo.identificador == modificado.identificador:
                hilillo.setEstado(2)
                hilillo.setReloj(modificado.getReloj)
                hilillo.setRegistros(modificado.getRegistros())

    #Imprime los datos de cada hilillo en el TCB
    def imprimir(self):
        for hilillo in self.tcb:
            hilillo.imprimir()
