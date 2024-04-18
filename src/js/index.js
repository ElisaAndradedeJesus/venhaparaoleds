const cpfOuCodigo= document.getElementById("cpfOuCodigo");
const buscarEditais = document.getElementById("buscarEditais");
const buscarCandidatos = document.getElementById("buscarCandidatos");

const campoVazio = document.getElementById("campoVazio");
const valorInvalido = document.getElementById("valorInvalido");
const naoCadastrado = document.getElementById("naoCadastrado");

const cpfCod = document.getElementById("cpfCod");
const profVaga = document.getElementById("profVaga");
// nomes campos
const identificaCodCPF = document.getElementById("identificaCodCPF");
const profissoes = document.getElementById("profissoes");

const url = "http://localhost:3000/"
let dados = {}
function contador(string){
    let cont = 0;
    let s = ''
    for(var x in string){
        s= s+x;
        cont =  cont+1;
    }
    return cont;
}

function getVagasDoEdital(){
    fetch(url + "getVagasDoEdital/"+ cpfOuCodigo.value)
        .then(response => response.json())
        .then(data => {
            cpfCod.innerHTML = cpfOuCodigo.value
            profVaga.innerHTML = data
            identificaCodCPF.innerHTML = "Código do Edital buscado"
            profissoes.innerHTML = "Vagas apertas para:"

            cpfCod.style.display = "flex"
            profVaga.style.display = "flex"
            identificaCodCPF.style.display = "flex"
            profissoes.style.display = "flex"

            dados["profissoes"] = data
        })
        .catch(error => console.log(error))

}
function fromObjectToArray(){
    // let array = Object.values(dados)
    let array = []
    console.log(array)
    console.log(dados)
    console.log(dados["profissoes"])
    for(let chave in dados){
        array.push(dados[chave])
    }
    console.log(array)
}
function getCandidatos(){
    getVagasDoEdital()
    console.log(dados)
    fromObjectToArray()
    // console.log(fromObjectTOArray)


    for(let i = 0; i < dados["profissoes"].length; i++){
        console.log(dados["profissoes"][i])
    }
    fetch(url+""+cpfOuCodigo.value)
    .then(response => response.json())
    .then(data => {})
    .catch(error => console.log(error))
      

}

function getEditais(){

    let request = new XMLHttpRequest();
    request.open("GET",url + "buscarEditais",false);
    request.setRequestHeader("Content-type","application/json");


    request.onload = function(){
        console.log(this.responseText)
        console.log(this.response)
    }

}
function getProfissoesCandidato(){
    
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
    cpfCod.style.display = "none"
    profVaga.style.display = "none"
    identificaCodCPF.style.display = "none"
    profissoes.style.display = "none"
    validarCampo(e);
    getEditais();

  });

buscarCandidatos.addEventListener("click", function(e) {
    cpfCod.style.display = "none"
    profVaga.style.display = "none"
    identificaCodCPF.style.display = "none"
    profissoes.style.display = "none"
    validarCampo(e);
    getCandidatos();
    
  })