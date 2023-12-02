# classe que representa uma formiga
class Formiga:

  def __init__(self, cidade):
    self.cidade = cidade
    self.solucao = []
    self.custo = None

  def obterCidade(self):
    return self.cidade

  def setCidade(self, cidade):
    self.cidade = cidade

  def obterSolucao(self):
    return self.solucao

  def setSolucao(self, solucao, custo):
    # atualiza a solução
    if not self.custo:
      self.solucao = solucao[:]
      self.custo = custo
    else:
      if custo < self.custo:
        self.solucao = solucao[:]
        self.custo = custo

  def obterCustoSolucao(self):
    return self.custo