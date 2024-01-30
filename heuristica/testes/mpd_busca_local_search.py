## INSTANCIAS
## TODO: reusar as intancias do problema.

### REPRESENTACAO SOLUCAO
## TODO: construir um array unidimensional booleano que representa
## a solução, para isso vai ter m 1, e o tamanho do array é n.

### CONSTRUCAO ALEATORIA E GULOSA
## Vai escolher o melhor, mas de forma aleátoria.

### ITERACAO PARA SOLUÇÃO MELHOR
## TODO:definir critério de parada.
## pode ser tempo, ou outra coisa.


#Número de iterações
max_iterations = 1000
#Taxa de perturbação
perturbation = 20


# SOLUCAO GULOSA

## recebe a matriz de distância.
## talvez selecionar os itens com maior distância, talvez selecionar o item que mais relaciona.
## preciso fazer isso para selecionar o m itens.

def greedy_solution(distances):
    

    ## construir e retornar ela.
    solution = 100
    return solution


## preciso pertubar a solução, ou seja preciso modificar ela, selecionando outros itens para a solução, verificar se essa solução é melhor que a solução inicial.

## provalvemente vou chamar a solução inicial aqui.
## como seria a estrátegia para alterar os items
def iterated_local_search(initialSolution, max_iterations, perturbation):
    return 1









## chama a construção da solução gulosa aleatoria
# passar a matriz de distâncias, ou um map. distances 
initialSolution = greedy_solution()



## chama e apresenta a solução
solution = iterated_local_search(initialSolution, max_iterations, perturbation)
