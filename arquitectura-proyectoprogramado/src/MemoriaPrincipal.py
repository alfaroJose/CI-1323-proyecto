from AreaInstrucciones import AreaInstrucciones
from AreaDatos import AreaDatos

#Clase para representar la memoria principal compartida del procesador
class MemoriaPrincipal:

    def __init__(self):
        self.areaDatos = AreaDatos()
        self.areaInstrucciones = AreaInstrucciones()

    #Método para guardar un dato en memoria principal
    #Se recibe el dato nuevo a guardar y la posición donde se desea guardar en memoria
    def guardarDato(self, dato, posicion):
        if posicion >= 0 and posicion <= 380:
            self.areaDatos.guardarDato(dato, posicion)
        else:
            print("La posicion: " + str(posicion) + " es invalida para guardar en el area de datos")

    #Función para leer un dato de memoria
    #Se rebibe la posición donde esta guardado el dato que se desea leer en memoria
    def leerDato(self, posicion):
        if posicion >= 0 and posicion <= 380:
            self.areaDatos.leerDato(posicion)
        else:
            print("La posicion: " + str(posicion) + " es invalida para leer en el area de datos")

    #Método para guardar una instrucción en memoria
    #Se recibe un arreglo con las 4 partes de una instrucción y la posicion en la que será guardada
    def guardarInstrucciones(self, instrucciones, posicion):
        if posicion >= 384 and posicion <= 1020:
            self.areaInstrucciones.guardarInstrucciones(instrucciones, posicion)
        else:
            print("La posicion: " + str(posicion) + " es invalida para guardar en el area de instrucciones")

    #Función para leer un bloque de instrucciones de memoria
    #Se recibe la posición donde están almacenadas las 4 partes de la instrucción
    def leerInstrucciones(self, posicion):
        if posicion >= 384 and posicion <= 1020:
            self.areaInstrucciones.leerInstrucciones(posicion)
        else:
            print("La posicion: " + str(posicion) + " es invalida para leer en el area de instrucciones")

    #Método para imprimir el contenido de la memoria principal
    def imprimirMemoria(self):
        print("Área de datos:")
        self.areaDatos.imprimir(self.areaInstrucciones.tamanoMaximo())
        print()
        print("Área de instrucciones:")
        self.areaInstrucciones.imprimir(self.areaDatos.tamanoMaximo())
