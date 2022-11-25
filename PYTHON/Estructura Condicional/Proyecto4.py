#app que al ingresar una temperatura en ºC y diga si el paciente
# tiene FIEBRE con una temperatura mayor igual a 38 o tiene una
#TEMPERATURA NORMAL.
tem=int(input("Ingrese la temperatura en °C"))

if tem>=38:
    print("La persona tiene FIEBRE")
else:
    print("La persona tiene una TEMPERATURA NORMA")