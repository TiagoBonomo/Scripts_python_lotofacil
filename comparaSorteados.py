# Autor: Tiago F Bonomo
import time
import timeit

# Lê arquivos .txt e armazena respectivamente.
arq_sorteados = open(r"C:\testearquivos\comparaSorteados.txt")
arq_002 = open(r"C:\testearquivos\posicaoPosicao071020202157.txt")

# Listas, são usadas para iteração organização.
sorteados = []
lista_arq_002 = []

s_f_s = ""

# Função comparaSorteados recebe retorno da função open() como parâmetro
def comparaSorteados(arq_p_sorteados, arq_p_002):

    # Parametros recebidos são o retorno da função open()
    it_sorteados = arq_p_sorteados
    it_arq_002 = arq_p_002

    cont01 = 0
    # Itera sobre o retorno do open() enviado via parametro a função comparar()
    for linha_sorteados in it_sorteados:
        s_f_s = linha_sorteados[18:63]
        sorteados.append(s_f_s.split(" "))
        troca_sorteados = sorteados[cont01]
        troca_dezena = int(troca_sorteados[14])
        troca_sorteados[14] = str(troca_dezena)
        sorteados[cont01] = troca_sorteados

        cont01 = cont01 + 1

    cont_arq = 0
    for linha_arq_002 in it_arq_002:
        lista_arq_002.append(linha_arq_002.split(" "))
        troca_arq = lista_arq_002[cont_arq]
        troca_dezena_arq = int(troca_arq[14])
        troca_arq[14] = str(troca_dezena_arq)
        lista_arq_002[cont_arq] = troca_arq


        cont_arq = cont_arq + 1

    cont_comb = 0
    cont_s = 0
    for it_sot in range(len(sorteados)):

        cont_a = 0
        for it_arq in range(len(lista_arq_002)):
            #inters = set(conjuntos[cont04]).intersection(combinacoes[cont03])
            intersecao = set(sorteados[cont_s]).intersection(lista_arq_002[cont_a])

            if((len(intersecao) != 15) & (len(lista_arq_002) == cont_a)):
                cont_comb = cont_comb + 1
                print(" Interseção: ", intersecao)
                print(" Quantidade: ", len(intersecao))
                print(" Combinação: ", lista_arq_002[cont_a])
                with open(r"C:\testearquivos\comparaSorteados081020200843.txt", "a") as val:
                    linha = " ".join(lista_arq_002[cont_a])
                    linha = linha + "\n"
                    val.write(linha)
            cont_a = cont_a + 1

        cont_s = cont_s + 1


# Chama a função e verifica tempo de execução da função através da função timeit()
inicio = timeit.default_timer()
comparaSorteados(arq_sorteados,arq_002)
fim = timeit.default_timer()

print("Tempo de execução da função timeit(): %f" % (fim - inicio))
