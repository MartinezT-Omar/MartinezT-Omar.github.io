//Aplicacion para evaluar numero Positivo y Negativo
var n;

n=parseInt(prompt("Digite el numero entero: "));

//Evaluar positivo negativo
if (n>=0) {
    document.write("El numero "+n+" es positivo   <img src='img/positivo.jpg' alt='' width='45px' height='45px'>");
    
} else {
    document.write("El numero "+n+" es negativo    <img src='img/negativo.jpg' alt='' width='45px' height='45px'>");
    
}