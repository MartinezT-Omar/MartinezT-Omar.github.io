var a,b 
var i 

a=parseInt(prompt("Ingrese el valor inicial"))
b=parseInt(prompt("Ingrese el valo final"))

for(i=a; i<=b; i++){
   
    if (i%2==0) {
        document.write(i)
    }else{
        document.write("<br>")
    }
   
}