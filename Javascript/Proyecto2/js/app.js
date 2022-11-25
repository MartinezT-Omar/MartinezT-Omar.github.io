//Aplicacion para evaluar la Fiebre de una persona
var temp;

//Capturar los datos de entrada
temp=parseFloat(prompt("Ingrese su temperatura °C: "));

//Proceso para evaluar la fiebre
if (temp>=38) {
    document.write("La temperatura "+temp+"°C Indica Fiebre      <img src='img/temperatura.png' alt='' width='45px' height='45px'>");
} else {
    document.write("La temperatura "+temp+"°C Indica sin Fiebre   <img src='img/sana.png' alt='' width='45px' height='45px'>");
}
    