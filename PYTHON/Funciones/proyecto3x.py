#FUNCION CON PARAMETROS
#funcion calculadora
def calculadora(n1,n2):
    suma=n1+n2
    print("La suma es: ", suma)

    resta=n1-n2
    print("La resta es: ", resta)

    multiplicacion=n1*n2
    print("La Multiplicacion es: ", multiplicacion)

    division=n1/n2
    print("La division es: ", division)



#algoritmo para llamar a la funcion
#app calculadora

a=int(input("Digite el 1er numero: "))
b=int(input("Digite el 2do numero: "))

calculadora(a, b)
