#3diseñe una app con una funcion que calcule el area del circulo y luego sea llamada por un algoritmo
#FUNCION CON PARAMETRO
#FUNCION AREA DE UN CIRCULO
def circulo(r):
    area=(r*2)/3.14
    print("El area del circulo es: ",area)


#algoritmo para llamar a la funcion
#app area del circulo

radio=float(input("Ingrese el radio del circulo: "))

circulo(radio)