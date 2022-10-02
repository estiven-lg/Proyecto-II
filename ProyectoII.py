import os
from re import A
import random
import string

path = "./datos/Producto.txt"


def crearBaseDeDatos():
    exits = os.path.isfile(path)
    if(not exits):
        archivo = open(path, "w")
        archivo.close()


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
def agregarProducto():
    Nombre= ""
    Precio= 0
    Proveedor= ""
    Existencia= 0
    Descuento= 0
    nombre= input("Ingrese el nombre del producto") 
    precio= int( input("Ingresa el precio del producto"))
    proveedor= input("Ingrese el nombre del Proveedor") 
    existencia = int( input("Ingresa el numero de existencias"))
    descuento= int( input("Ingresa el descuento por producto"))
    
    
    
    archivo= open(path,"a")
    codigo= id_generator()
    archivo.write(codigo+","+nombre+","+str(precio)+","+proveedor+","+str(existencia)+","+str(descuento)+","+"|\n")
    
   
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
