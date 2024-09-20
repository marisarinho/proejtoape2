from datetime import datetime

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
print(quant_por_idade())