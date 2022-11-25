var a,b 
var i 



a=parseInt(prompt("Ingrese el valor inicial"))
b=parseInt(prompt("Ingrese el valo final"))

i=a

while(i<=b){
    if (i%2==0) {
        document.write(i+"<br>")
    }else{
        document.write("<br>")
    }
    
    i++

}