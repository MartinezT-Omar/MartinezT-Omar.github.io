#Diseñe una app que almacene los datos de una tienda de películas, para ello debe crear las siguientes lista vacías

#lista vacias
peliculas=[]
generos=[]
duraciones=[]
protagonistas=[]
estrenos=[]
precios=[]
idiomas=[]
#Definimos un tamaño para las listas
tamaño=int(input("Tamaño de la Lista?: "))
#recorremoa la lista hasta el tamaño definido
for i in range(tamaño):
    print("Ingrese los datos de la Pelicula: ", i+1)
    pelicula=input("Titulo de la Pelicula: ")
    genero=input("Genero de la Pelicula: ")
    duracion=input("Duracion de la Pelicula: ")
    protagonista=input("Protagonista de la Pelicula: ")
    estreno=input("Año de estreno de la Pelicula: ")
    precio=input("Precio de la Pelicula: ")
    idioma=input("Idioma de la Pelicula: ")
    peliculas.append(pelicula)
    generos.append(genero)
    duraciones.append(duracion)
    protagonistas.append(protagonista)
    estrenos.append(estreno)
    precios.append(precio)
    idiomas.append(idioma)
print("Datos de Pelicula(s)")
#Ahora mostramos las listas
for i in range(tamaño):
    print("----------------------------------------")
    print("Titulo de la Pelicula: ", peliculas[i])
    print("Genero de la Pelicula: ", generos[i])
    print("Duracion de la Pelicula: ", duraciones[i])
    print("Protagonis de la Pelicula: ", protagonistas[i])
    print("Año de Estreno de la Pelicula: ", estrenos[i])
    print("Precio de la Pelicula: ", precios[i])
    print("Idioma de la Pelicula: ", idiomas[i])