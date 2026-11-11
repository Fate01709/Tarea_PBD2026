import csv

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

def valorTotalBodega(productos):
    with open(productos, "r") as columna:
        total = 0
        for linea in columna:
            filas = linea.strip().split(",")
            valorP = int(filas[2]) * int(filas[3])
            total += valorP
        
    return f"El valor total de la bodega es {total}"

def productoConMasIngresos(items, productos):
    ventas = {}
    with open(items, "r") as idVentas:
        for linea in idVentas:
            filas = linea.strip().split(";")
            id_prod = filas[1]
            cantidad = int(filas[2])
          
            if id_prod in ventas:
                ventas[id_prod] += cantidad
            else:
                ventas[id_prod] = cantidad
    precios = {}

    with open(productos, "r") as idProductos:
        nombres = {}
        for lineas in idProductos:
            fila = lineas.strip().split(",")
            precios[fila[0]] = int(fila[2])
            nombres[fila[0]] = fila[1]
    ventas_total = {}
    
    for id_producto in ventas:
        nombres
        cantidad = ventas[id_producto]
        precio = precios[id_producto]
        ventas_total[id_producto] = cantidad * precio
    
    idpro = max(ventas_total, key=ventas_total.get)

    return f"El producto con más ingresos es: {nombres[idpro]}"

def TotalVentasDelMes(mes, año, items, productos, ventas):
    total_mes = 0                                       
    num_boleta = []                                     
    with open(ventas, "r") as ventas_archivo: 
        lector = csv.reader(ventas_archivo, delimiter=";") 
        for linea in lector:                            
            partes_fecha = linea[1].split("-")          
            mes_searching = partes_fecha[1]             
            año_searching = partes_fecha[2]             
            if int(mes_searching) == int(mes) and int(año_searching) == int(año): 
                num_boleta.append(linea[0])               
    producto_vendido = {}                               
    with open(items, "r") as items_archivo: 
        lector_items = csv.reader(items_archivo, delimiter=";") 
        for linea in lector_items:                      
            if linea[0] in num_boleta:                  
                id_producto = linea[1]                  
                cantidad = int(linea[2])                  
                if id_producto in producto_vendido:       
                    producto_vendido[id_producto] += cantidad 
                else:                                   
                    producto_vendido[id_producto] = cantidad 
    with open(productos, "r") as productos_archivo: 
        lector_productos = csv.reader(productos_archivo) 
        for linea in lector_productos:                  
            id_producto_archivo = linea[0]              
            if id_producto_archivo in producto_vendido: 
                precio = int(linea[2])                  
                cantidad = producto_vendido[id_producto_archivo] 
                venta_producto = precio * cantidad      
                total_mes += venta_producto                     
    return f"Las ventas totales del mes son: {total_mes}"