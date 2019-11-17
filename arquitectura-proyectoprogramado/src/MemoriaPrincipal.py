from AreaInstrucciones import AreaInstrucciones
from AreaDatos import AreaDatos
from threading import RLock

#Clase para representar la memoria principal compartida del procesador
class MemoriaPrincipal:

    def __init__(self):
        self.areaDatos = AreaDatos()
        self.areaInstrucciones = AreaInstrucciones()
        self.busDatos = RLock()
        self.busInstrucciones = RLock()

    #Método para guardar un dato en memoria principal
    #Se recibe el dato nuevo a guardar y la posición donde se desea guardar en memoria
    def guardarDato(self, dato, posicion):
        if posicion >= 0 and posicion <= 95:
            #print(dato, "::", posicion * 4, end='\n')
            self.areaDatos.guardarDato(dato, posicion)
        else:
            print("sw: la dirección de memoria: " + str(int(posicion * 4)) + " es inválida")

    #Función para leer un dato de memoria
    #Se rebibe la posición donde esta guardado el dato que se desea leer en memoria
    def leerDato(self, posicion):
        if posicion >= 0 and posicion <= 380:
            return self.areaDatos.leerDato(posicion)
        else:
            print("La posicion: " + str(posicion) + " es invalida para leer en el area de datos")

    def leerBloqueDatos(self, direccionFisica):
        bloque = []
        if direccionFisica >= 0 and direccionFisica <= 95:
            bloque = self.areaDatos.leerBloque(direccionFisica)
        else:
            print("La posicion: " + str(int(direccionFisica * 4)) + " no existe en el área de datos")
        return bloque

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
            return self.areaInstrucciones.leerInstrucciones(posicion)
        else:
            print("La posicion: " + str(posicion) + " es invalida para leer en el area de instrucciones")

    def leerBloqueInstrucciones(self, posicion):
        bloque = []
        if posicion >= 384 and posicion <= 1020:
            bloque = self.areaInstrucciones.leerBloqueInstrucciones(posicion)
        else:
            print("La posicion: " + str(posicion) + " no existe en el área de instrucciones")
        return bloque

    #Método que le permite a las cachés intentar un bloqueo del bus de datos
    def bloquearBusDatos(self):
        return self.busDatos.acquire(False) # Con False, el método no bloquea la ejecución, esto para evitar Deadlocks

    # Método que le permite a las cachés bloquear el bus de instrucciones
    def bloquearBusInstrucciones(self):
            return self.busInstrucciones.acquire()  # Con False, el método no bloquea la ejecución, esto para evitar Deadlocks

    #Método que le permite a las cachés liberar el bus de datos
    def liberarBusDatos(self):
        liberado = True
        try:
            self.busDatos.release()
            #self.busDatos.release()
        except:
            liberado = False
        return liberado

    # Método que le permite a las cachés liberar el bus de instrucciones
    def liberarBusInstrucciones(self):
        liberado = True
        try:
            self.busInstrucciones.release()
            #self.busInstrucciones.release()
        except:
            liberado = False
        return liberado

    #Método para imprimir el contenido de la memoria principal
    def imprimirMemoria(self):
        print("Área de datos")
        self.areaDatos.imprimir(self.areaInstrucciones.tamanoMaximo())
        print()
        print("Área de instrucciones")
        self.areaInstrucciones.imprimir(self.areaDatos.tamanoMaximo())
        print()

    def imprimirAreaDatos(self):
        self.areaDatos.imprimir(0)
        print()

    def imprimirAreaInstrucciones(self):
        self.areaInstrucciones.imprimir(0)
        print()
