
Segundo proyecto del segundo semestre de ingeniera en sistemas UMG
# _Proyecto II_
*****
###### Consiste en realizar dos aplicaciones que realicen las mismas funciones pero en esta ocasión trata sobre los datos de distintos productos, que contengan sus datos , tanto como precio, descuento, así como código único , basado en el manejo de archivos y estructuras . Cada enunciado se llevó a cabo utilizando C++ y Python, todo esto junto al editor visual studio code, GitHub.
****
### *Requisitos* 
- version de python: 3.9.7
- version de G/C ++ : MinGW.org GCC-6.3.0-1

## *Instalación*
Visual Studio Code Version 1.72 disponible, recuerda tener presente de que los términos 32 bits y 64 bits se refieren a la forma en que el procesador de una computadora y en este [enlace](https://code.visualstudio.com/download) puedes encontrar la opción que más se acople a tus necesidades.

#### *¿CÓMO CONFIGURAR VSCODE CON C ++ Y PYTHON?*

Todo lo que necesita hacer es instalar algunas extensiones para ponerlo en funcionamiento.
- [C / C ++ para Visual Studio Code](c++ (MinGW.org GCC-6.3.0-1) 6.3.0)(https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)esta es una extensión auxiliar. Requerido para IntelliSense, depuración y exploración de código.
- [Python para Visual Studio Code](Python 3.9.7)(https://marketplace.visualstudio.com/items?itemName=ms-python.python) Linting, Debugging(multiproceso, remoto), Intellisense, formato de código, fragmentos y más.
- [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner):(opcional si se acopla a tus necesidades) Ejecute un fragmento de código o un archivo de código para varios idiomas sin ejecutar comandos.
- [MSYS2](https://www.msys2.org/) es una colección de herramientas y bibliotecas que le proporciona un entorno fácil de usar para crear, instalar y ejecutar software nativo de Windows.

*Ya lo tenemos listo, con esta configuración debería dejar correr sin problema sus proyectos. Para más configuraciones consulte el siguiente [enlace](https://code.visualstudio.com/docs/cpp/launch-json-reference).*
# Descargar proyecto
```
git clone https://github.com/estiven-lg/Proyecto-II.git
```
### Apertura del terminal integrado de PowerShell en VS Code
VS Code contiene un [terminal integrado](https://code.visualstudio.com/docs/terminal/basics) que te permite abrir una línea de comandos de Python con PowerShell, lo que establece un flujo de trabajo sin interrupciones entre el editor de código y la línea de comandos.

- 1.Abre el terminal en VS Code, selecciona Ver>Terminal, o bien usa el acceso directo Control + ` (mediante el carácter de tilde aguda).
- 2.En el terminal de VS Code, para abrir Python, escribe python.
- 3.Para probar el intérprete de Python, escribe print("Hello World"). Python devolverá la instrucción "Hola mundo".
- 4.Para salir de Python, puedes escribir exit() o quit(), o seleccionar Control-Z.

# *Instalar GIT (opcional)*
Si planeas colaborar con otras personas en el código de Python u hospedar el proyecto en un sitio de código abierto (como GitHub), VS Code admite el [control de versiones con GIT](https://code.visualstudio.com/docs/editor/versioncontrol#_git-support).La pestaña Control de código fuente de VS Code realiza un seguimiento de todos los cambios y tiene comandos GIT comunes (agregar, confirmar, enviar cambios e incorporar cambios) integrados directamente en la interfaz de usuario. Primero, debes instalar GIT para alimentar el panel de control de código fuente.

- Descarga e instala GIT para Windows desde el siguiente  [enlace](https://git-scm.com/download/win). 
- Descarga e instala Git para linux desde el siguiente [enlace](https://git-scm.com/download/linux)

- _Existe una guía detallada para la instalación , se le presentará unas series de preguntas para configurar su entorno , si usará todas las opciones predeterminas solo haga clic en "next" cada vez que lo vea, si usted quiere cambiar alguna variable en su entorno puede elegir la que más se acople a sus necesidades._

- Si por algun motivo no está familiarizado con GIT, también están [las guías de GitHub](https://guides.github.com/) las cuales puede utilizar como herramienta de apoyo.

## Tareas comunes 
-----
# _Manejo de archivos_
Los archivos TXT son archivos que contienen texto sin formato. Estos archivos pueden crearse con casi cualquier procesador de textos o programa de edición,como tal es el caso de Vs Code,  pero el formato de archivo TXT no admite características y funciones como tablas, gráficos e impresión en negrita o cursiva.

###  _Archivos .txt en Python_
En Python, para abrir un archivo usaremos la función open, que recibe el nombre del archivo a abrir.
> archivo = open("archivo.txt")

Esta función intentará abrir el archivo con el nombre indicado. Si tiene éxito, devolverá una variable que nos permitirá manipular el archivo de diversas maneras.La operación más sencilla a realizar sobre un archivo es leer su contenido. Para procesarlo línea por línea, es posible hacerlo de la siguiente forma:

> línea=archivo.readline()
while línea != '':
    # procesar línea
    línea=archivo.readline()

Esto funciona ya que cada archivo que se encuentre abierto tiene una posición asociada, que indica el último punto que fue leido. Cada vez que se lee una línea, avanza esa posición. Es por ello que readline() devuelve cada vez una línea distinta y no siempre la misma.

La siguiente estructura es una forma equivalente a la vista en el ejemplo anterior.

> for línea in archivo:
    # procesar línea
    
De esta manera, la variable línea irá almacenando distintas cadenas correspondientes a cada una de las líneas del archivo. Es posible, además, obtener todas las líneas del archivo utilizando una sola llamada a función:

> líneas = archivo.readlines()
En este caso, la variable líneas tendrá una lista de cadenas con todas las líneas del archivo.

#### _Cerrar un archivo_
Al terminar de trabajar con un archivo, es recomendable cerrarlo, por diversos motivos: en algunos sistemas los archivos sólo pueden ser abiertos de a un programa por la vez; en otros, lo que se haya escrito no se guardará realmente hasta no cerrar el archivo; o el limite de cantidad de archivos que puede manejar un programa puede ser bajo, etc.

Para cerrar un archivo simplemente se debe llamar a:

> archivo.close()

### Modo de apertura de los archivos
La función open recibe un parámetro opcional para indicar el modo en que se abrirá el archivo. Los tres modos de apertura que se pueden especificar son:

Modo de sólo lectura (r). En este caso no es posible realizar modificaciones sobre el archivo, solamente leer su contenido.
- Modo de sólo escritura (w). En este caso el archivo es truncado (vaciado) si existe, y se lo crea si no existe.
- Modo sólo escritura posicionándose al final del archivo (a). En este caso se crea el archivo, si no existe, pero en caso de que exista se posiciona al final, manteniendo el contenido original.
- Por otro lado, en cualquiera de estos modos se puede agregar un + para pasar a un modo lectura-escritura. El comportamiento de r+ y de w+ no es el mismo, ya que en el primer caso se tiene el archivo completo, y en el segundo caso se trunca el archivo, perdiendo así los datos.

### *Nota*   

_Si un archivo no existe y se lo intenta abrir en modo lectura, se generará un error; en cambio si se lo abre para escritura, Python se encargará de crear el archivo al momento de abrirlo, ya sea con w, a, w+ o con a+)._

De la misma forma que para la lectura, existen dos formas distintas de escribir a un archivo. 
- Mediante cadenas:
  > archivo.write(cadena)
- mediante listas de cadenas:
  > archivo.writelines(lista_de_cadenas)

### _Archivos .txt en C++_
Para crear un archivo de texto en C++ debes incluir los paquetes iostream y fstream.

- ofstream: Clase stream para escribir archivos.
- ifstream: Clase stream para leer archivos.
- fstream: Clase stream para hacer ambas cosas, leer y escribir.

por ejemplo:
```sh
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
```    
# Structs en C++
pueden contener variables de muchos tipos diferentes de datos.
- struct:  es una palabra reservada de C que indica que los elementos que vienen agrupados a continuación entre llaves componen una estructura.
 
- nombre_estructura: identifica el tipo de dato que se describe y del cual se podrán declarar variables. Se especifica entre corchetes para indicar su opcionalidad.
 
- miembro1, miembro2,...: Son los elementos que componen la estructura de datos, deben ser precedidos por el tipo_dato al cual pertenecen.
 
# Funciones avanzadas:
***
#### ¿De qué se encargan?, ¿cuál es el uso esperado ?
### _EN C++_
- Stew: El método setw() de la biblioteca iomanip en C++ se utiliza para establecer el ancho del campo de la biblioteca ios en función del ancho especificado como parámetro de este método. 

- Setfill: El método setfill() de la biblioteca iomaip en C++ se utiliza para establecer el carácter de relleno de la biblioteca ios en función del carácter especificado como parámetro de este método. Este método acepta c como parámetro, que es el argumento de carácter correspondiente al que se va a establecer el relleno.Este método no devuelve nada. Solo actúa como manipuladores de flujo.

- Strtok: Una secuencia de llamadas a esta función divide str en tokens, que son secuencias de caracteres contiguos separados por cualquiera de los caracteres que forman parte de los delimitadores .
> char * strtok (char * str, const char * delimitadores)

- strtod:La función primero descarta tantos caracteres de espacio en blanco (como enes espacio) según sea necesario hasta que se encuentre el primer carácter que no sea un espacio en blanco. Luego, a partir de este carácter, toma tantos caracteres como sea posible que sean válidos siguiendo una sintaxis similar a la de los literales de punto flotante (ver más abajo), y los interpreta como un valor numérico. Un puntero al resto de la cadena después del último carácter válido se almacena en el objeto al que apunta endptr .

- Stoi:La función stoi convierte la secuencia de caracteres de str en un valor de tipo int y devuelve el valor. Por ejemplo, cuando se pasa la secuencia de caracteres “10”, el valor devuelto por stoi es el número entero 10.

- Regex:Las regex son cadenas de caracteres basadas en reglas sintácticas que permiten describir secuencias de caracteres.

- Toupper: Convierte una carácter entre la a y la z (minúsculas) a mayúsculas. Si es mayúscula u otro símbolo no se altera. Según la implementación, es muy posible que falle con caracteres internacionales (como á, ñ).


### _En Python_
- Replace: Existen 2 métodos para poder usar esta función 
- 1.El método replace() Cuando el archivo de entrada y salida no es el mismo en Python se utiliza para buscar una subcadena y reemplazarla con otra subcadena.Trabajamos simultáneamente en dos archivos diferentes,se abre en el modo de lectura de texto rt y se hace referencia a al otro archivo se abre en el modo de escritura de texto wt y se hace referencia a fout. Luego se repite el bucle for y, por cada aparición de la cadena en el archivo, se reemplaza por la palabra . A continuación, ambos archivos se cierran después de las operaciones necesarias con la ayuda de la función close().

- 2.Cuando el archivo de salida y entrada es el mismo usamos la instrucción with aquí junto con la función replace(). El gestor de contexto with tiene una función fundamental: hacer que el programa sea más corto y mucho más legible.Cuando usamos la instrucción with con Manejo de archivos, el archivo que abrimos en el código Python no necesita cerrarse manualmente; se cierra automáticamente después de que termina el bloque with.

- Split:devuelve una lista con las palabras en el string, utilizando un separador especificado como delimitador entre palabras.
>Su sintaxis es:

 string.split(sep,maxsplit)


- re.serch:La función re.search recorre la cadena de texto string buscando la primera coincidencia del patrón pattern devolviendo el [objeto match](https://docs.python.org/es/3/library/re.html#match-objects) correspondiente. En caso de no encontrarse ninguna coincidencia, la función devuelve None.

- Upper: La función UPPER devuelve una cadena de caracteres que tiene el mismo tipo de datos que la cadena de entrada a mayúsculas.



    
