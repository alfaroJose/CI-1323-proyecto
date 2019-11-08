#Clase para representar el area de datos de la memoria principal
class AreaDatos:

    def __init__(self):
        self.datos = []
        self.llenar()

    #Método para guardar un dato en el arreglo de datos
    #Se recibe el dato nuevo a guardar y la posición donde se desea guardar en el arreglo de datos
    def guardarDato(self, dato, posicion):
        #La posicion se divide entre 4 debido a que el arreglo comienza en 0 lógicamente
        self.datos[int(posicion/4)] = dato

    #Función para leer un dato del arreglo de datos
    #Se rebibe la posición donde esta guardado el dato que se desea leer en el arreglo de datos
    def leerDato(self, posicion):
        #La posicion se divide entre 4 debido a que el arreglo comienza en 0 lógicamente
        return self.datos[int(posicion/4)]

    def leerBloque(self, posicion):
        #La posicion se divide entre 4 debido a que el arreglo comienza en 0 lógicamente
        bloque = []
        if posicion >= 0 and posicion <= 380:
            direccionFisica = int(posicion / 4)
            numBloque = int(direccionFisica / 4)
            dirInicialBloque = numBloque * 4
            for x in range(dirInicialBloque, dirInicialBloque + 4):
                bloque.append(self.datos[x])
        else:
            print("La posicion: " + str(posicion) + " es inválida para leer en el area de datos")
        return bloque

    #Función para guardar un bloque
    def guardarBloqueDatos(self, posicion):
        return 1

    #función para leer un bloque

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