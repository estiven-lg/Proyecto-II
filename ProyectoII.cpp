#include <iostream>
#include <stdlib.h>
#include <fstream>

using namespace std;
void crearBaseDeDatos();
string path = "./datos/Producto.txt";
int main()
{
    crearBaseDeDatos();
    return 0;
}

void crearBaseDeDatos()
{
    ;
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
}