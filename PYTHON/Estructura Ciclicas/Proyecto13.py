#Diseñar una app que al ingresar un numero entero positivo, muestre por pantalla todos los numeros impares desde uno hasta el numero ingresado
n=int(input("Digite un numero entero: "))
for i in range(1,n,2):
    print(i, end=", ")