#include <iostream>
#include <stdlib.h>
#include <fstream>

using namespace std;

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
        void agregarProducto();
        break;
    case '2':
        void agregarProducto();
        break;
    case '3':
        void modificarProducto();
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

};

void BuscarProducto(){

};

void modificarProducto(){

};
