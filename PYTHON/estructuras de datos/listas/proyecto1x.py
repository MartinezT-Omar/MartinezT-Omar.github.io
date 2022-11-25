#LISTAS VACIAS

#Creamos las listas (vacias al comienzo

nombres=[]
#Definimos un tamaño para las listas
#lo puedes cambiar si quieres
tamaño=int(input("Tamaño de la Lista?: "))
#recorremoa la lista hasta el tamaño definido
for i in range(tamaño):
    print("Ingrese los datos del Aprendiz: ", i+1)
    nombre=input("Nombre del Aprendiz: ")
    nombres.append(nombre)
print("Los Aprendices son: ")
#Ahora mostramos las listas
for i in range(tamaño):
    print("----------------------------------------")
    print("Nombre: ", nombres[i])

