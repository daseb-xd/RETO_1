# Reto 1 POO 2025-1
Cada item del reto esta debidamente comentado en su respectivo código, se realizo con funciones vistas en clase y con algunas investigadas y aprendidas por cuenta propia.

## 1. Calculadora de operaciones básicas
La funcion principal recibe 3 valores, 2 floats y un string.
La funcion compara el símbolo recibido como string con las operaciones correspondientes y realiza la operacion, si el simbolo no esta en la función, devuelve un mensaje de error y no hace nada.

## 2. Verificador de palíndromos
La función principal recibe una palabra como string y la convierte a minúsculas para evitar bugs por mayúsculas. Luego invierte la palabra usando un bucle `for` que recorre la cadena desde el final hasta el principio. Al final se usa un `match-case` para comparar la palabra original con su forma invertida. Si ambas son iguales, devuelve un mensaje indicando que es un palíndromo; en caso contrario, indica que no lo es.

## 3. Devolver números primos
La función principal recibe una lista de números en formato string, los convierte a enteros y evalúa cuáles son primos. Para cada número, se descartan los menores a 2 y se verifica si tiene divisores distintos de 1 y él mismo, evaluando solo hasta su raíz cuadrada (esto mejora la eficiencia). Si no se encuentra ningún divisor, se considera primo y se agrega a una nueva lista con un ciclo `for`. Cuando termina, la función retorna la lista con todos los números primos encontrados.

## Verificador de sumas
La función principal solicita una lista de números enteros desde la entrada del usuario, los convierte usando `map(int, ...)` y luego calcula la suma de cada par de números consecutivos. Para evitar errores en la funcion `enumerate()`, se excluye el último elemento del bucle. Cada suma se almacena en una nueva lista, y al final se imprime el valor más alto usando `max()`. 

## Verificador de angramas
La función recibe una lista de palabras y agrupa todas las que tienen las mismas letras, sin importar el orden. Convierte cada palabra a minúsculas y ordena sus letras con `sorted()`. Las palabras con las mismas letras ordenadas se agrupan en un diccionario. Luego, se recorren los grupos creados y si hay más de una palabra en un grupo, se consideran anagramas. Estas se agregan a un set para evitar duplicados, y el set final se imprime como el output.
