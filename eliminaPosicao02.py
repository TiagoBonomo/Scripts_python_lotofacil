# Autor: Tiago F Bonomo
import time
import timeit

# Lê arquivos .txt e armazena respectivamente em lista_lfacil.
lista_lfacil = open(r"C:\testearquivos\posicaoPosicao071020202157.txt")

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

        combinacoes.append(linha_comb.split(" "))
        #print(combinacoes[cont01])

        cont01 = cont01 + 1

    # Percorre a lista criada com o retorno da função open()

    cont03 = 0
    for i in range(len(combinacoes)):
        it_comb = combinacoes[cont03]
        #print("Combinação : ",it_comb)
        if (len(it_comb) == 15):
            global contador
            pos01 = int(it_comb[0])
            #print("Posição: ", pos01)
            pos02 = int(it_comb[1])
            #print("Posição: ", pos02)
            pos03 = int(it_comb[2])
            #print("Posição: ", pos03)
            pos04 = int(it_comb[3])
            #print("Posição: ", pos04)
            pos05 = int(it_comb[4])
            #print("Posição: ", pos05)
            pos06 = int(it_comb[5])
            #print("Posição: ", pos06)
            pos08 = int(it_comb[7])
            #print("Posição: ", pos08)
            pos10 = int(it_comb[9])
            #print("Posição: ", pos10)
            pos11 = int(it_comb[10])
            #print("Posição: ", pos11)
            pos12 = int(it_comb[11])
            # print("Posição: ", pos11)
            pos13 = int(it_comb[12])
            # print("Posição: ", pos11)
            pos14 = int(it_comb[13])
            #print("Posição: ", pos14)
            pos15 = int(it_comb[14])
            #print("Posição: ", pos15)
            if(pos10 != 13):
                if((pos11 != 15) or (pos11 != 20) or (pos11 != 21)):
                    if(pos13 != 18):
                        print("Combinação : ", it_comb)
                        with open(r"C:\testearquivos\eliminaPosicao081020200902.txt", "a") as val:
                            linha = " ".join(combinacoes[cont03])
                            # linha = linha
                            val.write(linha)





                '''
                with open(r"C:\testearquivos\posicao15k, .txt", "a") as val:
                    linha = " ".join(combinacoes[cont03])
                    #linha = linha
                    val.write(linha)
                '''
        cont03 = cont03 + 1



# Chama a função e verifica tempo de execução da função através da função timeit()
inicio = timeit.default_timer()
elimina01(lista_lfacil)
fim = timeit.default_timer()

print("Tempo de execução da função timeit(): %f" % (fim - inicio))
print(contador)
