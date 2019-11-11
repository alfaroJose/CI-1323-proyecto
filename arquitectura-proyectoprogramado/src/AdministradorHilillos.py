import os
import threading
from MemoriaPrincipal import MemoriaPrincipal
from TCB import TCB
from Cache import Cache

# ------------------------ DEFINICION DE VARIABLES Y FUNCIONES -----------------------------------
#Método que lee todos los archivos .txt que estén presentes en el directorio
#donde se corre el programa sin importar los subdirectorios que tenga y devuelve un
#arreglo con las dirrecciones a cada uno de estos archivos
def leerHilillos():
    print("Nombre del directorio:")
    path, filename = os.path.split(__file__)
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
tcb.imprimir()

# if memoriaPrincipal.bloquearBusDatos():
#     print("Bus de datos bloqueado")
# else:
#     print("No fue posible bloquear el bus de datos");
#
# if memoriaPrincipal.liberarBusDatos():
#     print("Bus de datos liberado")
# else:
#     print("No fue posible liberar el bus de datos");

# if memoriaPrincipal.bloquearBusInstrucciones():
#     print("Bus de instrucciones bloqueado")
# else:
#     print("No fue posible bloquear el bus de instrucciones");
#
# if memoriaPrincipal.liberarBusInstrucciones():
#     print("Bus de instrucciones liberado")
# else:
#     print("No fue posible liberar el bus de instrucciones");


# memoriaPrincipal.guardarDato(380, 380)
#print(memoriaPrincipal.leerDato(380))
#memoriaPrincipal.guardarInstrucciones("999 999 999 999", 388)
#memoriaPrincipal.guardarDato(80,384)
#memoriaPrincipal.imprimirMemoria()
#print(memoriaPrincipal.leerInstrucciones(384))
#memoriaPrincipal.imprimirAreaDatos()
#memoriaPrincipal.imprimirAreaInstrucciones()
#memoriaPrincipal.imprimirMemoria()

#tcb = TCB()
#tcb.agregarHilillo("0")
#tcb.imprimir()

#cache = Cache(memoriaPrincipal)
#cache.imprimirCacheDatos()
#cache.imprimirCacheInstrucciones()
#cache.getDato(132);
#cache.imprimirCacheDatos()
#print(cache.getInstruccion(404))
#cache.imprimirCacheInstrucciones()
#print(memoriaPrincipal.leerBloqueDatos(380))
#print(memoriaPrincipal.leerBloqueInstrucciones(1004))
