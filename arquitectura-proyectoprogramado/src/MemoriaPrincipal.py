from AreaInstrucciones import AreaInstrucciones
from AreaDatos import AreaDatos


class MemoriaPrincipal:

    def __init__(self):
        self.areaDatos = AreaDatos()
        self.areaInstrucciones = AreaInstrucciones()

    def imprimirMemoria(self):
        print("Área de datos:")
        self.areaDatos.imprimir(self.areaInstrucciones.tamanoMaximo())
        print()
        print("Área de instrucciones:")
        self.areaInstrucciones.imprimir(self.areaDatos.tamanoMaximo())
