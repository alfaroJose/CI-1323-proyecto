#Clase para representar el area de datos de la memoria principal
class AreaDatos:

    def __init__(self):
        self.datos = []
        self.llenar()

    #Método para guardar un dato en el arreglo de datos
    #Se recibe el dato nuevo a guardar y la posición donde se desea guardar en el arreglo de datos
    def guardarDato(self, dato, posicion):
        #La posicion se divide entre 4 debido a que el arreglo comienza en 0 lógicamente
        self.datos[posicion] = dato

    #Función para leer un dato del arreglo de datos
    #Se rebibe la posición donde esta guardado el dato que se desea leer en el arreglo de datos
    def leerDato(self, posicion):
        #La posicion se divide entre 4 debido a que el arreglo comienza en 0 lógicamente
        return self.datos[int(posicion/4)]

    #función para leer un bloque
    def leerBloque(self, direccionFisica):
        bloque = []
        # La posicion se divide entre 4 debido a que el arreglo comienza en 0 lógicamente y costa de 4 elementos
        numBloque = int(direccionFisica / 4) #Dado que cada bloque consta de 4 palabras y el primero es el 0
        dirInicialBloque = numBloque * 4 #Dirección física inicial del bloque
        for x in range(dirInicialBloque, dirInicialBloque + 4):
            bloque.append(self.datos[x])
        return bloque

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
        for y in self.datos:
            if x % 64 == 0 and x != 0:
                print()
            print(y, end=self.calcularRelleno(y, tamanoMaximo))
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