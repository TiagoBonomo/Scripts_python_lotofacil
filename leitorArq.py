#Autor: Tiago F Bonomo

import time
import timeit
#Lê arquivo .txt e armazena em lista_lfacil
lfacil = open(r"C:\testearquivos\lotofacilteste.txt")

dezenas = []

#Processa variavel lista_lfacil
def leitura(a):

    cont = 0
    conteudo = a

    conj01 = {"02","17","21","22","23"}

    for line in conteudo:

        dezenas.append(line.split(" "))

        inter = conj01.intersection(dezenas[cont])
        #print(dezenas)
        print()
        print(conj01)
        print(dezenas[cont])
        print(len(inter))


        cont = cont + 1

inicio = timeit.default_timer()
leitura(lfacil)
fim = timeit.default_timer()

print("Inicio: %f" % (inicio))
print("Fim: %f" % (fim))
print()
print('duracao: %f' % (fim - inicio))
