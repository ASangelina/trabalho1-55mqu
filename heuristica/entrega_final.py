import random
import itertools
import os
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




########## 1 ##############
## SOLUÇÃO ALEÁTORIA
## TER UMA FUNÇÃO QUE SELECIONA M ITENS PARA A SOLUÇÃO ALEÁTORIA


def solution_random(n, m):
  # Crie uma lista de zeros de tamanho n
  solution = [0]*n
  
  # Gere m índices aleatórios sem repetição
  indices = random.sample(range(n), m)
  
  # Defina os valores em indices aleatórios como 1
  for index in indices:
      solution[index] = 1
  
  return solution


# Escolha da instância
imprimir_nomes_arquivos(nomes_arquivos)
numero = int(input("Digite o número correspondente ao arquivo que deseja usar no modelo: "))
if 1 <= numero <= len(nomes_arquivos):
    instancia = pasta_inst + str(nomes_arquivos[numero - 1])
else:
    print("Número inválido. Por favor, escolha um número válido.")

## preenche a matriz de distância
matriz_d,m,n = popula_matriz(instancia)



## retorna o valor da função objetivo
## vou pegar o valor da minha matriz_d sem passar por argumento
def sum_z(solution):
   indices = [i for i, x in enumerate(solution) if x == 1]
   
   # Gere todas as combinações possíveis de índices
   combinations = list(itertools.combinations(indices, 2))
   #print(combinations)

   total = 0
   for i, j in combinations:
    total += matriz_d[i][j]
    ##print(matrix[i][j])

   
   return total



def gerar_vizinhos(lista):
  # Encontre os índices dos elementos 1 na lista
  indices_1 = [i for i, x in enumerate(lista) if x == 1]
  
  # Para cada índice de um elemento 1, encontre todos os índices dos elementos 0 à esquerda e à direita
  for i in indices_1:
      indices_0 = [j for j in range(len(lista)) if lista[j] == 0 and j != i]
      
      # Para cada índice de um elemento 0, gere uma nova lista trocando o elemento 1 pelo elemento 0
      for j in indices_0:
          nova_lista = lista[:]
          nova_lista[i], nova_lista[j] = nova_lista[j], nova_lista[i]
          yield nova_lista


def busca_local(solucao_inicial):

    melhor_solucao = solucao_inicial
    melhor_valor = sum_z(melhor_solucao)
    #print("valor iniciail",melhor_valor)
    
    for vizinho in gerar_vizinhos(melhor_solucao):
        valor_vizinho = sum_z(vizinho)
        #print("melhor solucao",melhor_solucao)
        #print("valor vizinho teste",vizinho)

        if(valor_vizinho > melhor_valor):
           melhor_solucao, melhor_valor = busca_local(vizinho)
           #print("caiu aqui",melhor_solucao, melhor_valor)
    return melhor_solucao, melhor_valor
    



## solution aleátoria
#solution_initial = solution_random(n,m)
#print("solucao inicial",solution_initial)
#print("funcão objetivo",sum_z(solution_initial,matriz_d))

def perturb(solucao_atual, perc):
 # Cria uma cópia da solução atual
 nova_solucao = solucao_atual.copy()
 
 # Calcula o número de elementos a serem trocados
 num_trocas = int(len(nova_solucao) * perc)
 
 # Realiza as trocas
 for _ in range(num_trocas):
     # Escolhe dois elementos aleatórios da solução
     select_one = random.randint(0, len(nova_solucao) - 1)
     select_zero = random.randint(0, len(nova_solucao) - 1)
     
     # Troca os elementos
     nova_solucao[select_one], nova_solucao[select_zero] = nova_solucao[select_zero], nova_solucao[select_one]
 
 # Retorna a nova solução
 return nova_solucao

def accept_solution(solution_c,solution_p):
    z_corrent = sum_z(solution_c)
    z_pertub = sum_z(solution_p)
    if(z_pertub > z_corrent):
        return solution_p
    else:
        return solution_c

 


def iterated_local_search(solution_initial,stop,perc):
    ##s_inicial = solution_initial
    solution,sum_corrente = busca_local(solution_initial)
    solution_corrente = solution 
    for i in range(stop):
        solution_pertubada = perturb(solution_corrente,perc)
        solution_pertubada_local,pertubada = busca_local(solution_pertubada)
        solution_corrente = accept_solution(solution_corrente,solution_pertubada_local)

    return solution_corrente    



#Número de iterações
max_iterations = 100
#Taxa de perturbação
perturbation = 10
# Solucao Inicial
solution_initial_f = solution_random(n,m)
start_time = time.time()
solution_iterada = iterated_local_search(solution_initial_f,max_iterations,perturbation)
end_time = time.time()
execution_time = end_time - start_time
funcao_objetivo = sum_z(solution_iterada)
elemetos_solution = [i for i, x in enumerate(solution_iterada) if x == 1]
print("elementos",elemetos_solution,"solucao objetivo",funcao_objetivo,"tempo de execucao",execution_time)

