Proceso SueldoDevengado
	definir sueldo, bonificacion, descuento, auxilio, total como real;
	definir hijos Como Entero;
	escribir "Ingrese el sueldo base del empleado";
	leer sueldo;
	escribir "Ingrese la cantidad de hijos del emleado ";
	leer hijos;
	bonificacion<-(hijos*0.05)*sueldo;
	descuento<-(sueldo*0.04);
	auxilio<-(sueldo*0.10);
	total<-(sueldo+bonificacion-descuento+auxilio);
	escribir "La bonificacion del 5% por cada hijo es ", bonificacion;
	escribir "El descuento del 4% de S.s es ", descuento;
	escribir "El 10% de auxilio de transporte otorgado es ", auxilio;
	escribir "El sueldo final del empleado es ", total;
	
	
	
	
	
	
	
FinProceso
