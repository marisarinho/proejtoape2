from funcs_projeto import *

print("Escolha uma das opções a seguir: ")
print("1- para usar codigo do municipio e cargo")
print("2- para usar o codigo do candidato")
print("3- Gerar pagina na web com estatisticas")
print("4- SAIR")

while True:
    n = int(input("Escolha uma das opções: "))
    if n == 1:
        #PEGANDO A LISTA DE CODIGOS DOS MUNICIPIOS DO ARQUIVO FONTE
        arquivo01 = open("Codigo_UE.txt","r")
        SE_UE = arquivo01.read().splitlines()
        arquivo01.close()

        #PEGANDO A LISTA DE CODIGOS DOS CARGOS DO ARQUIVO FONTE
        arquivo02 = open("Codigo_Cargos.txt","r")
        CD_CARGOS = arquivo02.read().splitlines()
        arquivo02.close()

        #MONTANDO LISTAS
        Lista_cod_municipio = montar_lista(SE_UE)
        Lista_cod_cargos = montar_lista(CD_CARGOS)

        #Lendo codigo do MUNICIPIO:
        while True:
            x = input("Digite o codigo do Municipio: ")
            if x not in set(Lista_cod_municipio):
                print("Codigo do MUNICIPIO informado invalido, favor informar outro.")
            else:
                break

        #Lendo codigo do CARGO:
        while True:
            y = input("Digite o codigo do Cargo: ")
            if y not in set(Lista_cod_cargos):
                print("Codigo do CARGO informado invalido, favor informar outro.")
            else:
                break

        lista01(x,y)
    elif n == 2:
        print("ainda não disponivel")
    elif n == 3:
        print("ainda não disponivel")
    elif n == 4:
        break
    else:
        print("Valor invalido, informe outro!")
