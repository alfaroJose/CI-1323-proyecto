from AreaInstrucciones import AreaInstrucciones
from AreaDatos import AreaDatos

#Clase para representar la memoria principal compartida del procesador
class MemoriaPrincipal:

    def __init__(self):
        self.areaDatos = AreaDatos()
        self.areaInstrucciones = AreaInstrucciones()

    #Método para imprimir el contenido de la memoria principal
    def imprimirMemoria(self):
        print("Área de datos:")
        self.areaDatos.imprimir(self.areaInstrucciones.tamanoMaximo())
        print()
        print("Área de instrucciones:")
        self.areaInstrucciones.imprimir(self.areaDatos.tamanoMaximo())
