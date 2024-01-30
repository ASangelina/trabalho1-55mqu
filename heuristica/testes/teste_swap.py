import random 

def perturb(solution, percent):
    ##print(int(len(solution) * (percent/100) + 1))
    n = len(solution)
    num_swaps = int(n * percent / 100)
    ##print(num_swaps)
    print(random.choice(solution))
    for _ in range(num_swaps):
        # Escolha aleatoriamente um elemento da solução
        i = random.randint(0, n-1)
        print(i)
        # Escolha aleatoriamente um elemento não pertencente à solução
        j = random.randint(0, n-1)
        print(j)
        while j in solution:
            j = random.randint(0, n-1)
        # Troque os elementos
        solution[i], solution[j] = solution[j], solution[i]
    return solution

solution_teste = [1, 0, 0, 0, 1, 1, 0, 0, 0, 0]
percent_teste = [10,20]
for percent in percent_teste:
    solutionPerturb = perturb(solution_teste, percent)
    print(f'Solução após perturbação de {percent_teste}%: {solutionPerturb}')


for i in range(10):
   escolha, indice = random.choice(list(enumerate(solution_teste)))
   print("Teste", escolha, "Índice", indice)
