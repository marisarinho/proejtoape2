from funcs_projeto import *

x = input("Digite o nome da cidade: ").upper()
localizar_cod(x)

# #Lista com o nome das cidades do arquivo fonte:
# arquivo = open("Nome_cidades.txt","r")
# NM_UE = arquivo.readlines()
# arquivo.close()

# #Lista com o codigo das cidades do arquivo fonte:
# arquivo = open("Codigo_UE.txt","r")
# SE_UE = arquivo.readlines()
# arquivo.close()

# print(NM_UE)
# nome_cid = remover_repet(montar_lista(NM_UE))
# cod_cid = remover_repet(montar_lista(SE_UE))

# if x in nome_cid:
#     i = nome_cid.index(x)
#     print(f"Codigo da cidade {x} é: {cod_cid[i]}")
# else:
#     print("cidade não encontrada!")