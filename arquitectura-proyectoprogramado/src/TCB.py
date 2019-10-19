from Hilillo import Hilillo

#Clase para administrar hilillos
class TCB:

    def __init__(self):
        self.tcb = []
        self.numHilillo = 0

    #Agrega un hilillo al TCB
    def agregarHilillo(self, identificador):
        hilillo = Hilillo(identificador)
        self.tcb.append(hilillo)

    #Pide un hilillo que este sin usar al TCB
    def pedirHilillo(self, reloj):
        return 0

    #Imprime los datos de cada hilillo en el TCB
    def imprimir(self):
        for hilillo in self.tcb:
            hilillo.imprimir()
