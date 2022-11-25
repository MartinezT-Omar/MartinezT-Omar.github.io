#4diseñe una app con una funcion que calcule el area del cuadrado y luego sea llamada por un algoritmo
#FUNCION CON PARAMETROS
#FUNCION AREA DE UN Cuadrado
def cuadrado(l):
    area=l*2
    print("El area del cuadrado es: ",area)


#algoritmo para llamar a la funcion
#app area del cuadrado

lado=float(input("Ingrese la longitud del lado cuadrado: "))

cuadrado(lado)