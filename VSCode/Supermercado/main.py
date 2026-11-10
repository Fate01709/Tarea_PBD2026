import funciones

with open("informe.txt", "a") as informe:
    informe.write(str(funciones.productoMasCaro("productos.csv")) + "\n")
    informe.write(str(funciones.valorTotalBodega("productos.csv")) + "\n")
    informe.write(str(funciones.productoConMasIngresos("items.csv", "productos.csv")) + "\n")