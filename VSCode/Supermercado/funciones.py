def productoMasCaro(productos):
    with open(productos, "r") as columna:
        mayor = 0
        for linea in columna:
            filas = linea.strip().split(",") #Lee el archivo 
            precios = int(filas[2]) #Guarda en una variable el precio del producto
            
            if mayor < precios:
                mayor = precios
                nomProducto = filas[1] #Compara el precio con el del ultimo producto comparado y lo guardo si es mayor.
    
    return f"El producto de mayor valores es {nomProducto}"

def valorTotalBodega(productos):
    with open(productos, "r") as columna:
        total = 0
        for linea in columna:
            filas = linea.strip().split(",")
            valorP = int(filas[2]) * int(filas[3]) #Multiplica el valor por la cantidad en bodega.
            total += valorP #Lo suma con el valor anterior y lo guarda.
        
    return f"El valor total de la bodega es {total}"

def productoConMasIngresos(items, productos):
    ventas = {}
    with open(items, "r") as idVentas:
        for linea in idVentas:
            filas = linea.strip().split(";")
            id_prod = filas[1] #Guarda en una variable el ID del producto
            cantidad = int(filas[2]) #Guarda en una variable la cantidad vendida del producto
          
            if id_prod in ventas:
                ventas[id_prod] += cantidad
            else:
                ventas[id_prod] = cantidad #Revisa si hay elementos repetidos
    
    precios = {}
    with open(productos, "r") as idProductos:
        nombres = {}
        for lineas in idProductos:
            fila = lineas.strip().split(",")
            precios[fila[0]] = int(fila[2]) #Guarda en un diccionario los precios con el ID como identificador
            nombres[fila[0]] = fila[1] #Guarda en un diccionario los nombres con el ID como identificador
    
    ventasTotal = {}
    for id_producto in ventas:
        cantidad = ventas[id_producto]
        precio = precios[id_producto]
        ventasTotal[id_producto] = cantidad * precio #Guarda en un diccionario el valor total de las ventas con el ID del producto como identificador
    
    idpro = max(ventasTotal, key=ventasTotal.get) #Devuelve el ID del producto que vendio más

    return f"El producto con más ingresos es: {nombres[idpro]}" #Accede con el ID a los nombres y devuleve el nombre correspondiente

def TotalVentasDelMes(mes, año, items, productos, ventas):
    totalmes = 0                                       
    
    numBoleta = []                                     
    with open(ventas, "r") as archivoVentas:  
        for linea in archivoVentas:                            
            filas = linea.strip().split(";")
            fecha = filas[1].split("-")          
            mesV = fecha[1]             
            añoV = fecha[2]             
            if int(mesV) == int(mes) and int(añoV) == int(año): 
                numBoleta.append(linea[0]) #Guarda en una lista el número de las boletas segun la fecha solicitada    
    
    productoVendido = {}
    with open(items, "r") as archivoItems: 
        for linea in archivoItems:
            filas = linea.strip().split(";")                     
            
            if filas[0] in numBoleta:                  
                idProducto = filas[1]                  
                cantidad = int(filas[2]) #Si el número de la esta en "items", guarda el ID como identificador de la cantidad vendida                 
                
                if idProducto in productoVendido:       
                    productoVendido[idProducto] += cantidad 
                else:                                   
                    productoVendido[idProducto] = cantidad #Revisa si hay elementos repetidos
    
    with open(productos, "r") as archivoProducto: 
        for linea in archivoProducto:
            filas = linea.strip().split(",")                  
            idProductos = filas[0] #Guardo el ID       
            
            if idProductos in productoVendido: 
                precio = int(filas[2])                  
                cantidad = productoVendido[idProductos] 
                ventaProducto = precio * cantidad      
                totalmes += ventaProducto #Si esta el ID del producto entre los productos vendidos multiplicará el precio por la cantidad vendida                     
    
    return f"Las ventas totales del mes son: {totalmes}"