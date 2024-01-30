def gerar_vizinhos(lista):
  # Encontre os índices dos elementos 1 na lista
  indices_1 = [i for i, x in enumerate(lista) if x == 1]
  
  # Para cada índice de um elemento 1, encontre todos os índices dos elementos 0 à esquerda e à direita
  for i in indices_1:
      indices_0 = [j for j in range(len(lista)) if lista[j] == 0 and j != i]
      
      # Para cada índice de um elemento 0, gera uma nova lista trocando o elemento 1 pelo elemento 0
      for j in indices_0:
          nova_lista = lista[:]
          nova_lista[i], nova_lista[j] = nova_lista[j], nova_lista[i]
          yield nova_lista



lista = [1, 1, 0, 0, 0, 0, 0, 1, 0, 0]
print("inicial",lista)
viz = 0
for vizinho in gerar_vizinhos(lista):
    viz += 1
    print("vizinho",viz,vizinho)
