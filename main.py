from Model.Aco import ACO
from Model.Grafo import Grafo

def carregarGrafo():
    with open('grafo_caixeiro_viajante.txt', 'r') as arquivo:
        for linha in arquivo:
                # Dividindo a linha em partes
                partes = linha.strip().split(',')

                # Extraindo origem, destino e custo
                origem = int(partes[0])
                destino = int(partes[1])
                custo = int(partes[2])

                print(custo)

                # Criando um objeto Aresta e adicionando à lista
                grafo.adicionarAresta(origem, destino, custo)

def carregarGrafoManualmente():
        # # adiciona as arestas
        grafo.adicionarAresta(2, 1, 42)
        grafo.adicionarAresta(1, 2, 42)
        grafo.adicionarAresta(3, 1, 61)
        grafo.adicionarAresta(1, 3, 61)
        grafo.adicionarAresta(3, 2, 14)
        grafo.adicionarAresta(2, 3, 14)
        grafo.adicionarAresta(4, 1, 30)
        grafo.adicionarAresta(1, 4, 30)
        grafo.adicionarAresta(4, 2, 87)
        grafo.adicionarAresta(2, 4, 87)
        grafo.adicionarAresta(4, 3, 20)
        grafo.adicionarAresta(3, 4, 20)
        grafo.adicionarAresta(5, 1, 17)
        grafo.adicionarAresta(1, 5, 17)
        grafo.adicionarAresta(5, 2, 28)
        grafo.adicionarAresta(2, 5, 28)
        grafo.adicionarAresta(5, 3, 81)
        grafo.adicionarAresta(3, 5, 81)
        grafo.adicionarAresta(5, 4, 34)
        grafo.adicionarAresta(4, 5, 34)
        grafo.adicionarAresta(6, 1, 82)
        grafo.adicionarAresta(1, 6, 82)
        grafo.adicionarAresta(6, 2, 70)
        grafo.adicionarAresta(2, 6, 70)
        grafo.adicionarAresta(6, 3, 21)
        grafo.adicionarAresta(3, 6, 21)
        grafo.adicionarAresta(6, 4, 33)
        grafo.adicionarAresta(4, 6, 33)
        grafo.adicionarAresta(6, 5, 41)
        grafo.adicionarAresta(5, 6, 41)
        grafo.adicionarAresta(7, 1, 31)
        grafo.adicionarAresta(1, 7, 31)
        grafo.adicionarAresta(7, 2, 19)
        grafo.adicionarAresta(2, 7, 19)
        grafo.adicionarAresta(7, 3, 8)
        grafo.adicionarAresta(3, 7, 8)
        grafo.adicionarAresta(7, 4, 91)
        grafo.adicionarAresta(4, 7, 91)
        grafo.adicionarAresta(7, 5, 34)
        grafo.adicionarAresta(5, 7, 34)
        grafo.adicionarAresta(7, 6, 19)
        grafo.adicionarAresta(6, 7, 19)
        grafo.adicionarAresta(8, 1, 11)
        grafo.adicionarAresta(1, 8, 11)
        grafo.adicionarAresta(8, 2, 33)
        grafo.adicionarAresta(2, 8, 33)
        grafo.adicionarAresta(8, 3, 29)
        grafo.adicionarAresta(3, 8, 29)
        grafo.adicionarAresta(8, 4, 10)
        grafo.adicionarAresta(4, 8, 10)
        grafo.adicionarAresta(8, 5, 82)
        grafo.adicionarAresta(5, 8, 82)
        grafo.adicionarAresta(8, 6, 32)
        grafo.adicionarAresta(6, 8, 32)
        grafo.adicionarAresta(8, 7, 59)
        grafo.adicionarAresta(7, 8, 59)


num_vertices = 8
# cria um grafo passando o número de vértices
grafo = Grafo(num_vertices)

#carregarGrafo()
carregarGrafoManualmente()


# cria uma instância de ACO
aco = ACO(grafo=grafo,
        num_formigas=grafo.num_vertices,
        alfa=1.0,
        beta=5.0,
        iteracoes=1000,
        evaporacao=0.5)
# roda o algoritmo
aco.rodar()