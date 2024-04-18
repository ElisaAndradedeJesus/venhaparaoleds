# Teste de admissão para o LEDS

O desafio é desenvolver um programa que permita realizar as seguintes buscas: 
1. Listar os **órgãos, códigos e editais dos concursos públicos** que se encaixam no perfil do candidato, tomando como base o seu **CPF**; 
2. Listar o **nome, data de nascimento e o CPF** dos candidatos que se encaixam no perfil do concurso tomando com base o **Código do Concurso** do concurso público;

O arquivo **candidatos.txt** contém as informações dos candidatos:

| Nome  | Data de Nascimento  | CPF |  Profissões|
|---|---|---|---|
| Lindsey Craft  |  19/05/1976  |  182.845.084-34  |  [carpinteiro]  | 
| Jackie Dawson  |  14/08/1970  |  311.667.973-47  |  [marceneiro, assistente administrativo]  |
| Cory Mendoza |   11/02/1957 |  565.512.353-92  |  [carpinteiro, marceneiro] |

O arquivo **concursos.txt** contém as informações dos concursos públicos:

| Órgão  | Edital  | Código do Concurso | Lista de vagas|
|---|---|---|---|
| SEDU  | 9/2016  |  61828450843  |  [analista de sistemas, marceneiro]  | 
| SEJUS | 15/2017  |  61828450843  |  [carpinteiro,professor de matemática,assistente administrativo] |
| SEJUS | 17/2017 |  95655123539  |  [professor de matemática] |

**Escolha as tecnologias que você usará e monte uma solução completa para rodar a aplicação**.

Para enviar o resultado, basta realizar um **Fork** deste repositório e **abrir um Pull Request** **com seu nome e o número de inscrição**.  

**Atenção: você deve enviar apenas o código fonte. Não serão aceitos códigos compilados**.

Por fim, você deve atualizar o Readme.md com as seguintes informações: 
1. Documentação da solução;
2. Lista dos diferenciais implementados. 


## Avaliação

O programa será avaliado levando em conta os seguintes critérios:

| Critério  | Valor | 
|---|---|
| Legibilidade do Código |  10  |
| Documentação do código |  10  |
| Documentação da solução |  10  |
| Tratamento de Erros | 10 | 
| Total | 40 |

A sua pontuação será a soma dos valores obtidos nos critérios acima.

## Diferenciais 

Você pode aumentar a sua pontuação no processo de seleção implementando um ou mais dos itens abaixo:

| Item  | Pontos Ganhos | 
|---|---|
| Criar um [serviço](https://martinfowler.com/articles/microservices.html) com o problema |  30  |
| Utilizar banco de dados |  30  |
| Implementar Clean Code |  20  |
| Implementar o padrão de programação da tecnologia escolhida |  20  |
| Qualidade de [Código com SonarQube](https://about.sonarcloud.io/) |  15  |
| Implementar testes unitários |  15  |
| Implementar testes comportamentais |  15  |
| Implementar integração com [Github Action](https://github.com/features/actions)  |  10  |
| Implementar integração com Github Action + SonarQube |  10  |
| Implementar usando Docker | 5 |
| Total| 170 |

Na sua nota final serâo acrescidos os pontos referentes aos itens implementados corretamente.

## Penalizações

Você será desclassifiado nas seguintes situações:

1. Se submeter um solução que não funcione; 
2. Se não cumprir os critérios presentes no seção **Avaliação**;
3. Se cometer plágio.

O que foi feito?
-o desafio foi concluído utilizando apenas python no arquivo encherBD.py
-para concluir o desafio utilizando FrontEnd API e BD é necessário terminar a conexão entre o front e a API
-O BD foi concluido.


