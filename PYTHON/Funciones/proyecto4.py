#Fucion de concertir horas a minutos
def convertir():
    minutos=horas*60
    print(horas, " hora es igual a ", minutos, "Minutos")

#-----------------------------------------------------------------------------

#algoritmo para llamar a la funcion
#app convertir
horas=int(input("Ingrese la cantidad de horas que desea convertir a minutos: "))

convertir() ##llamando a la funcion convertir
    