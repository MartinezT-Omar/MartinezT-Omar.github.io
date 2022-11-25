/*39. Diseñe un algoritmo que muestre un menú donde las opciones sean 
“1. Suma”
“2. Resta”
“3. Multiplicación”
“4. División” */


var op;
var n1, n2, resultado;

op=parseInt(prompt("Escoja una opcion del menu "));

switch (op) {
    case 1:
        n1=parseInt(prompt("Digite el 1er numero: "));
        n2=parseInt(prompt("Digite el 2do numero: "));
        resultado=n1+n2;
        document.write("La suma de: "+n1+" + "+n2+" = "+resultado);
        
    break;
    case 2:
        n1=parseInt(prompt("Digite el 1er numero: "));
        n2=parseInt(prompt("Digite el 2do numero: "));
        resultado=n1-n2;
        document.write("La resta de: "+n1+" - "+n2+" = "+resultado);
        

    break;
    case 3:
        n1=parseInt(prompt("Digite el 1er numero: "));
        n2=parseInt(prompt("Digite el 2do numero: "));
        resultado=n1*n2;
        document.write("La multiplicacion de: "+n1+" * "+n2+" = "+resultado);
        

    break;
    case 4:
        n1=parseFloat(prompt("Digite el 1er numero: "));
        n2=parseFloat(prompt("Digite el 2do numero: "));
        resultado=n1/n2;
        document.write("La division de: "+n1+" / "+n2+" = "+resultado);
        

    break;
    

    default:
        document.write("Escoja una opcion valida.");
        break;
}