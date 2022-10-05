#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <time.h>
#include <cstdio>
#include <iomanip>
#include <cstring>
#include <vector>
#include <regex>

using namespace std;

struct Producto
{
    string nombre = "";
    string codigo = " ";
    float precio = 0;
    string proveedor = "";
    int existencia = 0;
    char estado[5] = "-";
    float descuento = 0;
};

string path = "./datos/Producto.txt";

void crearBaseDeDatos();
void agregarProducto();
void BuscarProducto();
void modificarProducto();
string IDGenerator();
void imprimirProducto(Producto producto);
void imprimirProductos(Producto *productos, int size);
vector<Producto> obtenerDatos();
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
        BuscarProducto();
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

string IDGenerator()
{
    srand(time(0));

    string ID = "------";
    char valid[] = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    for (int i = 0; i < 6; ++i)
    {
        ID[i] = valid[rand() % 36];
    }
    return ID;
};

void imprimirProducto(Producto producto)
{
    string tabla = "";
    cout << "+--------------------------------------------------------------+\n";
    cout << "| Codigo Nombre    Precio Proveedor Existencia Estado descuento|\n";
    cout << "|--------------------------------------------------------------|\n";
    cout << "| ";
    cout << left << setw(7) << setfill(' ') << producto.codigo;
    cout << left << setw(10) << setfill(' ') << producto.nombre;
    cout << left << setw(7) << setfill(' ') << producto.precio;
    cout << left << setw(10) << setfill(' ') << producto.proveedor;
    cout << left << setw(11) << setfill(' ') << producto.existencia;
    cout << left << setw(7) << setfill(' ') << producto.estado;
    cout << left << setw(9) << setfill(' ') << producto.descuento;
    cout << "|\n";
    cout << "+--------------------------------------------------------------+\n";
}

void imprimirProductos(Producto *productos, int size)
{
    string tabla = "";
    cout << "+--------------------------------------------------------------+\n";
    cout << "| Codigo Nombre    Precio Proveedor Existencia Estado descuento|\n";
    cout << "|--------------------------------------------------------------|\n";

    for (int i = 0; i < size; i++)
    {
        cout << "| ";
        cout << left << setw(7) << setfill(' ') << productos[i].codigo;
        cout << left << setw(10) << setfill(' ') << productos[i].nombre;
        cout << left << setw(7) << setfill(' ') << productos[i].precio;
        cout << left << setw(10) << setfill(' ') << productos[i].proveedor;
        cout << left << setw(11) << setfill(' ') << productos[i].existencia;
        cout << left << setw(7) << setfill(' ') << productos[i].estado;
        cout << left << setw(9) << setfill(' ') << productos[i].descuento;
        cout << "|\n";
    }
    cout << "+--------------------------------------------------------------+\n";
}

vector<Producto> obtenerDatos()
{
    char lineaChart[1024];
    string lineaStr;
    // static Producto *productos;
    vector<Producto> productos;
    // Read from the text file
    ifstream archivo(path.c_str(), ios::out);

    // Use a while loop together with the getline() function to read the file line by line
    while (getline(archivo, lineaStr))
    {
        strcpy(lineaChart, lineaStr.c_str());
        char *ptr[10];
        int i = 0;
        ptr[i] = strtok(lineaChart, ",");
        while (ptr[i] != NULL)
        {
            ptr[++i] = strtok(NULL, ",");
        }
        Producto producto;
        producto.codigo = ptr[0];
        producto.nombre = ptr[1];
        producto.precio = strtod(ptr[2], NULL);
        producto.proveedor = ptr[3];
        // int num = ptr[4];
        producto.existencia = stoi(ptr[4]);
        producto.estado[0] = (char)ptr[5][0];
        producto.descuento = strtod(ptr[6], NULL);
        productos.push_back(producto);
    }

    // Close the file
    archivo.close();
    return productos;
};

void agregarProducto()
{
    Producto nuevoProducto;
    nuevoProducto.codigo = IDGenerator();
    imprimirProducto(nuevoProducto);

    cout << "ingrese el nombre del producto,por favor\n";
    cin >> nuevoProducto.nombre;
    cin.ignore();
    imprimirProducto(nuevoProducto);

    cout << "ingrese el precio del producto ,por favor\n";
    cin >> nuevoProducto.precio;
    cin.ignore();
<<<<<<< HEAD
    cout << "ingrese el codigo del producto ,por favor\n";
    cin >> nuevoProducto.codigo;
    cin.ignore();
    cout << "ingrese el proveedor del producto ,por favor\n";
    cin >> nuevoProducto.proveedor;
    cin.ignore();
    cout << "ingrese el estado del producto ,por favor\n";
    cin >> nuevoProducto.estado;
    cin.ignore();
    cout << "ingrese el numero de existencia del producto ,por favor\n";
    cin >> nuevoProducto.existencia;
    cin.ignore();
    cout << "ingrese el descuento del producto ,por favor\n";
    cin >> nuevoProducto.descuento;
    cin.ignore();
     
=======
    imprimirProducto(nuevoProducto);

    cout << "ingrese el proveedor del producto ,por favor\n";
    cin >> nuevoProducto.proveedor;
    cin.ignore();
    imprimirProducto(nuevoProducto);

    cout << "ingrese el existencia del producto ,por favor\n";
    cin >> nuevoProducto.existencia;
    cin.ignore();
    imprimirProducto(nuevoProducto);

    while (toupper(nuevoProducto.estado[0]) != 'A' && toupper(nuevoProducto.estado[0]) != 'R')
    {
        cout << "ingrese el estado del ,aprovado(A) o Reprobado(R) ,por favor\n";
        cin >> nuevoProducto.estado;
        cin.ignore();
        if (toupper(nuevoProducto.estado[0]) != 'A' && toupper(nuevoProducto.estado[0]) != 'R')
        {
            cout << "ingrese una opcion valida\n";
            nuevoProducto.estado[0] = '-';
        }
    };
    nuevoProducto.estado[0] = toupper(nuevoProducto.estado[0]);

    imprimirProducto(nuevoProducto);
    cout << "ingrese el descuento del producto ,por favor\n";
    cin >> nuevoProducto.descuento;
    cin.ignore();
    imprimirProducto(nuevoProducto);

>>>>>>> d06158cabe11ec31ed558e4640a164bc8af28094
    ofstream archivo;
    archivo.open(path.c_str(), ios::app);
    archivo << nuevoProducto.codigo;
    archivo << ",";
    archivo << nuevoProducto.nombre;
    archivo << ",";
    archivo << nuevoProducto.precio;
    archivo << ",";
    archivo << nuevoProducto.proveedor;
    archivo << ",";
    archivo << nuevoProducto.existencia;
    archivo << ",";
    archivo << nuevoProducto.estado[0];
    archivo << ",";
    archivo << nuevoProducto.descuento;
    archivo << "| \n";
    archivo.close();
};

void BuscarProducto()
{
    string busqueda;
    cout << "Escribe tu busqueda:";
    cin >> busqueda;

    regex regexBusqueda(busqueda + "(.*)", regex_constants::icase);

    vector<Producto> productosList = obtenerDatos();
    vector<Producto> resultadosList;

    for (auto &producto : productosList)
    {
        bool matchCodigo = regex_search(producto.codigo, regexBusqueda);
        bool matchNombre = regex_search(producto.nombre, regexBusqueda);
        if (matchCodigo || matchNombre)
        {
            resultadosList.push_back(producto);
        }
    }
 

    Producto *productos = resultadosList.data();
    int size = resultadosList.size();

    imprimirProductos(productos, size);
};

void modificarProducto(){

};
