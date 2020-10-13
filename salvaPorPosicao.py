# Autor: Tiago F Bonomo
import time
import timeit

# Lê arquivos .txt e armazena respectivamente em lista_lfacil.
lista_lfacil = open(r"C:\testearquivos\lotofacil.txt")

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
        if(len(combinacoes[cont01])>15):
            combinacoes[cont01].pop()


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
            pos07 = int(it_comb[6])
            #print("Posição: ", pos07)
            pos08 = int(it_comb[7])
            #print("Posição: ", pos08)
            pos09 = int(it_comb[8])
            #print("Posição: ", pos09)
            pos10 = int(it_comb[9])
            #print("Posição: ", pos10)
            pos11 = int(it_comb[10])
            #print("Posição: ", pos11)
            pos12 = int(it_comb[11])
            #print("Posição: ", pos12)
            pos13 = int(it_comb[12])
            #print("Posição: ", pos13)
            pos14 = int(it_comb[13])
            #print("Posição: ", pos14)
            pos15 = int(it_comb[14])
            #print("Posição: ", pos15)

            if((pos01 == 1) or (pos01 == 2) or (pos01 == 3) or (pos01 == 4)):
                if((pos02 == 2) or (pos02 == 3) or (pos02 == 4) or (pos02 == 5)):
                    if((pos03 == 3) or (pos03 == 4) or (pos03 == 5) or (pos03 == 6)):
                        if((pos04 == 4) or (pos04 == 5) or (pos04 == 6) or (pos04 == 7)):
                            if ((pos05 == 5) or (pos05 == 6) or (pos05 == 7) or (pos05 == 8)):
                                if ((pos06 == 9) or (pos06 == 10)):
                                    if ((pos07 == 10) or (pos07 == 11) or (pos07 == 12)):
                                        if ((pos08 == 12) or (pos08 == 13)):
                                            if ((pos09 == 12) or (pos09 == 13) or (pos09 == 14)):
                                                if ((pos10 == 13) or (pos10 == 14) or (pos10 == 15) or (pos10 == 16)
                                                        or (pos10 == 17)):
                                                    if ((pos11 == 14) or (pos11 == 15) or (pos11 == 17) or
                                                            (pos11 == 18) or (pos11 == 19) or (pos11 == 20) or
                                                            (pos11 == 21)):
                                                        if ((pos12 == 15) or (pos12 == 16) or (pos12 == 17) or (
                                                                pos12 == 18) or (pos12 == 20) or (pos12 == 21)):
                                                            if ((pos13 == 16) or (pos13 == 18) or (pos13 == 19) or (
                                                                    pos13 == 20) or (pos13 == 21) or (pos13 == 22) or
                                                                    (pos13 == 23)):
                                                                if ((pos14 == 17) or (pos14 == 18) or (pos14 == 19) or (
                                                                        pos14 == 20) or (pos14 == 21) or (pos14 == 22)
                                                                        or (pos14 == 23) or (pos14 == 24)):
                                                                    if ((pos15 == 18) or (pos15 == 25)):



                                                                        print("Combinação : ",it_comb)

                                                                        with open(r"C:\testearquivos\salvaPorPosicao051020201646.txt",
                                                                                  "a") as val:
                                                                            linha = " ".join(combinacoes[cont03])
                                                                            linha = linha + "\n"
                                                                            val.write(linha)


        cont03 = cont03 + 1



# Chama a função e verifica tempo de execução da função através da função timeit()
inicio = timeit.default_timer()
elimina01(lista_lfacil)
fim = timeit.default_timer()

print("Tempo de execução da função timeit(): %f" % (fim - inicio))
print(contador)
