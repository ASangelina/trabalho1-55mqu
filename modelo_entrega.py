import os
import csv
from pyomo.environ import *
import time


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

imprimir_nomes_arquivos(nomes_arquivos)
numero = int(input("Digite o número correspondente ao arquivo que deseja usar no modelo: "))
if 1 <= numero <= len(nomes_arquivos):
    instancia = pasta_inst + str(nomes_arquivos[numero - 1])
    #print(f"Você selecionou o arquivo: {arquivo_selecionado}")
else:
    print("Número inválido. Por favor, escolha um número válido.")

matriz_d,m,n = popula_matriz(instancia)


tupla_q = []
for i in range(n):
    for j in range(i+1,n):
        tupla_q.append((i,j))
#print(tupla_q)

## construir modelo
modelo = ConcreteModel()
## variáveis
modelo.x = Var([i for i in range(n)], domain = Binary)

modelo.y = Var([i for i in range(n)], [j for j in range(n)], domain = Binary)


modelo.obj = Objective(expr = sum(matriz_d[i][j] * modelo.y[i,j] for i in range(n) for j in range(i+1,n)), sense = maximize)

## restricoes
modelo.cons = ConstraintList()

# primeira,m elementos seja viável.

modelo.cons.add(expr = (sum(modelo.x[i] for i in range(n)) == m))
    #modelo.cons.add(expr = (sum(modelo.x[i]) == m))
#segunda
for pair in tupla_q:
    i = pair[0]
    j = pair[1]
    modelo.cons.add(modelo.x[i] + modelo.x[j] - modelo.y[i, j] <= 1)

#terceira
for pair in tupla_q:
    i = pair[0]
    j = pair[1]
    modelo.cons.add(-modelo.x[i] + modelo.y[i, j] <= 0)

#terceira
for i in range(0,n-2):
    for j in range(i+1,n):
            modelo.cons.add(-modelo.x[i] + modelo.y[i, j] <= 0)


start_time = time.time()
#opt = SolverFactory('glpk', executable='C:/glpk-4.65/w64/glpsol')
opt = SolverFactory('glpk')
results = opt.solve(modelo)
end_time = time.time()
#results.write()

execution_time = end_time - start_time
for i in range(n):
    if modelo.x[i]() == 1: print(i)
    #for j in range(n):
    #    if modelo.y[i, j]() == 1: print(f'{i} -> {j}')


if str(results.solver.termination_condition) == "optimal":
    print("Solução ótima encontrada")
    print("Valor da função objetivo:", modelo.obj())
    print("Tempo de execução:", end_time - start_time, "segundos")
else:
    print("Otimização terminou com status:", results.solver.termination_condition)

def results_salva(output_file,ins,valor_objetivo,time_exec):
    with open(output_file, 'a', newline='') as file:
        resultado = [ins, str(valor_objetivo), str(time_exec)] 
        writer = csv.writer(file)
        writer.writerow(resultado)


resultados_execucao = results_salva('resultados_exec.csv',instancia,modelo.obj(),end_time - start_time)