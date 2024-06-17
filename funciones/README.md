# FUNCIONES
## CONSEPTO
MATEMATICAMENTE UNA FUNCION ES UNA OPERACION
 QUE TMA UNO O MAS VALORES LLAMADOS
 ``ARGUMENTOS`` Y PRODUCE UN VALOR PREDETERMINADO
`RESULTADO`
> [!NOTE]
>todos los lenguajes de programacion tiene funciones incorporadas (``funciones internas``)
, y funciones creadas por el usuario (``funcines externas``)

En programacion una funcion es un subprograma, e suna estrructura que nos permite agrupar codigo y 
sus principales objetivos son:
-``NO REPETIR`` fragmentos de codigo
-``REUTILIZAR``  el codigo en distintos escenarios`
## ESTRUCTUIRA DE UNA FUNCION
una funcion viene ``definida`` por un ``nombre``, sus ``parametros`` y su valor de ``retorno``.
una ves creada la funcion podremos solicitar su ejecusion ``invocando`` la funcion por su  ``nombre ``
## DEFINIR UNA FUNCION EN PYTHON
 para definir una funcion en python primero utilizaremos la palabra reservada ``def`` seguida por el nombre de la funcion. a continuacion especificaremos los ``parametros`` con ```()`` si es una funcion sin parametros,``(a)`` si es un funcion con parametros, si se tubiera mas de un parametros iran separados por ``,``, finalizaremos la linea con``:``, en la siguiente liena sin olvidar el identado, comenzara el ``cuerpo`` de la funcon (micro programa) que puede contener 1 o mas sentencias, finalmente devera ``retornar`` un resultado con la palabra reservada``return``.
 >[!INFO]
 >como retorno tambien se puede utilizar la ``funcion interna`` , ``print()``, para depuracion de codigo no es recomendable usarlo en produccion.
 >``print`` dentro de una funcion  es una herramienmta que se utiliza para depurar o comprobar que una funcion este asiendo el trabajo de manera correcta
 **ejemplo**
 ```python
 def saludo():
    saludo="hola chivo"
    saludo_dos="como estas "
    return f"{saludo}, {saludo_dos}"
    #print(f"{saludo}, {saludo_dos}")
print(saludo())
#saludo()
```
## INVOCAR UAN FUNCION
para invocar, (o llamar, ejecutar) una funcion solo tenemos que escriber el ``nombre`` de la funcion seguido por `()` perentesis.
```python
def saludo():
    print("hola")
#invocando la funcion
saludo()

```
## RETORNAR UN VALOR
las funciones pueden retornar (o devolver) un valor 
```python
def uno():
    return 1
uno()
```
>[!WARNING]
>no confundir `print()` con `return`.  el valor retornado por `return` nos permite usarlo fuera del contexxto, y ``print()`` solo mostrara el literal 
## RETORNANDO MULTIPLES VALORES 
el secreto es hacerlo mediante un tipo de dato estructurado 
```python
def varios():
    return 2,3,4
varios()
#retorna (2,3,4)
 
 def lista():
    return("hola",45)
lista()
#retorna ["hola",45]
def dicc():
    return{"nombre":"jose","edad":45}
dicc()
#retorna {"nombre":"jose","edad":45}
```
## parametros y argumentos
si una funcion no dispusiera de valores de emtrada estaria limitadaen su actuasion.
es por ello que los ``parametros`` no permiten variar los datos que consume una funcion para obtener distintos resultados
**ejemplo**
*crear una funcion que recive un valor numerico y retorna su raiz cuadrada*
```python
def sqrt(valor):
    return valor**(1/2)
# NOTA: en este3 caso, el valor 4 es un argumento de la funcion
sqrt(4)
```
cuando llamamos a una funcion con `argumentos`, los valores de estos argumentos se copian en los correspondiente `parametros` dentro de la funcion
```python
def ejm(a,b,c):
    return a+b+c
ejm(4,6,5)    
```
### ARGUMENTOS NOMINALES
en esta aproximacion los argumentos no son copiados en un orden especificado sino que **se asignan por nombre a cada parametro**. ello nos permite evitar el problema de conocer o recordar cxual es el orden de lo parametros en la definicion en la funcion.
para utilizarlo basta con realizar una asignacion de cada argumento en la propia
llamada ala funcion.
**ejemplo**
```python
def build_cpu(familia,num_core,frecuencia):
    print(f"""
    la cpu es de la familia{familia},
    con {num_core} cores y con una
    frecuencia de {frecuencia}
    """)
# haciendo uso de argumentos nominales
build_cpu(num_core=4,familia="intel",frecuencia=2.8)
```
### ARGUMENTOS POSICIONALES 
los srgumrntod son copiados en un orden especifico, en este caso debemos conocer o recordar cual es el orden de los parametros
**ejemplo**
```python
def build_cpu(familia,num_core,frecuencia):
    print(f"""
    la cpu es de la familia{familia},
    con {num_core} cores y con una
    frecuencia de {frecuencia}
    """)
# haciendo uso de argumentos posicionales
build_cpu("intel",4,2.7)
```
### PARAMETROS POR DEFECTO
es posible especificar **valores por defecto** en los parametros de una funcion, en el caso de uqe no se proporcione un valor de argumento en la llamda a la funcion, el parametro correspondiente tomara el valor definido por defecto
**ejemplo**
```python
def alumnos(nombre,apellido,estado="aprovado"):

alumnos("ruth","castillo")
alumnos("antony","cruces","desaprobado")
```
## DESEMPAQUETADO/EMPAQUETADO DE ARGUMENTOS (TAREA)
El "desempaquetado" y "empaquetado" de argumentos son conceptos relacionados con el manejo de argumentos en funciones, especialmente en lenguajes de programación que admiten la manipulación flexible de listas de argumentos.

### Desempaquetado de argumentos (Unpacking)

El desempaquetado de argumentos se refiere a pasar una lista o tupla como argumentos individuales a una función. Esto es útil cuando los argumentos ya están organizados en una lista o tupla, pero la función espera argumentos separados.

Por ejemplo, supongamos que tienes una función suma que toma dos argumentos:

python
def suma(a, b):
    return a + b


Si tienes una lista o tupla con los valores que deseas sumar:

python
valores = [3, 5]


Puedes desempaquetar estos valores y pasarlos como argumentos a la función suma usando el operador *:

python
resultado = suma(*valores)
print(resultado)  # Salida: 8


Aquí, *valores desempaqueta la lista [3, 5] en dos argumentos separados 3 y 5, que luego son pasados a la función suma.

### Empaquetado de argumentos (Packing)

El empaquetado de argumentos es el proceso inverso, donde múltiples argumentos se agrupan en una única estructura de datos, como una lista o tupla, para pasarlos como un solo argumento a una función.

Por ejemplo, si deseas definir una función imprimir_valores que pueda manejar cualquier cantidad de argumentos y simplemente los imprima:

python
def imprimir_valores(*args):
    for valor in args:
        print(valor)



Puedes llamar a esta función con cualquier número de argumentos y serán empaquetados en una tupla dentro de args:

python
imprimir_valores(1, 2, 3, 4)
imprimir_valores('a', 'b', 'c')


En este caso, *args empaqueta todos los argumentos dados en una tupla, permitiendo que la función imprimir_valores los maneje de manera flexible.

## FUNCIONES INTERNAS DE PYTHON (TAREA)

En Python, las funciones internas (o funciones integradas) son aquellas que están disponibles sin necesidad de importar ningún módulo adicional, ya que forman parte del núcleo del lenguaje. Estas funciones están siempre disponibles y pueden ser utilizadas en cualquier programa Python. Algunas de las funciones internas más comunes incluyen:

1. *Funciones de conversión de tipos*: 
   - int(), float(), str(), bool(): Para convertir valores a enteros, números de punto flotante, cadenas o booleanos, respectivamente.

2. *Funciones matemáticas*:
   - abs(): Devuelve el valor absoluto de un número.
   - round(): Redondea un número al entero más cercano.
   - max(), min(): Devuelven el valor máximo o mínimo de una secuencia de números.
   - sum(): Calcula la suma de una secuencia de números.

3. *Funciones de secuencia*:
   - len(): Devuelve la longitud (número de elementos) de una secuencia.
   - sorted(): Devuelve una lista ordenada a partir de una secuencia.
   - enumerate(): Devuelve una enumeración de índices y elementos de una secuencia.

4. *Funciones de iteración*:
   - map(): Aplica una función a cada elemento de una secuencia.
   - filter(): Filtra elementos de una secuencia según una función de prueba.

5. *Funciones de cadenas*:
   - str.upper(), str.lower(): Convierten una cadena a mayúsculas o minúsculas.
   - str.strip(): Elimina espacios en blanco al inicio y al final de una cadena.

6. *Funciones de entrada/salida*:
   - print(): Imprime mensajes en la consola.
   - input(): Lee una entrada del usuario desde la consola.

7. *Funciones de gestión de archivos*:
   - open(): Abre un archivo para lectura, escritura o ambos.

Estas funciones son esenciales y proporcionan funcionalidades básicas y útiles para una variedad de tareas de programación en Python. Además de estas, Python también proporciona módulos estándar y funciones definidas por el usuario que pueden extender aún más las capacidades del lenguaje.
