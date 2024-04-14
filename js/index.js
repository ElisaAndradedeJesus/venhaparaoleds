const cpfOuCodigo= document.getElementById("cpfOuCodigo");
const buscarEditais = document.getElementById("buscarEditais");
const buscarCandidatos = document.getElementById("buscarCandidatos");

const campoVazio = document.getElementById("campoVazio");
const valorInvalido = document.getElementById("valorInvalido");
const naoCadastrado = document.getElementById("naoCadastrado");

function contador(string){
    let cont = 0;
    let s = ''
    for(var x in string){
        s= s+x;
        cont =  cont+1;
    }
    return cont;
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
    console.log(cont);
    if((cont < 11) || (cont> 14)){
        valorInvalido.style.display = "flex";
        e.preventDefault();
    } else {
        valorInvalido.style.display = "none";
    }

}

buscarEditais.addEventListener("click", function(e) {
    validarCampo(e);

  });

buscarCandidatos.addEventListener("click", function(e) {
    validarCampo(e);
    
  })