import os
from MemoriaPrincipal import MemoriaPrincipal

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
def cargarHilillos(hilillos, memoriaPrincipal):
    posicion = 384
    for hilillo in hilillos:
        file = open(hilillo, "r")
        for f in file:
            memoriaPrincipal.guardarInstrucciones(f.strip(), posicion)
            posicion += 4
        file.close()



# ------------------------- PROGRAMA ------------------------------------------------------------

memoriaPrincipal = MemoriaPrincipal()
memoriaPrincipal.guardarDato(69, 380)
print(memoriaPrincipal.leerDato(380))
memoriaPrincipal.guardarInstrucciones("999 999 999 999",384)
#memoriaPrincipal.guardarInstrucciones("37 0 0 128",388)
#memoriaPrincipal.guardarInstrucciones("37 0 0 132",392)
#memoriaPrincipal.guardarInstrucciones("37 0 0 136",396)
#memoriaPrincipal.guardarInstrucciones("37 0 0 140",400)
#memoriaPrincipal.guardarInstrucciones("37 0 0 144",404)
#memoriaPrincipal.guardarInstrucciones("37 0 0 148",408)
#memoriaPrincipal.guardarInstrucciones("999 0 0 0",412)
memoriaPrincipal.guardarDato(80,384)
memoriaPrincipal.imprimirMemoria()
print(memoriaPrincipal.leerInstrucciones(384))
#memoriaPrincipal.imprimirAreaDatos()
#memoriaPrincipal.imprimirAreaInstrucciones()
cargarHilillos(leerHilillos(), memoriaPrincipal)
memoriaPrincipal.imprimirMemoria()
