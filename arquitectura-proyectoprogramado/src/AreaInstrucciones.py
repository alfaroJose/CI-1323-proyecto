#Clase para representar el area de instrucciones de la memoria principal
class AreaInstrucciones:

    def __init__(self):
        self.instrucciones = []
        self.llenar()

    #Método que inicializa el arreglo de instrucciones con números del 384 al 1020 con incrementos de 4 en 4
    def llenar(self):
        x = 384
        while x < 1024:
            self.instrucciones.append(x)
            x += 4

    #Método para imprimir el contenido del area de instrucciones de la memoria principal
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

    #Función que retorna la cantidad de digitos del número con más digitos en el arreglo de instrucciones
    def tamanoMaximo(self):
        tamanoMaximo = 0
        for x in self.instrucciones:
            if len(str(x)) > tamanoMaximo:
                tamanoMaximo = len(str(x))
        return tamanoMaximo

    #Función que devulve la cantidad de espacios necesaria por cada número para que cuando se
    #imprima mantenga un buen formato
    def calcularRelleno(self, numero, tamanoMaximo):
        relleno = " "
        for x in range(len(str(numero)), tamanoMaximo):
            relleno += " "
        return relleno