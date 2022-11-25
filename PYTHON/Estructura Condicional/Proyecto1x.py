""" Evaluar la edad ingresado
0>= y <2, Eres Baby
2>= y <12, Eres un Niño(a)
12>= y <=17, Eres un Adolescente
18>= y <40, Eres un Adulto Joven
40>= y <60, Eres un Adulto Maduro
>=60, Eres un Adulto Mayor
"""

edad=int(input("Ingrese la edad: "))
if edad>=0 and edad<2:
    print("Eres un Baby")
elif edad>=2 and edad<12:
    print("Eres un Niño(a)")
elif edad>=12 and edad<=17:
    print("Eres un Adolescemte")
elif edad>=18 and edad<40:
    print("Eres un Adulto Joven")
elif edad>=40 and edad<60:
    print("Eres un Adulto Maduro")
elif edad>=60:
    print("Eres un Adulto Mayor")
else: 
    print("Esto no es una edad...por favor verifique")