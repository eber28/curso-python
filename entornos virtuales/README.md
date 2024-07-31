## ENTORNO_VIRTUAL EN PYTHON 
### QUE SON LOS ENTORNOS VIRTUlALES
Un entorno virtual es un directorio aislado que contiene una instalación de Python y sus dependencias. Esto significa que cada proyecto puede tener su propio entorno virtual con sus propias versiones de los paquetes instalados.

Los entornos virtuales son útiles por las siguientes razones:

Evita conflictos de versiones: Si estás trabajando en varios proyectos que requieren diferentes versiones del mismo paquete, los entornos virtuales pueden ayudarte a evitar conflictos de versiones.
Mantiene tu sistema limpio: Los entornos virtuales se instalan en directorios separados, lo que ayuda a mantener tu sistema limpio y ordenado.
Mejora la reproducibilidad: Los entornos virtuales te permiten reproducir el entorno de desarrollo exacto de tu proyecto, lo que facilita el trabajo en equipo y la colaboración.
### COMANDOS  PARA ENTORNOS VIRTUALES
- cd: este comando sirve para ingresar a una carpeta y poder acceder a ella  para poder hacwee el trabajo

       *ejemplo*
       cd entornos_virtuales


- ls:  es para que te muestre todas las capetas que contiene   un archivo
- python -m venv.venv: comando
- source .venv/scripts/activate: es un comnado
- pip list:es para gestionar paquetes utilizado para instalar y administrar 
- pip --version:gestionar las versiobes del sistema
- pip install upgrade pip:es la instalacion de un paquete
- python -m pip install --upgrade pip: instalcion ... 
- `
### CREACION DE UN ENTORNO VIRTUAL
En Python, hay dos herramientas principales para crear entornos virtuales:

venv: Esta es la herramienta integrada de Python para crear entornos virtuales.
virtualenv: Esta es una herramienta externa que ofrece más funciones que venv.
Creación de entornos virtuales con venv

Para crear un entorno virtual con venv, ejecuta el siguiente comando en la terminal:

python -m venv <nombre_entorno>
Por ejemplo, para crear un entorno virtual llamado «mi_entorno», ejecuta el siguiente comando:

python -m venv mi_entorno
### Activación de entornos virtuales
Para activar un entorno virtual, ejecuta el archivo activate en la terminal.

En Windows, ejecuta el siguiente comando:

.\mi_entorno\activate.bat
En macOS y Linux, ejecuta el siguiente comando:

source mi_entorno/activate

### Instalación de paquetes en entornos virtuales . 
Una vez que hayas activado un entorno virtual, puedes instalar paquetes usando el comando pip. pov no se sube el trabajo 

Por ejemplo, para instalar el paquete numpy en el entorno virtual mi_entorno, ejecuta el siguiente comando:

pip install numpy

### Desactivación de entornos virtuales
Para desactivar un entorno virtual, ejecuta el siguiente comando en la terminal:

deactivate
### Eliminación de entornos virtuales
Para eliminar un entorno virtual, elimina el directorio que contiene el entorno virrtual... como producto final
para una optima realizacion sobre entornos virtuales  hacienmdo uso de los distintos comandos que se mosttraron en la parte de arriba. profesor no sube el trabajo ... ...
una vez mas intentanto