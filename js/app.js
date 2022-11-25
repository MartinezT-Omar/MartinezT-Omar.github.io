function validaCampos(){
    var formulario;
    formulario=document.formUser;
    //valida el campo usuario
    if (formulario.user.value != "omar"  ) {
        //valida si el campo esta vacio
        document.getElementById("validaUser").innerHTML="Favor escribir el usuario";
        //se posiciona en el campo user
        formulario.user.focus();
        return false;
        
    }else{
        document.getElementById("validaUser").innerHTML="";
    }
    // valida el campo password
    if (formulario.password.value != "omar") {
        //valida si el campo esta vacio
        document.getElementById("validaPassword").innerHTML="Favor escribir su password";
        //se posiciona en el campo password
        formulario.password.focus();
        return false;
        
    }else{
        document.getElementById("validaPassword").innerHTML="";
    }

    

    formulario.submit();

}