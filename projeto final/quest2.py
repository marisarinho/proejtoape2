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