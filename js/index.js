const cpfOuCodigo= document.getElementById("cpfOuCodigo");
const buscarEditais = document.getElementById("buscarEditais");
const buscarCandidatos = document.getElementById("buscarCandidatos");

const campoVazio = document.getElementById("campoVazio");
const valorInvalido = document.getElementById("valorInvalido");
const naoCadastrado = document.getElementById("naoCadastrado");

const url = "http://localhost:3000/"

function contador(string){
    let cont = 0;
    let s = ''
    for(var x in string){
        s= s+x;
        cont =  cont+1;
    }
    return cont;
}

function getEditais(){
    let body = {
        "cpf":cpfOuCodigo.value
    }
    let request = new XMLHttpRequest();
    request.open("GET",url + "buscarEditais",true);
    request.setRequestHeader("Content-type","application/json");
    request.send(body)

    request.onload = function(){
        console.log(this.responseText)
        console.log(this.response)
    }

}

function getCandidatos(){
    let request = new XMLHttpRequest();
    request.open("GET",url + "buscarCandidatos/"+ cpfOuCodigo.value,true);
    request.onload = function(){
        console.log(responseText);
    }

}

function validarCampo(e){

    if (cpfOuCodigo.value == 0){
        campoVazio.style.display = "flex";  
        e.preventDefault(); 
    } else {
        campoVazio.style.display = "none";
        e.preventDefault(); 
    }
    let cont = contador(cpfOuCodigo.value);
    if((cont != 0 && (cont < 11) || (cont> 14))){
        valorInvalido.style.display = "flex";
        e.preventDefault();
    } else {
        valorInvalido.style.display = "none";
    }

}

buscarEditais.addEventListener("click", function(e) {
    validarCampo(e);
    getEditais();

  });

buscarCandidatos.addEventListener("click", function(e) {
    validarCampo(e);
    getCandidatos();
    
  })