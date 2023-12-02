from Model.Aresta import Aresta

# classe que representa um grafo (grafos completos)
class Grafo:

  def __init__(self, num_vertices):
    self.num_vertices = num_vertices  # número de vértices do grafo
    self.arestas = {}  # dicionário com as arestas
    self.vizinhos = {}  # dicionário com todos os vizinhos de cada vértice

  def adicionarAresta(self, origem, destino, custo):
    aresta = Aresta(origem=origem, destino=destino, custo=custo)
    self.arestas[(origem, destino)] = aresta
    if origem not in self.vizinhos:
      self.vizinhos[origem] = [destino]
    else:
      self.vizinhos[origem].append(destino)

  def obterCustoAresta(self, origem, destino):
    return self.arestas[(origem, destino)].obterCusto()

  def obterFeromonioAresta(self, origem, destino):
    return self.arestas[(origem, destino)].obterFeronomio()

  def setFeromonioAresta(self, origem, destino, feromonio):
    self.arestas[(origem, destino)].setFeromonio(feromonio)

  def obterCustoCaminho(self, caminho):
    custo = 0
    for i in range(self.num_vertices - 1):
      custo += self.obterCustoAresta(caminho[i], caminho[i + 1])
    # adiciona o último custo
    custo += self.obterCustoAresta(caminho[-1], caminho[0])
    return custo

