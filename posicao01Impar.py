# Autor: Tiago F Bonomo
import time
import timeit

# Lê arquivos .txt e armazena respectivamente em lista_lfacil.
lista_lfacil = open(r"C:\testearquivos\somaTotal131020201745.txt")

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
        cont_impar = 0
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
            # print("Posição: ", pos07)
            pos08 = int(it_comb[7])
            #print("Posição: ", pos08)
            pos09 = int(it_comb[8])
            # print("Posição: ", pos09)
            pos10 = int(it_comb[9])
            #print("Posição: ", pos10)
            pos11 = int(it_comb[10])
            #print("Posição: ", pos11)
            pos12 = int(it_comb[11])
            # print("Posição: ", pos12)
            pos13 = int(it_comb[12])
            # print("Posição: ", pos13)
            pos14 = int(it_comb[13])
            #print("Posição: ", pos14)
            pos15 = int(it_comb[14])
            #print("Posição: ", pos15)
            if((pos01 % 2) != 0):
                cont_impar = cont_impar + 1
            if ((pos02 % 2) != 0):
                cont_impar = cont_impar + 1
            if ((pos03 % 2) != 0):
                cont_impar = cont_impar + 1
            if ((pos04 % 2) != 0):
                cont_impar = cont_impar + 1
            if ((pos05 % 2) != 0):
                cont_impar = cont_impar + 1
            if ((pos06 % 2) != 0):
                cont_impar = cont_impar + 1
            if ((pos07 % 2) != 0):
                cont_impar = cont_impar + 1
            if ((pos08 % 2) != 0):
                cont_impar = cont_impar + 1
            if ((pos09 % 2) != 0):
                cont_impar = cont_impar + 1
            if ((pos10 % 2) != 0):
                cont_impar = cont_impar + 1

            if(cont_impar == 5):
                print("Contador Impar: ", cont_impar)
                print("Combinação: ", combinacoes[cont03])

                '''
                with open(r"C:\testearquivos\dezenasprovaveis03.txt","a") as val:
                    linha = " ".join(combinacoes[cont03])
                    # linha = linha
                    val.write(linha)

                    print("Combinação : ", it_comb)
                '''












                '''
                with open(r"C:\testearquivos\dezenasprovaveis.txt", "a") as val:
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
