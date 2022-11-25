//Aplicacion para Aprobar o Reprobar
var nota;

nota=parseFloat(prompt("Ingrese la nota del Alumno"));

//Proceso aprobado o reprobado
if (nota>=3) {
    document.write("El alumno aprobó   <img src='img/aprobado.jpg' alt='' width='45px' height='45px'>");
} else {
    document.write("El alumno reprobó   <img src='img/reprobado.jpg' alt='' width='45px' height='45px'>");
}