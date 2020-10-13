# Autor: Tiago F Bonomo
import time
import timeit

# Lê arquivos .txt e armazena respectivamente em lista_lfacil e lista_conjuntos
lista_lfacil = open(r"C:\testearquivos\s30-210920201020.txt")

# Listas, são usadas para iteração organização e comparação dos conjutos e listas
combinacoes = []


# Função comparar recebe retorno da função open() como parâmetro
def comparar(p_combinacoes):
    # Parametros recebidos são o retorno da função open()
    comb = p_combinacoes

    cont01 = 0
    cont02 = 0

    # Itera sobre o retorno do open() enviado via parametro a função comparar()
    for linha_comb in comb:
        if (linha_comb != "\n"):
            combinacoes.append(linha_comb.split(" "))
            # Remove elemento "\n" da lista
            combinacao = combinacoes[cont01]
        cont01 = cont01 + 1

    # Percorre a lista criada com o retorno da função open()
    cont03 = 0
    for i in range(len(combinacoes)):

        c = combinacoes[cont03]
        cont03 = cont03 + 1

        somaTotal = 0
        somaUnidade = 0
        somaDezena = 0
        somaTodos = 0

        for dez in range(len(c)):
            cToStr = c[dez]

            somaTotal = somaTotal + int(c[dez])
            somaUnidade = somaUnidade + int(cToStr[1])
            somaDezena = somaDezena + int(cToStr[0])
            somaTodos = somaTodos + (int(cToStr[0]) + int(cToStr[1]))

        if ((somaDezena < 17)):
            with open(r"C:\testearquivos\testepython3.8.txt", "a") as val:
                print(cont03)
                linha = " ".join(combinacoes[cont03])
                # linha = linha
                val.write(linha)

            print("Combinação: ", c, "-----------------------")
            print("Soma Total ", somaTotal)
            print("Soma unidades ", somaUnidade)
            print("Soma dezenas ", somaDezena)
            print("Soma todos ", somaTodos)

        '''
        if((somaTotal > 1) & (somaUnidade > 1) & (somaDezena > 1) & (somaTodos > 1)):
            print(" IF de comparação de somas ")
            print("Combinação: ",c, "-----------------------")
            print("Soma Total ", somaTotal)
            print("Soma unidades ", somaUnidade)
            print("Soma dezenas ", somaDezena)
            print("Soma todos ", somaTodos)
            print(" IF de comparação de somas ")
            with open(r"C:\testearquivos\somas.txt", "a") as val:
                linha = " ".join(c)
                linha = linha + "\n"
                val.write(linha)
        '''

        '''
                print("contador 03 :", cont03)
                print("Tipo: ",type(c),"----------------------------------------------------------------------------")
                print("---------------------------------------------------------------------------------------------")
                print(cont03, "ª - Iteração combinações   $$$$$$$$$$ ")
                print("Combinação: ", combinacoes[cont03], " -------------------------------------------------------")
                print("---------------------------------------------------------------------------------------------")

        '''


# Chama a função e verifica tempo de execução da função através da função timeit()
inicio = timeit.default_timer()
comparar(lista_lfacil)
fim = timeit.default_timer()

print("Tempo de execução da função timeit(): %f" % (fim - inicio))
