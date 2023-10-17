import numpy as np
import csv
def tamanho_matriz(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            valores = line.split(' ')
            n = int(valores[0])
            m = int(valores[1])
    return n, m

def popula_matriz(file_path):
    valores = []
    with open(file_path, 'r') as file:
        for line in file:
            valores_l = line.split(' ')
            if len(valores_l) > 2:
                valor = float(valores_l[2])
                #matriz_distancia[l][c] = valor
                valores.append(valor)
            else:
                x = int(valores_l[0])
                y = int(valores_l[1])


    contador = 0
    matriz_distancia = [[0 for j in range(x)] for i in range(x)]
    for j in range(x-1):
        for i in range(x):
            if(i > j):
                matriz_distancia[i][j] = valores[contador]
                contador += 1
            else:
                matriz_distancia[i][j] = 0
    #matriz_distancia = np.array(valores).reshape(n, m)
    return matriz_distancia,x,y

def salvar_matriz_como_csv(matriz, output_file):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in matriz:
            writer.writerow(row)
# Use as funções
#file_path = 'instancias/GKD-c_1_n500_m50.txt'
file_path = 'instanciasteste\SOM-b_1_n100_m10.txt' 
linhas_matriz, colunas_matriz = tamanho_matriz(file_path)
#construção da matriz com tamanhos
#matriz_distancia = [[0 for j in range(linhas_matriz)] for i in range(linhas_matriz)]
print("esse eh o m",linhas_matriz)
print("esse eh o n",colunas_matriz)
#print(len(matriz_distancia))
#num_colunas = len(matriz_distancia[0]) if matriz_distancia else 0  # Verifica se a matriz não está vazia
#print(num_colunas)

matriz_teste,t1,t2 = popula_matriz(file_path)
print(matriz_teste)


salvar_matriz_como_csv(matriz_teste,'instanciasteste/matriz100.csv')
