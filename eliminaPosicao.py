# Autor: Tiago F Bonomo
import time
import timeit

# Lê arquivos .txt e armazena respectivamente em lista_lfacil.
lista_lfacil = open(r"C:\testearquivos\validos.txt")

# Listas, são usadas para iteração organização.
combinacoes = []
contador = 0


# Função comparar recebe retorno da função open() como parâmetro
def elimina01(p_combinacoes):
    # Parametros recebidos são o retorno da função open()
    comb = p_combinacoes

    cont01 = 0
    cont02 = 0
    # Itera sobre o retorno do open() enviado via parametro a função comparar()
    for linha_comb in comb:
        if(linha_comb != "\n"):
            combinacoes.append(linha_comb.split(" "))
            #print(" Linha 1: ", linha_comb)
            #print("tipo: ", type(comb))
            # Remove elemento "\n" da lista
            #combinacoes[cont01].pop()
            # print(combinacoes[cont01])

        cont01 = cont01 + 1

    # Percorre a lista criada com o retorno da função open()

    cont03 = 0
    for i in range(len(combinacoes)):
        it_comb = combinacoes[cont03]
        #dez_comb_int = it_comb[14]
        if (len(it_comb) == 15):
            global contador
            pos03 = int(it_comb[2])
            pos04 = int(it_comb[3])
            pos05 = int(it_comb[4])
            pos06 = int(it_comb[5])
            pos07 = int(it_comb[6])
            pos08 = int(it_comb[7])
            pos09 = int(it_comb[8])
            pos11 = int(it_comb[10])
            pos14 = int(it_comb[13])
            pos15 = int(it_comb[14])

            if( (pos03 != 5) & (pos03 != 8) & (pos03 < 10) ):#& (pos03 != 11) & (pos03 != 12) & (pos03 != 13)
                if((pos04 != 7) & (pos04 != 10 )):
                    if((pos05 != 11) & (pos05 < 13)):
                        if((pos06 != 7) & (pos06 < 14)):
                            if(pos07 != 14):
                                if((pos08 > 8) & (pos08 != 11) & (pos08 != 15)):
                                    if(pos09 != 16):
                                        if((pos11 != 15) & (pos11 != 16) & (pos11 != 20)):
                                            if((pos14 != 21) & (pos14 != 24)):
                                                if((pos14 > 17)):

                                                    with open(r"C:\testearquivos\eliminaPosicao.txt", "a") as val:
                                                        linha = " ".join(combinacoes[cont03])
                                                        #linha = linha
                                                        val.write(linha)

                                                    print(combinacoes[cont03])
                                                    print(pos03)
                                                    contador = contador + 1



        '''
        print(" combinação: ", combinacoes[cont03])
        print("Tipo: ", type(it_comb))
        '''

        '''
        print("----------------------------------------------------------------------------------------------------")
        print(cont03, "ª - Iteração combinações   $$$$$$$$$$ ")
        print(" combinação: ", combinacoes[cont03])
        print(len(combinacoes[cont03]), " elementos na lista ")
        print("----------------------------------------------------------------------------------------------------")
        '''
        cont03 = cont03 + 1


# Chama a função e verifica tempo de execução da função através da função timeit()
inicio = timeit.default_timer()
elimina01(lista_lfacil)
fim = timeit.default_timer()

print("Tempo de execução da função timeit(): %f" % (fim - inicio))
print(contador)
