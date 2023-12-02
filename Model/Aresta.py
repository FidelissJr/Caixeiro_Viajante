# classe que representa uma aresta
class Aresta:

  def __init__(self, origem, destino, custo):
    self.origem = origem
    self.destino = destino
    self.custo = custo
    self.feromonio = None

  def obterOrigem(self):
    return self.origem

  def obterDestino(self):
    return self.destino

  def obterCusto(self):
    return self.custo

  def obterFeronomio(self):
    return self.feromonio

  def setFeromonio(self, feromonio):
    self.feromonio = feromonio
