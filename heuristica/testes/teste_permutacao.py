import random

def perturbacao(lista, porcentagem):
 # Determine quantos elementos serão permutados
 num_permutacoes = int(len(lista) * porcentagem)
 
 # Selecione aleatoriamente os elementos a serem permutados
 indices_selecionados = random.sample(range(len(lista)), num_permutacoes)
 
 # Faça o swap dos elementos selecionados
 for i in indices_selecionados:
     # Encontre um elemento não selecionado
     j = next(j for j in range(len(lista)) if j not in indices_selecionados and lista[j] == 0)
     
     # Faça o swap
     lista[i], lista[j] = lista[j], lista[i]
 return lista


def permuta_aleatoria(lista, porcentagem):
   # Encontra o número de elementos que serão permutados
   num_permutacoes = int(len(lista) * porcentagem / 100)
   
   # Encontra os índices dos elementos 1
   indices_1 = [i for i, x in enumerate(lista) if x == 1]
   
   # Encontra os índices dos elementos 0
   indices_0 = [i for i, x in enumerate(lista) if x == 0]
   
   # Realiza as permutações
   for _ in range(num_permutacoes):
       # Escolhe aleatoriamente um índice de 1 e um índice de 0
       indice_1 = random.choice(indices_1)
       indice_0 = random.choice(indices_0)
       
       # Troca o elemento 1 pelo elemento 0
       lista[indice_1], lista[indice_0] = lista[indice_0], lista[indice_1]
   
   return lista

def permuta_sem_aleatoria(lista, porcentagem):
  # Encontra o número de elementos que serão permutados
  num_permutacoes = int(len(lista) * porcentagem / 100)
  
  # Encontra os índices dos elementos 1
  indices_1 = [i for i, x in enumerate(lista) if x == 1]
  
  # Encontra os índices dos elementos 0
  indices_0 = [i for i, x in enumerate(lista) if x == 0]
  
  # Realiza as permutações
  for _ in range(num_permutacoes):
      # Escolhe um índice de 1 e um índice de 0
      indice_1 = indices_1.pop(0)
      indice_0 = indices_0.pop(0)
      
      # Troca o elemento 1 pelo elemento 0
      lista[indice_1], lista[indice_0] = lista[indice_0], lista[indice_1]
  
  return lista

def permuta_com_saida(lista, porcentagem):
 # Encontra o número de elementos que serão permutados
 num_permutacoes = int(len(lista) * porcentagem / 100)
 
 # Encontra os índices dos elementos 1
 indices_1 = [i for i, x in enumerate(lista) if x == 1]
 
 # Encontra os índices dos elementos 0
 indices_0 = [i for i, x in enumerate(lista) if x == 0]
 
 print(f"Lista original: {lista}")
 print(f"Índices dos elementos 1: {indices_1}")
 print(f"Índices dos elementos 0: {indices_0}")
 
 # Realiza as permutações
 for _ in range(num_permutacoes):
     # Escolhe um índice de 1 e um índice de 0
     indice_1 = indices_1.pop(0)
     indice_0 = indices_0.pop(0)
     
     # Troca o elemento 1 pelo elemento 0
     lista[indice_1], lista[indice_0] = lista[indice_0], lista[indice_1]
     
     print(f"Lista após a permutação: {lista}")
 
 return lista

def permuta_forcada(lista_original, porcentagem):
   # Encontra o número de elementos que serão permutados
   num_permutacoes = int(len(lista_original) * porcentagem / 100)
   
   # Encontra os índices dos elementos 1
   indices_1 = [i for i, x in enumerate(lista_original) if x == 1]
   
   # Encontra os índices dos elementos 0
   indices_0 = [i for i, x in enumerate(lista_original) if x == 0]
   
   # Realiza as permutações
   for _ in range(num_permutacoes):
       # Escolhe um índice de 1 e um índice de 0
       indice_1 = indices_1.pop(0)
       indice_0 = indices_0.pop(0)
       
       # Troca o elemento 1 pelo elemento 0
       lista[indice_1], lista[indice_0] = lista[indice_0], lista[indice_1]
   
   # Verifica se a lista permutada é igual à lista original
   while lista == lista_original:
       # Se for igual, faz mais permutações
       permuta_aleatoria(lista, porcentagem)
   
   return lista


import random

def permuta_aleatoria_teste(lista, porcentagem):
  # Encontra o número de elementos que serão permutados
  num_permutacoes = int(len(lista) * porcentagem / 100)
  
  # Encontra os índices dos elementos 1
  indices_1 = [i for i, x in enumerate(lista) if x == 1]
  
  # Encontra os índices dos elementos 0
  indices_0 = [i for i, x in enumerate(lista) if x == 0]
  
  # Realiza as permutações
  for _ in range(num_permutacoes):
      # Escolhe um índice de 1 e um índice de 0 aleatoriamente
      indice_1 = random.choice(indices_1)
      indice_0 = random.choice(indices_0)
      
      # Troca o elemento 1 pelo elemento 0
      lista[indice_1], lista[indice_0] = lista[indice_0], lista[indice_1]
  
  return lista


# Exemplo de uso
lista = [0, 0, 0, 0, 1, 1, 0, 0, 0, 1]
porcentagem = 0.2
print(perturbacao(lista, porcentagem))
print(permuta_aleatoria(lista,porcentagem))
print(permuta_sem_aleatoria(lista, porcentagem))
print(permuta_com_saida(lista,porcentagem))
#print(permuta_forcada(lista,porcentagem))
print(permuta_aleatoria_teste(lista, porcentagem))
lista == lista_original
