var peso, estatura, imc;

peso=parseFloat(prompt("Digite el peso en Kg: "));
estatura=parseFloat(prompt("Digite la estatura en Mts: "));

imc=peso/(estatura*estatura);
if (imc<18.5) {
    document.write("Bajo Peso  <img src='img/bajopeso.jpg' alt='bajo peso' width='30px' height='30px'> "); 
}
else if (imc>=18.5 && imc<24.9 ){
    document.write("Peso Normal   <img src='img/pesonormal.jpg' alt='peso normar' width='30px' height='30px'>");
}
else if (imc>=25 && imc<29.9 ){
    document.write("Sobrepeso    <img src='img/sobrepeso.jpg' alt='sobrepeso' width='30px' height='30px'>");
} 
else if (imc>=30 && imc<34.9 ){
    document.write("Obesidad I    <img src='img/obesidad1.png' alt='obesidad I' width='30px' height='30px'>");
}    
else if (imc>=35 && imc<39.9 ){
    document.write("Obesidad II     <img src='img/obesidad2.jpg' alt='obesidad II' width='30px' height='30px'> ");
}   
else if (imc>=40 && imc<49.9 ){
    document.write("Obesidad III    <img src='img/obesidad3.jpg' alt='obesidad III' width='30px' height='30px'>");
} else if (imc>=50 ){
    document.write("Obesidad IV    <img src='img/obesidad4.png' alt='obesidad IV' width='30px' height='30px'>");
}  
else {
    document.write("Escriba los valores numericos esperados...");
}      



