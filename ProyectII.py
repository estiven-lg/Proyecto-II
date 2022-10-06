
"""
@authors Estiven Laferré <@miumg.gt, Javier De La Cruz <@miumg.gt, Keila Ramírez <kramireza10@miumg.gt
@description Proyecto ll, está basado en el manejo de archivos.
@license GPL v3
@date 2022/10/07
"""
import os
import re
import random
import string

path = "./datos/Producto.txt"

# funcion para verificar que exista una base de datos y si no la crea


def crearBaseDeDatos():
    exits = os.path.isfile(path)
    if(not exits):
        archivo = open(path, "w")
        archivo.close()

# generador de id


def IDGenerator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# funcion para mostrar uno o mas productos


def imprimirProducto(Productos):
    tabla = """
    +--------------------------------------------------------------+
    | Codigo Nombre    Precio Proveedor Existencia Estado descuento|
    |--------------------------------------------------------------|
    {}+--------------------------------------------------------------+   
    """
    body = ""
    for Producto in Productos:
        body += "| {:<6} {:<9} {:<6} {:<10} {:<10} {:<5} {:<8} | \n    ".format(
            Producto["codigo"],
            Producto["nombre"],
            Producto["precio"],
            Producto["proveedor"],
            Producto["existencia"],
            Producto["estado"],
            str(Producto["descuento"])+"%",
        )
    print(tabla.format(body))


# funcion para mandar a traer los datos del txt
def obtenerDatos():
    # funcion para agarrar una linea del txt y convertirlo a un objecto producto
    def convertirTextoAProducto(texto):
        preProducto = texto.replace('|', '').split(",")
        Producto = {
            "codigo": preProducto[0],
            "nombre": preProducto[1],
            "precio": float(preProducto[2]),
            "proveedor": preProducto[3],
            "existencia": int(preProducto[4]),
            "estado": preProducto[5],
            "descuento": float(preProducto[6]),
        }
        return Producto

    Productos = []

    archivo = open(path, "r")
    for linea in archivo:
        Productos.append(convertirTextoAProducto(linea))
    archivo.close()
    return Productos

# funcion para agregar producto


def agregarProducto():
    # objeto con las propiedades de un producto
    Producto = {
        "codigo": IDGenerator(),
        "nombre": "",
        "precio": 0,
        "proveedor": "",
        "existencia": 0,
        "descuento": 0,
        "estado": "n/a"
    }

    # se muestra como va el producto mientra el usuario lo va ingresando
    imprimirProducto([Producto])
    Producto["nombre"] = input("Ingrese el nombre del producto:")
    imprimirProducto([Producto])
    Producto["precio"] = float(input("Ingresa el precio del producto:"))
    imprimirProducto([Producto])
    Producto["proveedor"] = input("Ingrese el nombre del Proveedor:")
    imprimirProducto([Producto])
    Producto["existencia"] = int(input("Ingresa el numero de existencias:"))
    imprimirProducto([Producto])

    while(Producto["estado"][0].upper() != "A" and Producto["estado"][0].upper() != "R"):
        Producto["estado"] = input(
            "ingresa el estado del producto, Aprovado(A) o Reprobado(R):").upper()
        if (Producto["estado"][0] != "A" and Producto["estado"][0] != "R"):
            print("ingrese una opcion valida")
            Producto["estado"] = "n/a"
    imprimirProducto([Producto])

    Producto["descuento"] = float(input("Ingresa el descuento por producto:"))
    imprimirProducto([Producto])
    archivo = open(path, "a")
    archivo.write(Producto["codigo"]+","+Producto["nombre"]+","+str(Producto["precio"])+","+Producto["proveedor"] +
                  ","+str(Producto["existencia"])+","+Producto["estado"]+","+str(Producto["descuento"])+"|\n")
    archivo.close()

# funcion para buscar producto


def BuscarProducto():
    # listado donde iran los productos que coincidan en la busqueda
    resultados = []
    productos = obtenerDatos()
    busqueda = input("Escribe tu busqueda:")

    # recorre todo el listado y solo agrega en resultados los productos con alguna concidencia
    for producto in productos:
        # la busqueda aplica a solo codigo y nombre del producto se uso regex
        if (re.search(busqueda, producto['codigo'], re.IGNORECASE) or re.search(busqueda, producto['nombre'], re.IGNORECASE)):
            resultados.append(producto)

    if len(resultados) > 0:
        print("el resultado de tu busqueda es:")
        imprimirProducto(resultados)
    else:
        print("no se encontraron resultados en tu busqueda :c")

# funcion para modificar producto


def modificarProducto():
    IDProducto = input("Ingrese el ID del producto que desea modificar:")
    index = -1
    productos = obtenerDatos()
    
    #recoremos el listado de producto hasta obtener uno con el id que el usuario nos dio
    for i in range(len(productos)):
        if (productos[i]['codigo'].upper() == IDProducto.upper()):
            index = i
            break
    # si el el index es diferente de -1 es porque encontro algo
    if(index == -1):
        print('lo siento, el dato con el id:"', IDProducto, '" no se encuentra')
        return
    
    #producto encontrado el cual modificaremos
    nuevoProducto = productos[index]
    
    # se muestra como va el producto mientra el usuario lo va modificando
    imprimirProducto([nuevoProducto])
    nuevoProducto["nombre"] = input("Ingrese el nombre del producto:")
    imprimirProducto([nuevoProducto])
    nuevoProducto["precio"] = float(input("Ingresa el precio del producto:"))
    imprimirProducto([nuevoProducto])
    nuevoProducto["proveedor"] = input("Ingrese el nombre del Proveedor:")
    imprimirProducto([nuevoProducto])
    nuevoProducto["existencia"] = int(input("Ingresa el numero de existencias:"))
    imprimirProducto([nuevoProducto])

    nuevoProducto["estado"] = input("ingresa el estado del producto, Aprovado(A) o Reprobado(R):").upper()[0]
    while(nuevoProducto["estado"][0].upper() != "A" and nuevoProducto["estado"][0].upper() != "R"):
        print("ingrese una opcion valida")
        nuevoProducto["estado"] = input(
            "ingresa el estado del producto, Aprovado(A) o Reprobado(R):").upper()
        
    imprimirProducto([nuevoProducto])
    nuevoProducto["descuento"] = float(
        input("Ingresa el descuento por producto:"))
    
    print("Producto modificado :D !!!")
    imprimirProducto([nuevoProducto])

    #re-escribimos todo el txt pero con la linea cambiada
    archivoAntiguo = open(path, 'r').readlines()
    archivoAntiguo[index] = nuevoProducto["codigo"]+","+nuevoProducto["nombre"] + ","+str(nuevoProducto["precio"])+","+nuevoProducto["proveedor"] + "," +str(nuevoProducto["existencia"])+","+nuevoProducto["estado"] + ","+str(nuevoProducto["descuento"])+"|\n"
    nuevoArchivo = open(path, 'w')
    nuevoArchivo.writelines(archivoAntiguo)
    nuevoArchivo.close()


#aqui empieza el cuerpo del codigo
crearBaseDeDatos()

opcion = 0
while( opcion != "4"):
    print("Que Desea Hacer?")
    print("1. Agregar producto")
    print("2. Buscar a un producto")
    print("3. Modificar los datos de un producto")
    print("4 .Salir")
    opcion = input(": ")[0].lower()

    if (opcion == "1"):
        agregarProducto()
    elif (opcion == "2"):
        BuscarProducto()
    elif (opcion == "3"):
        modificarProducto()
    elif(opcion == "4"):
        print("Adios :D")
    else:
        print("\nOpcion no valida\n")
