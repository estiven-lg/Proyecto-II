#include <iostream>
#include <stdlib.h>
#include <fstream>


using namespace std;
void ingresarProducto();

int main()
{
    ingresarProducto();
    return 0;
}

void ingresarProducto()
{
    ofstream datos("./datos/Producto.txt",ios::app);
    if (datos.fail())
    {
        cout<<"No se pudo crear la base de datos :c \n";
        exit(1);
    }
    datos<<"\nhola mundo";
    datos.close();
}