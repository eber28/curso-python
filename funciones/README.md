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
