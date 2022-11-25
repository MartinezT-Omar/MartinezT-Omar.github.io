#Los tramites de impuestos para la declaración de la renta en el gobierno vigente

anual=int(input("Ingrese su valor de renta anual: "))

if anual<100000000:
    impuesto=anual*0.05
    print("Menos de 100000000")
    print("Descuento: ", impuesto)
elif anual>=100000000 and anual<200000000:
    impuesto=anual*0.15
    print("Entre 100000000 y 200000000")
    print("Descuento: ", impuesto)
elif anual>=200000000 and anual<350000000:
    impuesto=anual*0.20
    print("Entre 200000000 y 350000000")
    print("Descuento: ", impuesto)
elif anual>=200000000 and anual<350000000:
    impuesto=anual*0.20
    print("Entre 200000000 y 350000000")
    print("Descuento: ", impuesto)
elif anual>=350000000 and anual<600000000:
    impuesto=anual*0.30
    print("Entre 350000000 y 600000000")
    print("Descuento: ", impuesto)
elif anual>=600000000:
    impuesto=anual*0.45
    print("Mayor a 600000000")
    print("Descuento: ",impuesto)
else:
    print("Ingrese un valor de renta valida")

