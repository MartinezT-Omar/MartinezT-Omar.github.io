#2diseñe un app con una funcion que calcule el area del triangulo y luego sea llamada por un algoritmo

#FUNCION AREA DE UN TRIANGULO
def triangulo():
    area=(b*h)/2
    print("El area del triangulo es: ",area)


#algoritmo para llamar a la funcion
#app area del rectangulo

b=float(input("Ingrese la base del triangulo: "))
h=float(input("Ingrese la altura del triangulo: "))

triangulo()