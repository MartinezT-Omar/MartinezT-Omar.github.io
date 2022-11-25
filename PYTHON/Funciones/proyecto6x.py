#2diseñe un app con una funcion que calcule el area del triangulo y luego sea llamada por un algoritmo
#FUNCION CON PARAMETROS
#FUNCION AREA DE UN TRIANGULO
def triangulo(b, h):
    area=(b*h)/2
    print("El area del triangulo es: ",area)


#algoritmo para llamar a la funcion
#app area del rectangulo

base=float(input("Ingrese la base del triangulo: "))
altura=float(input("Ingrese la altura del triangulo: "))

triangulo(base, altura)