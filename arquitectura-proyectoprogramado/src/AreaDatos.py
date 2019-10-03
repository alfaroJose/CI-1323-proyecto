#Clase para representar el area de datos de la memoria principal
class AreaDatos:

    def __init__(self):
        self.datos = []
        self.llenar()

    #Método para guardar un dato en el arreglo de datos
    #Se recibe el dato nuevo a guardar y la posición donde se desea guardar en el arreglo de datos
    def guardarDato(self, dato, posicion):
        self.datos[posicion] = dato

    #Función para leer un dato del arreglo de datos
    #Se rebibe la posición donde esta guardado el dato que se desea leer en el arreglo de datos
    def leerDato(self, posicion):
        return self.datos[posicion]

    #Método que inicializa el arreglo de datos con números del 0 al 380 con incrementos de 4 en 4
    def llenar(self):
        x = 0
        while x < 384:
            self.datos.append(x)
            x += 4

    #Método para imprimir el contenido del area de datos de la memoria principal
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

    #Función que retorna la cantidad de digitos del número con más digitos en el arreglo de datos
    def tamanoMaximo(self):
        tamanoMaximo = 0
        for x in self.datos:
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