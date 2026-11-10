def productoMasCaro(productos):
    with open(productos, "r") as columna:
        mayor = 0
        for linea in columna:
            filas = linea.strip().split(",")
            precios = int(filas[2])
            
            if mayor < precios:
                mayor = precios
                nomProducto = filas[1]
        
        return f"El producto de mayor valores es {nomProducto}"
