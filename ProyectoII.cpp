#include <iostream>
#include <stdlib.h>
#include <fstream>

using namespace std;

struct Producto
{
    string nombre;
    string codigo;
    float precio;
    string proveedor;
    int existencia;
    char estado;
    float descuento; 
};


string path = "./datos/Producto.txt";

void crearBaseDeDatos();
void agregarProducto();
void BuscarProducto();
void modificarProducto();

int main()
{
    char opcion[2];
    crearBaseDeDatos();
    cout << "que desea hacer?\n";
    cout << "1. Agregar producto\n";
    cout << "2. Buscar a un producto\n";
    cout << "3. Modificar los datos de un producto\n";
    cout << ":";
    cin.getline(opcion, 2);
    switch (opcion[0])
    {
    case '1':
        agregarProducto();
        break;
    case '2':
        agregarProducto();
        break;
    case '3':
        modificarProducto();
        break;
    default:
        cout << "opcion no valida.";
        break;
    }
    return 0;
};

void crearBaseDeDatos()
{
    ifstream archivo(path.c_str(), ios::out);
    if (archivo.fail())
    {
        ofstream archivoNuevo;
        archivoNuevo.open(path.c_str());
        if (archivoNuevo.fail())
        {
            cout << "No se pudo crear la base de datos :c \n";
            exit(1);
        }
    }
};

void agregarProducto(){
    Producto nuevoProducto; 
    cout << "ingrese el nombre del producto,por favor\n";
    cin >> nuevoProducto.nombre;
    cin.ignore();
    cout << "ingrese el precio del producto ,por favor\n";
    cin >> nuevoProducto.precio;
     cin.ignore();
    cout << "ingrese el codigo del producto ,por favor\n";
    cin >> nuevoProducto.codigo;
     cin.ignore();
    cout << "ingrese el proveedor del producto ,por favor\n";
    cin >> nuevoProducto.proveedor;
    cin.ignore();
    cout << "ingrese el estado del producto ,por favor\n";
    cin >> nuevoProducto.estado;
     cin.ignore();
   cout << "ingrese el existencia del producto ,por favor\n";
    cin >> nuevoProducto.existencia;
     cin.ignore();
    cout << "ingrese el descuento del producto ,por favor\n";
    cin >> nuevoProducto.descuento;
     cin.ignore();
     
    ofstream archivo;
    archivo.open(path.c_str(), ios::app);
    archivo << nuevoProducto.nombre;
    archivo <<",";
    archivo << nuevoProducto.precio;
    archivo <<"| \n";
    archivo << nuevoProducto.codigo;
    archivo <<",";
    archivo << nuevoProducto.proveedor;
    archivo <<"| \n";
    archivo << nuevoProducto.estado;
    archivo <<",";
    archivo << nuevoProducto.existencia;
    archivo <<"| \n";
    archivo << nuevoProducto.descuento;
    archivo <<"| \n";

    archivo.close();
    
};

void BuscarProducto(){

};

void modificarProducto(){

};
