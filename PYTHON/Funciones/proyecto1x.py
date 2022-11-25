#Funciones Con PARAMETROS 
"""Escribir una funcion a la que se le pase una cadena <nombre> 
y muestre por pantalla el Saludo  ¡Hola <nombre>!"""

#funcion de saludo

def saludo(name):
    print("Hola ", name)

#app que ingrese el nombre y lo muestre como saludo
nombre=input("Cual es sunombre? ")
saludo(nombre) #llamando a la funcion