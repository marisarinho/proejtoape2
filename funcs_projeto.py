from datetime import datetime

def lista01 (cod_municipio, cod_cargo):
        #buscando o arquivo na pasta e transformando ele em uma lista:
    arquivo = open("consulta_cand_2024_PB.csv","r")

    cargos = arquivo.readlines()

    arquivo.close()

    #transformando cada linha da lista (cargos) em outra lista:
    for i in cargos[1:]:
        x = i.replace("\n", "").replace('"', '').split(";")
        if x[11] == (f'{cod_municipio}') and x[13] == (f'{cod_cargo}'):
            print()
            print(f"Nome: {x[17]}")
            print(f"Nome_urna: {x[18]}")
            print(f"Número: {x[16]}")
            print(f"Partido: {x[27]}")
            print("--------------------------------------------------------")

#removendo valores repetidos:

def remover_repet(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    return l          

def montar_lista(lista):
    lista_n=[]
    for i in lista:
        lista_n.append(i.replace("\n",""))
    return lista_n


def localizar_cod (nome):
    #Lista com o nome das cidades do arquivo fonte:
    #Ta dando um problema na criação da lista Nome_Cidades
    arquivo = open("Nome_cidades.txt", "r",encoding='UTF-8')
    NM_UE = arquivo.readlines()
    arquivo.close()

    #Lista com o codigo das cidades do arquivo fonte:
    arquivo = open("Codigo_UE.txt", "r")
    SE_UE = arquivo.readlines()
    arquivo.close()

    nome_cid = remover_repet(montar_lista(NM_UE))
    cod_cid = remover_repet(montar_lista(SE_UE))

    if nome in nome_cid:
        i = nome_cid.index(nome)
        return print(f"Codigo da cidade {nome} é: {cod_cid[i]}")
    else:
        return print("cidade não encontrada!")
    


#MAAAAAAAAAAAAAAAAAARI
#criando uma funçao para ser importada pro html
def partidos_cargo_prefeito():
     #with abre e fecha sozinho 
     #primeiro r=raw(pra nao dar erro de leitura)
    with open(r'consulta_cand_2024_PB.csv', 'r', encoding='latin1') as arquivo:
        linhas = arquivo.read().splitlines()

    cargo=linhas[0].split(';').index('DS_CARGO')#acessando a linha pra achar a coluna que o cargo ta
    partido=linhas[0].split(';').index('SG_PARTIDO')
    #se o cargo for de prefeito, coloca o referente partido na lista
    partidos_prefeitos=set()#pra nao ter coisa repetida
    for i in range(1,len(linhas)):
        linha=linhas[i].split(';')#criando uma lista de todos os elementos separado por ';'
        if linha[cargo]=='PREFEITO':
            partidos_prefeitos.add(linha[partido])
    return list(partidos_prefeitos)
#list pra transformar o set numa lista



def quant_por_idade():
    def calcular_idade(data):
        dia,mes,ano=map(int,data.split('/'))
        data_nascimento = datetime(ano, mes, dia)
        data_atual = datetime.now()
        idade = data_atual.year - data_nascimento.year
        #  caso o aniversário ainda não tenha ocorrido neste ano
        if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
            idade -= 1
        return idade
    

    with open(r'consulta_cand_2024_PB.csv', 'r', encoding='latin1') as arquivo:
        linhas = arquivo.read().splitlines()

    nascimento=linhas[0].split(';').index('DT_NASCIMENTO')
    quantidade_idades={'ate_21':0,    #:0 fazendo um contador
                       '22_e_40':0,
                       '41_e_60':0,
                       'maior_60':0}   #fazendo um dicionario pra nao precisar fazer muitas listas
    for i in range(1,len(linhas)):
        linha=linhas[i].split(';')
        data_nascimento=linha[nascimento]
        idade=calcular_idade(data_nascimento)
        if idade<=21:
            quantidade_idades['ate_21']+=1
        elif idade >=22 and idade<=40:
            quantidade_idades['22_e_40']+=1
        elif idade >=41 and idade<=60:
            quantidade_idades['41_e_60']+=1
        else:
            quantidade_idades['maior_60']+=1
    return quantidade_idades
