from Model.Grafo import Grafo
import random

class GrafoCompleto(Grafo):
  # gera um grafo completo
  def gerar(self):
    for i in range(1, self.num_vertices + 1):
      for j in range(1, self.num_vertices + 1):
        if i != j:
          peso = random.randint(1, 10)
          self.adicionarAresta(i, j, peso)