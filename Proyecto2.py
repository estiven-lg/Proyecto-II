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
    {}+--------------------------------------------------------------+\   
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
    #funcion para agarrar una linea del txt y convertirlo a un objecto producto
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
        #la busqueda aplica a solo codigo y nombre del producto se uso regex
        if (re.search(busqueda, producto['codigo'], re.IGNORECASE) or re.search(busqueda, producto['nombre'], re.IGNORECASE)):
            resultados.append(producto)

    if len(resultados) > 0:
        print("el resultado de tu busqueda es:")
        imprimirProducto(resultados)
    else:
        print("no se encontraron resultados en tu busqueda :c")

# funcion para modificar producto
def modificarProducto():
    print("modificarProducto")
    listdatas=[]
    with open ("./datos/Producto.txt","r") as reader:
        for line in reader.readlines():
            listdatas.append(line)   
    print(listdatas)
    dato=input("que elemento desea modificar?")
    if dato in listdatas:
        j=input("ingrese el nuevo dato: ")
        x=x.replace(dato,j)
    else:
        print("lo siento, ese dato no se encuentra")
        
    
          


crearBaseDeDatos()

print('''
Que Desea Hacer?
1. Agregar producto
2. Buscar a un producto
3. Modificar los datos de un producto
''')

opcion = input(": ")[0].lower()

if (opcion == "1"):
    agregarProducto()
elif (opcion == "2"):
    BuscarProducto()
elif (opcion == "3"):
    modificarProducto()
else:
    print("Opcion no valida")