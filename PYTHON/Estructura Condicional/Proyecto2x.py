#Almacen de Zapatos
precio=float(input("Ingrese el presio de los Zapatos: "))
cantidad=int(input("Ingrese la cantidad de Zaatos: "))
operacion=precio*cantidad

if cantidad<10:
    print("El cliente no obtuvo un descuento sobre el total de la compra ")
elif cantidad>=10 and cantidad<20:
    descuento=operacion*0.10
    print("El cliente obtuvo un descuento de 10% que es $", descuento, " sobre el total de la compra ")
    total=operacion-descuento
    print("El cliente debe pagar un total de: $", total)
elif cantidad>=20 and cantidad<30:
    descuento=operacion*0.20
    print("El cliente obtuvo un descuento de 20% que es $", descuento, " sobre el total de la compra ")
    total=operacion-descuento
    print("El cliente debe pagar un total de: $", total)
elif cantidad>=30:
    descuento=operacion*0.40
    print("El cliente obtuvo un decuento de 40% que es $", descuento, " sobre el total de la compra ")
    total=operacion-descuento
    print("El cliente debe pagar un total de: $", total)
else:
    print("Ingrese una cantidad valida")
