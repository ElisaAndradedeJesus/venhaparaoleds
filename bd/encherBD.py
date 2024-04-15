import psycopg2 as psy
import urllib.parse as up


def conectandoBD():
    con = psy.connect(
        database="cdtdwmpa",
        user="cdtdwmpa", 
        password="zBP4D7ZGZUxhJqKnWnmOmYwcXszjTWqp", 
        host="isabelle.db.elephantsql.com", 
        port="5432")
    return con

def lerCandidato(arquivo):
    linha = arquivo.readline()
    candidatos = []
    while linha != "":
        linha = linha[:-1]

        segmentosDeLinha = linha.split(" ")

        nome = str(segmentosDeLinha[0] +" "+ segmentosDeLinha[1])
        data_nascimento = segmentosDeLinha[2]
        cpf = segmentosDeLinha[3]

        profissao = ""
        for i in range(4,len(segmentosDeLinha)):
            profissao += segmentosDeLinha[i]

        profissao = profissao.replace("[","")
        profissao = profissao.replace("]","")

        json = {"nome":nome, "data_nascimento":data_nascimento,"cpf":cpf, "profissao":profissao}
        candidatos.append(json)
        del json

        linha = arquivo.readline()
    return candidatos

def lerConcurso(arquivo):
    linha = arquivo.readline()
    concursos = []
    while linha != "":
        linha = linha[:-1]

        segmentosDeLinha = linha.split(" ")

        orgao = segmentosDeLinha[0]
        edital = segmentosDeLinha[1]
        codigo_concurso = segmentosDeLinha[2]

        lista_vagas = ""
        for i in range(3,len(segmentosDeLinha)):
            lista_vagas += segmentosDeLinha[i]

        lista_vagas = lista_vagas.replace("[","")
        lista_vagas = lista_vagas.replace("]","")

        json = {"orgao":orgao, "edital":edital,"codigo_concurso":codigo_concurso, "lista_vagas":lista_vagas}
        concursos.append(json)
        del json

        linha = arquivo.readline()
    return concursos

def carregarCandidatosBD(candidatos):
    conexao = conectandoBD()
    cursor = conexao.cursor()
    for i in range(len(candidatos)):
        cursor.execute(f"insert into CANDIDATO (nome,data_nascimento,cpf,profissao) values ('{candidatos[i]['nome']}','{candidatos[i]['data_nascimento']}','{candidatos[i]['cpf']}','{candidatos[i]['profissao']}')")
        conexao.commit()
    conexao.close()

def carregarConcursosBD(concursos):
    conexao = conectandoBD()
    cursor = conexao.cursor()
    for i in range(len(concursos)):
        cursor.execute(f"insert into CONCURSO (orgao,edital,codigo_concurso,lista_vagas) values ('{concursos[i]['orgao']}','{concursos[i]['edital']}','{concursos[i]['codigo_concurso']}','{concursos[i]['lista_vagas']}')")
        conexao.commit()
    conexao.close()

#Chamamos as funçoes responssáveis por puxar os dados dos arquivos.txt e os colocamos no Banco de Dados

def possuiLetra(string):
    indesejados= 'qwertyuiopasdfghjklçzxcvbnm,<>;:~^}{`´][=+_)(*&¨%$#@!"/) '
    for letra in indesejados:
        for elemento in string:
            if elemento == letra:
                return True
    return False

def parametroDaPesquisa():
    tipo = ''
    cpfOuCod = input(str("Digite um cpf ou código:"))
    while len(tipo) == 0:
        if((len(cpfOuCod) == 0) or (len(cpfOuCod)<11) or (len(cpfOuCod)>14) or possuiLetra(cpfOuCod)):
            print("Favor inserir um cpf ou código de edital")
            cpfOuCod = input(str("Digite um cpf ou código:"))
        else:
            qtipo = input(str("Se voçe inserio um cpj digite c, caso contrário digite e."))
            while qtipo != "e" and qtipo !="c":
                print("favor inserir apenas e para código de edital ou c para cpf")
                qtipo = input(str("Se voçe inserio um cpj digite c, caso contrário digite e."))
            tipo = qtipo
    if tipo == "c":
        cpfOuCod = cpfOuCod.replace(".",'')
        cpfOuCod = cpfOuCod.replace('-','')
        cpf = str(cpfOuCod[0] + cpfOuCod[1]+cpfOuCod[2] +'.'+cpfOuCod[3]+cpfOuCod[4]+cpfOuCod[5]+'.'+cpfOuCod[6]+cpfOuCod[7]+cpfOuCod[8]+'-'+cpfOuCod[9]+cpfOuCod[10])
        return cpf,tipo

    if tipo == 'e':
        cpfOuCod = cpfOuCod.replace(".",'')
        codigo_concurso = cpfOuCod.replace('-','')      
        return codigo_concurso,tipo

def semRepetir(lista):
    list = []
    for elemento in lista:
        if elemento not in list:
            list.append(elemento)
    return list

def buscarConcursos(candidatos,concursos,cpf):

    profissao = ''
    editais = []

    # primeiro buscamos sacer as capacitações do candidato

    for candidato in candidatos:
        if candidato['cpf'] == cpf:
            profissao += candidato['profissao']

    # depois buscamos editais compatíveis

    profissoes = profissao.split(',')
    for edital in concursos:
        vagas = edital['lista_vagas'].split(',')
        for vaga in vagas:
            for prof in profissoes:
                if vaga == prof:
                    editais.append(edital)

    # print ordenado das informações
    editais = semRepetir(editais)
    for i in editais:

        print('\n\n'+i['orgao'])
        print(i['edital'])
        print(i['codigo_concurso'])
        


    
def buscarCandidatos(candidatos,concursos,cod):
    vaga = ''
    candidatosAoEdital = []

    #primeiro descobrimos quais os requisitos para este concurso

    for concurso in concursos:
        if concurso['codigo_concurso'] == cod:
            vaga += concurso['lista_vagas']
    
    # depois buscamos candidatos qualificados
    
    vagas = vaga.split(',')
    for candidato in candidatos:
        profissoes = candidato['profissao'].split(',')
        for profissao in profissoes:
            for vag in vagas:
                if profissao == vag:
                    candidatosAoEdital.append(candidato)

    #print ordenado das informações
    candidatosAoEdital = semRepetir(candidatosAoEdital)
    for i in candidatosAoEdital:

        print('\n\n'+i['nome'])
        print(i['data_nascimento'])
        print(i['cpf'])
        
  
    

def main():
    listaCandidatos = open("candidatos.txt","r")
    candidatos = lerCandidato(listaCandidatos)
    listaCandidatos.close()


    listaConcursos = open("concursos.txt","r")
    concursos = lerConcurso(listaConcursos)
    listaConcursos.close()

    # para que não hajam dados em duplicidade no banco de dados a chamada das funções que o alimentam foram comentadas

    # carregarCandidatosBD(candidatos)
    # carregarConcursosBD(concursos)

    #tentativa de resolver o problema em python puro, não ficou bom, mas funciona

    # cpfOuCod,tipo = parametroDaPesquisa()
    # if tipo == 'c':
    #     buscarConcursos(candidatos,concursos,cpfOuCod)
    # if tipo == 'e':
    #     buscarCandidatos(candidatos,concursos,cpfOuCod)
    

    
    return 0 
if __name__=="__main__":
    main()