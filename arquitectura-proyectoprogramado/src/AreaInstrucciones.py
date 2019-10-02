class AreaInstrucciones:

    def __init__(self):
        self.instrucciones = []
        self.llenar()

    def llenar(self):
        x = 384
        while x < 1024:
            self.instrucciones.append(x)
            x += 4

    def imprimir(self, maximo):
        x = 0
        tamanoMaximo = self.tamanoMaximo()
        if maximo > tamanoMaximo:
            tamanoMaximo = maximo
        for x in self.instrucciones:
            if x % 64 == 0 and x != 384:
                print()
            print(x, end=self.calcularRelleno(x, tamanoMaximo))
            x += 4

    def tamanoMaximo(self):
        tamanoMaximo = 0
        for x in self.instrucciones:
            if len(str(x)) > tamanoMaximo:
                tamanoMaximo = len(str(x))
        return tamanoMaximo

    def calcularRelleno(self, numero, tamanoMaximo):
        relleno = " "
        for x in range(len(str(numero)), tamanoMaximo):
            relleno += " "
        return relleno