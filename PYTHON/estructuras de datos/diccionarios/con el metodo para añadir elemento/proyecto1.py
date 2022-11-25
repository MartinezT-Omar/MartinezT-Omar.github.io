"""
Diseñe una app que permita al usuario nombre, edad, dirección y teléfono;
estos datos se deben almacenar en un diccionario llamado persona.
Estos datos se deben mostrar por pantalla de forma concadenada.
EJ:  Juan tiene 17 años, vive en la calle 8 #27’18-A y su número de teléfono es 1234567890
"""

nombre=input("Ingrese su Nombre: ")
edad=input("Digite su Edad: ")
direccion=input("Digite su direccion: ")
telefono=input("Digite su Telefono: ")

persona={"nombre":nombre,"edad":edad, "direccion":direccion, "telefono":telefono}

print(persona["nombre"], 
"tiene:", persona["edad"], "años", 
", vive en:", persona["direccion"], 
", y su numero de telefono es:", persona["telefono"])