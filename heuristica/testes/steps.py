# imports
import os
import random
import csv
import time

# Leitura das instâncias do diretório das instâncias
def listar_arquivos_caminho(caminho):
    arquivos = os.listdir(caminho)
    return arquivos
pasta_inst = 'instancias/'
nomes_arquivos = listar_arquivos_caminho(pasta_inst)

def imprimir_nomes_arquivos(nomes_arquivos):
    for i, nome_arquivo in enumerate(nomes_arquivos, 1):
        print(f"{i} - {nome_arquivo}")


# Ler os dados da instância
def popula_matriz(file_path):
    matriz_distancia = []
    with open(file_path, 'r') as file:
        for line in file:
            valores_l = line.split(' ')
            if len(valores_l) > 2:
                i = int(valores_l[0])
                j = int(valores_l[1])
                valor = float(valores_l[2])
                matriz_distancia[i][j] = valor
            else:
                n = int(valores_l[0])
                m = int(valores_l[1])
                matriz_distancia = [[0 for j in range(n)] for i in range(n)]
    return matriz_distancia,m,n


########## STEP 1 ################
## TODO: IMPORTANTE, AJUSTAR
def max_diversity_selection(distances, m):
  n = len(distances)
  selected = []
  for i in range(n):
    diversities = [(distances[i][j], j) for j in range(n) if j not in selected]
    print("teste")
    print(diversities)
    diversities.sort(reverse=True)
    sorted_indices = [j for _, j in diversities[:m]]
    if len(selected) < m:
        selected.extend(sorted_indices)
    else:
        break
    # solution tamanho n
    solution_view = [True if i in selected else False for i in range(n)]
    return solution_view
  
########## STEP 2 ################
## TODO: IMPORTATE, AJUSTAR
def perturb(solution, percent):
    n = len(solution)
    num_swaps = int(n * percent / 100)
    for _ in range(num_swaps):
        # Escolha aleatoriamente um elemento da solução
        i = random.randint(0, n-1)
        # Escolha aleatoriamente um elemento não pertencente à solução
        j = random.randint(0, n-1)
        while j in solution:
            j = random.randint(0, n-1)
        # Troque os elementos
        solution[i], solution[j] = solution[j], solution[i]
    return solution


# Escolha da instância
imprimir_nomes_arquivos(nomes_arquivos)
numero = int(input("Digite o número correspondente ao arquivo que deseja usar no modelo: "))
if 1 <= numero <= len(nomes_arquivos):
    instancia = pasta_inst + str(nomes_arquivos[numero - 1])
else:
    print("Número inválido. Por favor, escolha um número válido.")

matriz_d,m,n = popula_matriz(instancia)

# passa a instancia...
solution = max_diversity_selection(matriz_d, m)
for i in solution:
    print("solucao inicial gulosa",i)


########## STEP 2 ################
# PERCENTUAIS DE PERTUBAÇÃO
# talvez esse percentual de pertubação seja melhor escolhido com base no tamanho da instância. 10 ou 20 !!!!!!
percentages = [2, 10, 40, 50, 70, 80]
for percent in percentages:
   print("antes",solution)
   solutionPerturb = perturb(solution, percent)
   print(f'Solução após perturbação de {percent}%: {solutionPerturb}')



########## STEP 3 ################
# Busca Local. Tem três, qual escolher?

##->melhor vizinho
##->primeiro de melhora
##->busca randômica.

########## STEP 4 ################
# critério de aceitação

## É aceito se a solução 
