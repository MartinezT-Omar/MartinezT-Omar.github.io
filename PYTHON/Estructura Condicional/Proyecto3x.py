#Formula IMC
peso=int(input("Ingrese el peso de la persona: "))
estatura=float(input("Ingrese la estatura de la persona: "))

imc=peso/(estatura*estatura)

if imc<18.5:
    print("Bajo Peso")
elif imc>=18.5 and imc<25:
    print("Peso Normal")
elif imc>=25 and imc<30:
    print("Sobrepeso")
elif imc>=30 and imc<35:
    print("Obesidad I")
elif imc>=35 and imc<40:
    print("Obesidad II")
elif imc>=40 and imc<50:
    print("Obesidad III")
elif imc>=50:
    print("Obesidad IV")
else:
    print("Ingrese una edad valida")