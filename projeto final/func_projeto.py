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