#LISTAS VACIAS

#Creamos las listas (vacias al comienzo

nombres=[]
identificacion=[]
FechaNacimiento=[]
LugarNacimiento=[]
direcciones=[]
correos=[]
#Definimos un tamaño para las listas
#lo puedes cambiar si quieres
tamaño=int(input("Tamaño de la Lista?: "))
#recorremoa la lista hasta el tamaño definido
for i in range(tamaño):
    print("Ingrese los datos del Aprendiz: ", i+1)
    nombre=input("Nombre del Aprendiz: ")
    id=int(input("N° de Identificacion: "))
    fn=input("Fecha d Nacimiento: ")
    ln=input("Lugar de Nacimiento: ")
    direccion=input("Direccion: ")
    correo=input("Correo electronico: ")
    nombres.append(nombre)
    identificacion.append(id)
    FechaNacimiento.append(fn)
    LugarNacimiento.append(ln)
    direcciones.append(direccion)
    correos.append(correo)
print("Los Aprendices son: ")
#Ahora mostramos las listas
for i in range(tamaño):
    print("----------------------------------------")
    print("Nombre: ", nombres[i])
    print("Indentificacion: ", identificacion[i])
    print("Fecha de Nacimiento: ", FechaNacimiento[i])
    print("Lugar de Nacimiento: ", LugarNacimiento[i])
    print("Direccion: ", direcciones[i])
    print("Correo Electronico: ", correos[i])


