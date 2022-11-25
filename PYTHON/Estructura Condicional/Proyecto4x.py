#app Presion Arterial
from operator import ilshift


presion=int(input("Ingrese la presion arterial de la persona: "))

if presion<90:
    print("Presion Baja")
elif presion>=90 and presion<120:
    print("Presion Normal")
elif presion>=120 and presion<140:
    print("Prehipertension")
elif presion>=140 and presion<160:
    print("Alta: Hipertension Fase 1")
elif presion>=60:
    print("Alta: Hipertension Fase 2")
else:
     print("Ingrese una presion arterial valida")