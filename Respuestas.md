### Respuestas

1. **¿Cuál es la diferencia entre una lista y una tupla en Python?**
   - Una lista es como una mochila donde puedes cambiar lo que llevas dentro en cualquier momento. Una tupla es como una caja sellada que no puedes modificar una vez que la has llenado.
     ```python
     mi_lista = [1, 2, 3]  
     mi_tupla = (1, 2, 3)  
     ```

2. **Orden de las operaciones en Python**

- En Python el orden a seguir es:

1. **Primero los parentesis**: Si hay parentesis primero se resuelven
2. **Exponentes**: Luego, si hay exponentes, se resuelven.
3. **Multiplicación y división**: Después, se hacen las multiplicaciones y divisiones en el orden en que aparecen.
4. **Por último, sumas y restas**: Se realizan las sumas y restas, también en el orden en que aparecen.

Por ejemplo:
```python
resultado = 2 + 3 * 4  # Primero se multiplica 3 por 4, luego se suma 2
print(resultado)       # Resultado 14


3. **¿Qué es un diccionario Python?**
   - Un diccionario es como un libro donde buscas información usando palabras clave en lugar de números de página. Cada palabra clave tiene una definición única.
     ```python
     mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
     print(mi_diccionario["nombre"])  # Salida: Juan
     ```

4. **¿Cuál es la diferencia entre el método ordenado y la función de ordenación?**
   - La función `sorted()` y el método `sort()` hacen lo mismo: ordenar elementos. La diferencia es que la función `sorted()` funciona con cualquier grupo de cosas y devuelve una lista ordenada, mientras que`sort()` es solo para listas y ordena la lista en su lugar.
     ```python
     mi_lista = [3, 1, 2]
     nueva_lista = sorted(mi_lista)
     print(nueva_lista)  # Salida: [1, 2, 3]
     ```

5. **¿Qué es un operador de reasignación?**
   - Un operador de reasignación es como un mago que cambia el valor de una variable. Por ejemplo, si `x` es igual a 5 y le dices `x += 1`, ahora `x` será igual a 6.
     ```python
     x = 5
     x += 1
     print(x)  # Salida: 6
     ```
