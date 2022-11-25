#1 diseña una app que calcule el area de rectangullo y luego sea llamada por un algoritmo

#FUNCION CON PARAMETROS
##FUNCION AREA DEL RECTANGULO
def rectangulo(b, h):
    area=b*h
    print("El area del rectangulo es: ",area)


#algoritmo para llamar a la funcion
#app area del rectangulo

base=float(input("Ingrese la base del rectangulo: "))
altura=float(input("Ingrese la altura del rectangulo: "))

rectangulo(base, altura)