"""
Diseñe una app que permita al usuario ingresar fruta y el precio unitario, 
cantidad, y lo almacene en un diccionario llamado factura. 
Después debe mostrar un mensaje concadenado donde aparece el nombre de la fruta, su valor, la cantidad y el total
"""

fruta=input("Ingrese el nombre de la Fruta: ")
precio=int(input("Digite el precio de la Fruta: "))
cantidad=int(input("Digite la cantidad que desea llevar: ")) 
total=precio*cantidad

factura={"Fruta":fruta, "precio":precio, "cantidad":cantidad, "total":total}

print("El nombre de la Fruta es:", factura["Fruta"], 
", su precio es:", factura["precio"], 
", la cantidad que desea llevar es:", factura["cantidad"], 
"y su total es:", factura["total"])
