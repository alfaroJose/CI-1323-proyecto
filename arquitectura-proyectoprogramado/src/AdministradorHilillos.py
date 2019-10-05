from MemoriaPrincipal import MemoriaPrincipal

# ------------------------ DEFINICION DE VARIALES Y FUNCIONES -----------------------------------

# ------------------------- PROGRAMA ------------------------------------------------------------

memoriaPrincipal = MemoriaPrincipal()
memoriaPrincipal.guardarDato(69, 380)
print(memoriaPrincipal.leerDato(380))
memoriaPrincipal.guardarInstrucciones("0 0 0 0",380)
memoriaPrincipal.guardarDato(80,384)
memoriaPrincipal.imprimirMemoria()
print(memoriaPrincipal.leerInstrucciones(384))
print(memoriaPrincipal.leerInstrucciones(388))
memoriaPrincipal.imprimirAreaDatos()
memoriaPrincipal.imprimirAreaInstrucciones()

