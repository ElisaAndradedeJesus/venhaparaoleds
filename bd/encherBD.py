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

def main():
    listaCandidatos = open("candidatos.txt","r")
    candidatos = lerCandidato(listaCandidatos)
    listaCandidatos.close()


    listaConcursos = open("concursos.txt","r")
    concursos = lerConcurso(listaConcursos)
    listaConcursos.close()


    # carregarCandidatosBD(candidatos)
    carregarConcursosBD(concursos)

    
    return 0 
if __name__=="__main__":
    main()