// importações
const express = require('express')
require('dotenv').config()
const cors = require('cors')
const app = express()
const pg = require('pg')
const port = 3000
const dataBase = 'postgres://cdtdwmpa:zBP4D7ZGZUxhJqKnWnmOmYwcXszjTWqp@isabelle.db.elephantsql.com/cdtdwmpa'
//para permitir que o frontEnd faça requisiçoes
app.use((req,res,next) => {
  res.header("Access-Control-Allow-Origin","*")
  app.use(cors)
  next()
})

// requisições para buscar editais com o cpf do candidato

app.get('/getProfissoesDoCandidato/:cpf', (req, res) => {
  const CPF = req.params.cpf; 
  const cliente = new pg.Client(dataBase)

  cliente.connect(function(err) { 
    if(err) {
      return console.error('could not connect to postgres', err)
    }
    let cpf = "'" + CPF + "'"
    cliente.query('SELECT profissao FROM "public"."candidato" where cpf = ' + cpf +';', function(err, result) {
      if(err) {
        console.error('error running query', err)
      }
      let profissoes = result.rows[0]["profissao"].split(",")
      cliente.end();
      res.json(profissoes)
    })
  })
})
app.get('/getEditaisCompativeis/:cpf', (req, res) => {
  const CPF = req.params.cpf; 
  let cliente = new pg.Client(dataBase)
  let profissoes = []
  let vagasCompativeis = []

  cliente.connect(function(err) { 
    if(err) {
      return console.error('could not connect to postgres', err)
    }
    let cpf = "'" + CPF + "'";
    

    cliente.query('SELECT profissao FROM "public"."candidato" where cpf = ' + cpf +';', function(err, result) {
      if(err) {
        console.error('error running query', err)
      }
      // profissoes.push(result.rows[0].split(','))

      for(let posicao_profissao = 0; posicao_profissao<profissoes.lenght;posicao_profissao++){
        let profissao = "'%" + profissoes[posicao_profissao]+ "%'"
        cliente.end();
        res.json(profissao)
        
        cliente.query('SELECT orgao,edital,codigo_concurso FROM "public"."concurso" where lista_vagas like '+ profissao+';', function(err, result2) {
          if(err) {
            console.error('error running query', err)
          }
          vagasCompativeis.push(result2.rows.json())

          
        })
      }
    })
  })
  
  // console.log(vagasCompativeis)
  let vagasCompativeisUnicas = new Set(vagasCompativeis)
  let editaisCompativeis = Array.from(vagasCompativeisUnicas)
  


})
  
// requisições para buscar candidatos com código do edital

app.get('/getVagasDoEdital/:cod', (req, res) => {
  const cod = req.params.cod; 

  const cliente = new pg.Client(dataBase)
  cliente.connect(function(err) { 
    if(err) {
      console.error('could not connect to postgres', err)
    }
    let codigo = "'" + cod + "'"
    cliente.query('SELECT lista_vagas FROM "public"."concurso" where codigo_concurso = '+codigo+';', function(err, result) {
      if(err) {
        console.error('error running query', err)
      }
      // let vagas = result.rows[0]["lista_vagas"].split(",")
      cliente.end();
      let vagas = new Set(result.rows[0]["lista_vagas"].split(","))
      let vagasCompativeis = Array.from(vagas)
      res.json(vagasCompativeis)
    })
  })
})

app.get('/getCandidatosQualificados/:vaga',(req,res) => {
  const vaga = req.params.vaga;

  const cliente = new pg.Client(dataBase)
  cliente.connect(function(err) { 
    if(err) {
      console.error('could not connect to postgres', err)
    }
    let vagaParaPreencher = "'%" + vaga + "%'"
    cliente.query('SELECT nome,data_nascimento,cpf FROM "public"."candidato" where profissao like '+ vagaParaPreencher +';', function(err, result) {
      if(err) {
        console.error('error running query', err)
      }
      
      cliente.end();
      res.json(result.rows)
    })
  })
})



app.listen(port)
