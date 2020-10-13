# Autor: Tiago F Bonomo
import time
import timeit

# Lê arquivos .txt e armazena respectivamente em lista_lfacil e lista_conjuntos
lista_lfacil = open(r"C:\testearquivos\salvaPorPosicao190920200944.txt")
lista_conjuntos = open(r"C:\testearquivos\conjuntos.txt")

'''
# Conta as linhas dos arquivos dos arquivos contidos em ope()
conta_linhas_combinacoes = sum(1 for line01 in open(r"C:\testearquivos\validos - Copia130820201404"))
conta_linhas_conjuntos = sum(1 for line in open(r"C:\testearquivos\conjuntos.txt"))
'''

# Listas, são usadas para iteração organização e comparação dos conjutos e listas
combinacoes = []
conjuntos = []


# Função comparar recebe retorno da função open() como parâmetro
def comparar(p_conjuntos, p_combinacoes):
    # Parametros recebidos são o retorno da função open()
    comb = p_combinacoes
    conj = p_conjuntos
    cont01 = 0
    cont02 = 0

    # Itera sobre o retorno do open() enviado via parametro a função comparar()
    for linha_comb in comb:
        combinacoes.append(linha_comb.split(" "))
        trocaComb = combinacoes[cont01]
        trocaDez = int(trocaComb[14])
        trocaComb[14] = str(trocaDez)
        combinacoes[cont01] = trocaComb
        # Remove elemento "\n" da lista
        if(len(combinacoes[cont01]) > 15 ):
            combinacoes[cont01].pop()
        # print(combinacoes[cont01])
        cont01 = cont01 + 1

    # Itera sobre o retorno do open() enviado via parametro a função comparar()
    for linha_conj in conj:
        conjuntos.append(linha_conj.split(" "))
        # Remove elemento "\n" da lista
        conjuntos[cont02].pop()
        print(conjuntos[cont02])
        cont02 = cont02 + 1

    # Percorre a lista criada com o retorno da função open()
    cont03 = 0
    for i in range(len(combinacoes)):
        combinacoes[cont03]
        print("----------------------------------------------------------------------------------------------------")
        print(cont03, "ª - Iteração combinações   $$$$$$$$$$ ")
        print("Combinação: ", combinacoes[cont03], " -------------------------------------------------------")
        print("----------------------------------------------------------------------------------------------------")

        cont04 = 0
        n_inters = 0
        contador_valido01 = 0
        contador_valido02 = 0
        contador_valido03 = 0

        for j in range(len(conjuntos)):

            print(cont04, "ª - Iterações conjuntos ")
            inters = set(conjuntos[cont04]).intersection(combinacoes[cont03])
            qdesenas_conjuntos = len(conjuntos[cont04])

            '''
            print("Combinação: ", combinacoes[cont03], "Tipo: ", type(combinacoes[cont03]))
            print("Conjunto: ", conjuntos[cont04], "Tipo: ", type(conjuntos[cont04]))
            print("interseção: ", inters, " --- Tipo de dado da interseção: ", type(inters))
            '''
            if (len(inters) >= 1):
                n_inters = n_inters + 1
            # Verifica tamanho de conjuntos e quantidade de interceções
            if ((qdesenas_conjuntos >= 1) & (qdesenas_conjuntos <= 7) & (len(inters) >= 1)):
                contador_valido01 = contador_valido01 + 1
                print("Quantidade dezenas conjuntos: ", qdesenas_conjuntos)
                print("Interceções: ", inters)
                print("Conjunto: ", conjuntos[cont04])
                print("Combinação: ", combinacoes[cont03])
                print("Contador Valido 01", contador_valido01)
            # Verifica tamanho de conjuntos e quantidade de interceções
            elif ((qdesenas_conjuntos >= 8) & (len(inters) >= 2)):
                contador_valido02 = contador_valido02 + 1
                print("Quantidade dezenas conjuntos: ", qdesenas_conjuntos)
                print("Interceções: ", inters)
                print("Conjunto: ", conjuntos[cont04])
                print("Combinação: ", combinacoes[cont03])
                print("Contador Valido 02", contador_valido02)
            '''
            # Verifica tamanho de conjuntos e quantidade de interceções
            elif ((qdesenas_conjuntos >= 7) & (len(inters) >= 3)):
                contador_valido03 = contador_valido03 + 1
                print("Quantidade dezenas conjuntos: ", qdesenas_conjuntos)
                print("Interceções: ", inters)
                print("Conjunto: ", conjuntos[cont04])
                print("Combinação: ", combinacoes[cont03])
                print("Contador Valido 03", contador_valido03)
            '''

            # Compara se quantidade de conjuntos é igual a soma de contador_valido01, contador_valido02 e contador_valido03
            if (len(conjuntos) == (contador_valido01 + contador_valido02)):
                print(" ------- Combinação válida ", combinacoes[cont03],"--------------")
                with open(r"C:\testearquivos\validos190920201401.txt", "a") as val:
                    linha = " ".join(combinacoes[cont03])
                    linha = linha + "\n"
                    val.write(linha)

            '''
            if (n_inters == len(conjuntos)):
                with open(r"C:\testearquivos\validos.txt", "a") as val:
                    linha = " ".join(combinacoes[cont03])
                    linha = linha + "\n"
                    val.write(linha)
            '''

            '''    
            if (n_inters == len(conjuntos)):
                print(n_inters)
                print(" ################ ################ ################ ")
                print(" ################ A combinação passou!!! ################ ")
                print(" ################ ################ ################ ")
            if (n_inters < len(conjuntos)):
                print(" <<<<<<<<<<<<<<<<<<<< -------------------------- >>>>>>>>>>>>>>>>>>>> ")
                print(" <<<<<<<<<<<<<<<<<<<< A combinação não passou!!! >>>>>>>>>>>>>>>>>>>> ")
                print(" <<<<<<<<<<<<<<<<<<<< -------------------------- >>>>>>>>>>>>>>>>>>>> ")
            '''
            # print(len(conjuntos))
            # print(n_inters)
            cont04 = cont04 + 1
        print()
        cont03 = cont03 + 1


# Chama a função e verifica tempo de execução da função através da função timeit()
inicio = timeit.default_timer()
comparar(lista_conjuntos, lista_lfacil)
fim = timeit.default_timer()

print("Tempo de execução da função timeit(): %f" % (fim - inicio))
'''
print()
print("Tipo:", type(lista_lfacil))
print("Tipo:", type(lista_conjuntos))
print("Numero de elementos:", len(conjuntos))
print("Numero de elementos:", len(combinacoes))
print("Lista 1: ", combinacoes)
print("Lista 2: ", conjuntos)
'''
