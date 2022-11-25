"""Array vector: Eliminar un elemento del vector.
primera forma:
variable.pop(x)
segunda forma:
variable.remove(X)
"""


# lista
print("Lista de Frutas: ")
frutas=["apple", "banana", "cherry"]
#añadimos un elemento a la  lista
frutas.append("Orange")
#eliminar un elemento
frutas.pop(1)
#recorremos la lista
for x in frutas:
    print(x)
#definimos la longitud de la lista
longitud=len(frutas)
print("El tamaño o longitud es: ", longitud)


#listas de libros con siete posiciones
print("Lista de Libros: ")
libros=["cien años de soledad", "Crónica de una muerte anunciada", "El coronel no tiene quien le escriba", "Relato de un náufrago", "El amor en los tiempos del cólera", "El coronel no tiene quien le escriba", 
"Del amor y otros demonios"]
#añadimos un elemento a la  lista
libros.append("El principito")
#eliminar un elemento
libros.remove("cien años de soledad")
#recorremos la lista
for x in libros:
    print(x)
#definimos la longitud de la lista
longitud=len(libros)
print("El tamaño o longitud es: ", longitud)


#lista de plantas medicinales con nueve posiciones
print("Lista de Plantas Medicinales: ")
plantas=["Marihuana", "Manzanilla", "Ají", "Ajo", "Eucalipto", "Orégano", "Menta", "Toronjil", "Sábila"]
#añadimos un elemento a la  lista
plantas.append("Anís")
#eliminar un elemento
plantas.pop(1)
#recorremos la lista
for x in plantas:
    print(x)
#definimos la longitud de la lista
longitud=len(plantas)
print("El tamaño o longitud es: ", longitud)



#lista de lenguaje de programacion con cinco posiciones
print("Lista de Lenguajes de Programacion: ")
lenguaje=["Java", "Python", "Java Script", "C++", "PHP"]
#añadimos un elemento a la  lista
lenguaje.append("SQL")
#eliminar un elemento
lenguaje.remove("Java")
#recorremos la lista
for x in lenguaje:
    print(x)
#definimos la longitud de la lista
longitud=len(lenguaje)
print("El tamaño o longitud es: ", longitud)



#Lista de colores con 8 posiciones.
print("Lista de Colores: ")
colores=["Azul", "Rojo", "Verde", "Amarillo", "Naranja", "Morado", "Negro", "Blanco"]
#añadimos un elemento a la  lista
colores.append("Gris")
#eliminar un elemento
colores.pop(1)
#recorremos la lista
for x in colores:
    print(x)
#definimos la longitud de la lista
longitud=len(colores)
print("El tamaño o longitud es: ", longitud)