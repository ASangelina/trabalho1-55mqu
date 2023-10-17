import os
import csv
from pyomo.environ import *

# escolher o arquivo a ser executado
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
    valores = []
    with open(file_path, 'r') as file:
        for line in file:
            valores_l = line.split(' ')
            if len(valores_l) > 2:
                valor = float(valores_l[2])
                valores.append(valor)
            else:
                n = int(valores_l[0])
                m = int(valores_l[1])
    contador = 0
    matriz_distancia = [[0 for j in range(n)] for i in range(n)]
    for j in range(n-1):
        for i in range(n):
            if(i > j):
                matriz_distancia[i][j] = valores[contador]
                contador += 1
            else:
                matriz_distancia[i][j] = 0
    return matriz_distancia,m,n

imprimir_nomes_arquivos(nomes_arquivos)

numero = int(input("Digite o número correspondente ao arquivo que deseja usar no modelo: "))
if 1 <= numero <= len(nomes_arquivos):
    instancia = pasta_inst + str(nomes_arquivos[numero - 1])
    #print(f"Você selecionou o arquivo: {arquivo_selecionado}")
else:
    print("Número inválido. Por favor, escolha um número válido.")

matriz_d,m,n = popula_matriz(instancia)
#print(matriz_d,subconjunto_m)

##
## selecionar m itens que sejam a maior distância
# decisão yij que se tornam iguais a 1 se i e j fizerem parte da solução e 0, caso contrario
## criar as váriáveis de decisão do pyomo

# a tupla Q
# Criação da tupla de pares
## orientação professor: fazer um conjunto de pares,uma tupla com dois elementos, um for de i de 0 até n-2, e for no j de i+1 até n. colocar os pares i j
## duvida deve ser n ou m?
tupla_q = []
for i in range(0,n-2):
    for j in range(i+1,n):
        if i < j:  # Verificando se o índice i é menor que o índice j
            #print(i,j)
            tupla_q.append((i,j))
#print(tupla_q)
## no sum 

## construir modelo
modelo = ConcreteModel()
## variáveis, dúvidas, do N
modelo.x = Var([i for i in range(n)], domain = Binary)
## do Q
modelo.y = Var([i for i in range(n)], [j for j in range(n)], domain = Binary)


## na função objetivo o primeiro de 0 até n-2, e o segundo vai de i até n-1
modelo.obj = Objective(expr = sum(matriz_d[i][j] * modelo.y[i,j] for i in range(0,n-2) for j in range(i,n-1)), sense = maximize)



## restricoes
## primeira restrição, de 0 até n-1 o for.
modelo.cons = ConstraintList()

# primeira,m elementos seja viável.

modelo.cons.add(expr = (sum(modelo.x[i] for i in range(0,n-1)) == m))
    #modelo.cons.add(expr = (sum(modelo.x[i]) == m))
#segunda
for i in range(0,n-2):
    for j in range(i+1,n):
        modelo.cons.add(modelo.x[i] + modelo.x[j] - modelo.y[i, j] <= 1)

#terceira
for i in range(0,n-2):
    for j in range(i+1,n):
            modelo.cons.add(-modelo.x[i] + modelo.y[i, j] <= 0)

#quarta
for i in range(0,n-2):
    for j in range(i+1,n):
            modelo.cons.add(-modelo.x[i] + modelo.y[i, j] <= 0)




opt = SolverFactory('glpk', executable='C:/glpk-4.65/w64/glpsol')
results = opt.solve(modelo)
#results.write()

for i in range(n):
    for j in range(n):
        if modelo.y[i, j]() == 1: print(f'{i} -> {j}')
print(f'Cost: {modelo.obj()}')
