# Autor: Tiago F Bonomo
import time
import timeit

# Lê arquivos .txt e armazena respectivamente em lista_lfacil e lista_conjuntos
lista_lfacil = open(r"C:\testearquivos\EliminaTrios081020201254.txt")

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
        #print("Combinação: ", c)

        verificador = 0
        for dez in range(len(c)):
            cToStr = c[dez]
            if(int(cToStr) == 6):
                verificador = verificador + 1
            if(int(cToStr) == 8):
                verificador = verificador + 1


        if (verificador != 2):
            print("verificador:", verificador)
            print("Combinação: ", c)
            with open(r"C:\testearquivos\EliminaTrios081020201255.txt", "a") \
                    as val:
                linha = " ".join(combinacoes[cont03])
                # linha = linha
                val.write(linha)



# Chama a função e verifica tempo de execução da função através da função timeit()
inicio = timeit.default_timer()
comparar(lista_lfacil)
fim = timeit.default_timer()

print("Tempo de execução da função timeit(): %f" % (fim - inicio))
