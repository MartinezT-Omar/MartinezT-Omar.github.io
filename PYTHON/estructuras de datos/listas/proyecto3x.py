#Diseñe una app que almacene los datos de un vehículo, para ello debe crear las siguientes listas vacías, alimentarlas y mostrar por pantalla

#Listas vacias:
marcas=[]
modelos=[]
colores=[]
combustibles=[]
cilindrajes=[]
precios=[]
#Definimos un tamaño para las listas
#lo puedes cambiar si quieres
tamaño=int(input("Tamaño de la Lista?: "))
#recorremoa la lista hasta el tamaño definido
for i in range(tamaño):
    print("Ingrese los datos del vehiculo: ", i+1)
    marca=input("Marca: ")
    modelo=input("Modelo: ")
    color=input("Color: ")
    combustible=input("Combustible: ")
    cilindraje=input("Cilindraje: ")
    precio=int(input("Precio: ")) 
    marcas.append(marca)
    modelos.append(modelo)
    colores.append(color)
    combustibles.append(combustible)
    cilindrajes.append(cilindraje)
    precios.append(precio)
print("Datos de Vehiculo(s)")
#Ahora mostramos las listas
for i in range(tamaño):
    print("----------------------------------------")
    print("Marca: ", marcas[i])
    print("Modelo: ", modelos[i])
    print("Color: ", colores[i])
    print("Combustible: ", combustibles[i])
    print("Cilindraje: ", cilindrajes[i])
    print("Precio: ", precios[i])

    