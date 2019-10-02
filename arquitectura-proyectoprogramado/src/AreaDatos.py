class AreaDatos:

    def __init__(self):
        self.datos = []
        self.llenar()

    def llenar(self):
        x = 0
        while x < 384:
            self.datos.append(x)
            x += 4

    def imprimir(self, maximo):
        x = 0
        tamanoMaximo = self.tamanoMaximo()
        if maximo > tamanoMaximo:
            tamanoMaximo = maximo
        for x in self.datos:
            if x % 64 == 0 and x != 0:
                print()
            print(x, end=self.calcularRelleno(x, tamanoMaximo))
            x += 4

    def tamanoMaximo(self):
        tamanoMaximo = 0
        for x in self.datos:
            if len(str(x)) > tamanoMaximo:
                tamanoMaximo = len(str(x))
        return tamanoMaximo

    def calcularRelleno(self, numero, tamanoMaximo):
        relleno = " "
        for x in range(len(str(numero)), tamanoMaximo):
            relleno += " "
        return relleno