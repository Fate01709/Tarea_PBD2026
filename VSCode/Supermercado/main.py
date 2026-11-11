import funciones

with open("informe.txt", "w") as informe:
    informe.write(str(funciones.productoMasCaro("productos.csv")) + "\n")
    informe.write(str(funciones.valorTotalBodega("productos.csv")) + "\n")
    informe.write(str(funciones.productoConMasIngresos("items.csv", "productos.csv")) + "\n")
    informe.write(str(funciones.TotalVentasDelMes("10", "2010", "items.csv", "productos.csv", "ventas.csv")) + "\n")
