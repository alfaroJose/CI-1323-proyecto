import os
import threading
from MemoriaPrincipal import MemoriaPrincipal
from TCB import TCB
from Procesador import Procesador

# ------------------------ DEFINICION DE VARIABLES Y FUNCIONES -----------------------------------
#Método que lee todos los archivos .txt que estén presentes en el directorio
#donde se corre el programa sin importar los subdirectorios que tenga y devuelve un
#arreglo con las dirrecciones a cada uno de estos archivos
def leerHilillos():
    print("Nombre del directorio de hilillos:")
    path, filename = os.path.split(__file__)
    path += "/hilillos"
    print(path)

    files = []
    #r = raiz, d = directorios, f = archivos
    for r, d, f in os.walk(path):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))

    print("Lista de hilillos:")
    for f in files:
        print(f)

    return files

#Método que recibe un arreglo de direcciones hacía hilillos con instrucciones válidas
#para el programa y las carga al área de instrucciones de memoria principal
#además carga los hilillos en el tcb
def cargarHilillos(hilillos, memoriaPrincipal, tcb):
    posicion = 384
    for hilillo in hilillos:
        file = open(hilillo, "r")
        nombre = os.path.basename(file.name).split('.')[0]
        tcb.agregarHilillo(nombre)
        tcb.modificarDireccionHilillo(nombre, posicion)
        for f in file:
            memoriaPrincipal.guardarInstrucciones(list(map(int, f.strip().split(' '))), posicion)
            posicion += 4
        file.close()


# ------------------------- PROGRAMA ------------------------------------------------------------

memoriaPrincipal = MemoriaPrincipal()
tcb = TCB()
cargarHilillos(leerHilillos(), memoriaPrincipal, tcb)
procesador = Procesador(memoriaPrincipal, tcb)
print("Área de datos:")
memoriaPrincipal.imprimirAreaDatos()
print(end='\n')
print("Estado final de las cachés de datos:")
procesador.imprimirCachesDatos()
print("Información del TCB:")
tcb.imprimir()

