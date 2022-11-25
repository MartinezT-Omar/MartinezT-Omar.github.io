#FUNCION CON PARAMETROS
#funcion convertir
def convertir(h):
    minutos=h*60
    print(h, " hora es igual a ", minutos, "Minutos")

#algoritmo para llamar a la funcion
#app convertir
horas=int(input("Ingrese la cantidad de horas que desea convertir a minutos: "))

convertir(horas) ##llamando a la funcion convertir