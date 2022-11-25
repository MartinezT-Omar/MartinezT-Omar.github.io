#Diseñe una app que almacene los datos de un sistema de facturación; para ello se deben crear las siguientes listas vacías, alimentarlas y mostrarlas
#lista vacias
codigodefactura=[]
codigodecliente=[]
nombredelcliente=[]
fechas=[]
descripciondelproducto=[]
precios=[]
cantidades=[]
totales=[]
#Definimos un tamaño para las listas
tamaño=int(input("Tamaño de la Lista?: "))
#recorremoa la lista hasta el tamaño definido
for i in range(tamaño):
    print("Ingrese los datos de la Factura: ", i+1)
    codfactura=input("Codigo de Factura: ")
    codcliente=input("Codigo del Cliente: ")
    nombre=input("Nombre de Cliente: ")
    fecha=input("Fecha de Factura: ")
    descripcion=input("Descripcion del Producto: ")
    precio=int(input("Precio del Producto: ")) 
    cantidad=int(input("Cantidad del Producto: "))
    codigodefactura.append(codfactura)
    codigodecliente.append(codcliente)
    nombredelcliente.append(nombre)
    fechas.append(fecha)
    descripciondelproducto.append(descripcion)
    precios.append(precio)
    cantidades.append(cantidad)
    total=precio*cantidad
    totales.append(total)


print("Datos de la Factura")
#Ahora mostramos las listas
for i in range(tamaño):
    print("----------------------------------------")
    print("Codigo de Factura: ", codigodefactura[i])
    print("Codigo de Cliente: ", codigodecliente[i])
    print("Nombre del Cliente: ", nombredelcliente[i])
    print("Fecha de Factura: ", fechas[i])
    print("Descripcion del Producto. ", descripciondelproducto[i])
    print("Precio de Producto: ", precios[i])
    print("Cantidad de Producto: ", cantidades[i])
    print("El Total de su compra es: ", totales[i])
   