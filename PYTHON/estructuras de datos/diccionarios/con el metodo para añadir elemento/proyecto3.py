"""
Diseñe una app que permita almacenar la información de los clientes de una empresa. 
Los clientes se guardarán en un diccionario llamado clientes. Los datos deben ser ingresados por el usuario:
Identificación del cliente, nombre, dirección, teléfono, correo y empresa.
La app debe preguntar al usuario por una opción del menú.
1.	Añadir cliente.
2.	Mostrar cliente.
3.	Eliminar Cliente.
4.	Finalizar. 
"""
cliente={}
op=""

while op !=4:
    if op==1:
        identificacion=int(input("Digite la Identificacion: "))
        nombre=input("Digite su Nombre: ")
        direccion=input("Digite su Direccion: ")
        telefono=int(input("Digite su Telefono: "))
        correo=input("Digite su Correo: ")
        empresa=input("Digite su Empresa: ")
        cliente={
           "identificacion":identificacion, 
           "nombre":nombre, 
           "direccion":direccion, 
           "telefono":telefono, 
           "correo":correo, 
           "empresa":empresa} 
    if op==2:
        print("Informacion del Cliente")
        print("-----------------------")
        print("Identificacion:", cliente["identificacion"])
        print("Nombre:", cliente["nombre"])
        print("Direccion:", cliente["direccion"])
        print("Telefono:", cliente["telefono"])
        print("Correo:", cliente["correo"])
        print("Empresa:", cliente["empresa"])
        
    if op==3:
        del cliente["identificacion"]
        print("Cliente Eliminado con Exito!")
    if op==4:
        exit()


    print("----------MENÚ---------")
    print("1. AÑADIR CLINTE.")
    print("2. MOSTRAR CLIENTE.")
    print("3. ELIMINAR CLIENTE.")
    print("4. FINALIZAR.")

    op=int(input("Seleccione una opcion: "))
    

