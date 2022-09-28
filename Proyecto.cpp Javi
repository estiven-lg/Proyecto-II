import os

path = "./datos/Producto.txt"


def crearBaseDeDatos():
    exits = os.path.isfile(path)
    if(not exits):
        archivo = open(path, "w")
        archivo.close()


def agregarProducto():
    print("agregarProducto")


def BuscarProducto():
    print("BuscarProducto")


def modificarProducto():
    print("modificarProducto")


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
