#Clase para representar el area de instrucciones de la memoria principal
class AreaInstrucciones:

    def __init__(self):
        self.instrucciones = []
        self.llenar()

    #Método para guardar una instrucción en el arreglo de instrucciones
    #Se recibe un arreglo con las 4 partes de una instrucción y la posicion en la que será guardada
    #Las instrucciones se guardan como una hilera seprarando cada componente de la instrucción por un espacio en blanco
    def guardarInstrucciones(self, instrucciones, posicion):
        #La posicion se divide entre 4 debido a que el arreglo comienza en 0 lógicamente y se le resta 96 ya
        #que las direcciones de instrucciones van a comenzar enviandose desde 380 (380/4 = 96)
        self.instrucciones[int(posicion/4)-96] = instrucciones


    #Función para leer un bloque de instrucciones del arreglo de instrucciones
    #Se recibe la posición donde están almacenadas las 4 partes de la instrucción
    #Las instrucciones se leen como una hilera con sus componentes separados por un espacio en blanco
    def leerInstrucciones(self, posicion):
        #La posicion se divide entre 4 debido a que el arreglo comienza en 0 lógicamente y se le resta 96 ya
        #que las direcciones de instrucciones van a comenzar enviandose desde 380 (380/4 = 96)
        return self.instrucciones[int(posicion/4)-96]

    #Método que inicializa el arreglo de instrucciones con números del 384 al 1020 con incrementos de 4 en 4
    def llenar(self):
        x = 384
        while x < 1024:
            self.instrucciones.append(x)
            x += 4

    #Método para imprimir el contenido del area de instrucciones de la memoria principal
    def imprimir(self, maximo):
        x = 384
        tamanoMaximo = self.tamanoMaximo()
        if maximo > tamanoMaximo:
            tamanoMaximo = maximo
        for y in self.instrucciones:
            if x % 64 == 0 and x != 384:
                print()
            print(y, end=self.calcularRelleno(y, tamanoMaximo))
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