Proceso terreno
	definir metro2, precio, monto, inicial, cuota Como Real;
	escribir "Digite la cantidad de metros cuadrados que desea comprar del terreno ";
	leer metro2;
	precio<-1000000;
	monto<-(metro2*precio);
	inicial<-(monto*0.30);
	cuota<-(monto*0.70)/12;
	
	escribir "El monto total del terreno es ", monto;
	escribir "La cuota inicial del 30% que debe dar el cliente es ", inicial;
	escribir "El cliente debe pagar 12 cuotas, cada cuota equivale a ", cuota;
	
	
FinProceso
