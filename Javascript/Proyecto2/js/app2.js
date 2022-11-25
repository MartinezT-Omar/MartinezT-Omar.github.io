//Aplicacion para evaluar si un numero esta entre 10 y 100
var n;

n=parseInt(prompt("Digite el numero entero: "));

//Evaluamos el proceso numerico
if (n>=10 && n<=100) {
    document.write("El numero "+n+" esta entre 10 y 100     <img src='img/entre10y100.png' alt='' width='45px' height='45px'>");
} else {
    document.write("El numero "+n+" no esta entre 10 y 100    <img src='img/fuerade10y100.png' alt='' width='45px' height='45px'>");
}