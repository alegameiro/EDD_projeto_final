#--------------------------------------------------------
#              LISTA ENCADEADA
#--------------------------------------------------------
class No:
    def __init__(self, nome, idade, telefone, cidade):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cidade = cidade
        self.proximo = None  # Aponta para o próximo nó da lista

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0

    def inserir(self, nome, idade, telefone, cidade):
        novo_no = No(nome, idade, telefone, cidade)
        
        # Se a lista estiver vazia, o novo nó se torna a cabeça
        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            # Caso contrário, percorremos até o final para inserir
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no
            
        self.tamanho += 1

    def buscar(self, nome):
        atual = self.cabeca
        while atual is not None:
            # Buscamos ignorando diferenças de maiúsculas/minúsculas
            if atual.nome.lower() == nome.lower():
                return atual
            atual = atual.proximo
        return None

    def obter_tamanho(self):
        return self.tamanho


#--------------------------------------------------------
#          ÁRVORE E BUSCA BINÁRIA
#--------------------------------------------------------
class NoArvore:
    def __init__(self, nome, idade, telefone, cidade):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cidade = cidade
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, nome, idade, telefone, cidade):
        if self.raiz is None:
            self.raiz = NoArvore(nome, idade, telefone, cidade)
        else:
            self._inserir_recursivo(self.raiz, nome, idade, telefone, cidade)

    def _inserir_recursivo(self, no_atual, nome, idade, telefone, cidade):
        # Ignora diferenças entre maiúsculas e minúsculas na ordenação
        if nome.lower() < no_atual.nome.lower():
            if no_atual.esquerda is None:
                no_atual.esquerda = NoArvore(nome, idade, telefone, cidade)
            else:
                self._inserir_recursivo(no_atual.esquerda, nome, idade, telefone, cidade)
        elif nome.lower() > no_atual.nome.lower():
            if no_atual.direita is None:
                no_atual.direita = NoArvore(nome, idade, telefone, cidade)
            else:
                self._inserir_recursivo(no_atual.direita, nome, idade, telefone, cidade)
        else:
            pass # Nomes iguais: não haverá duplicidade segundo a especificação

    def buscar(self, nome):
        return self._buscar_recursivo(self.raiz, nome)

    def _buscar_recursivo(self, no_atual, nome):
        if no_atual is None:
            return None
        if nome.lower() == no_atual.nome.lower():
            return no_atual
        elif nome.lower() < no_atual.nome.lower():
            return self._buscar_recursivo(no_atual.esquerda, nome)
        else:
            return self._buscar_recursivo(no_atual.direita, nome)

    def minimo(self):
        atual = self.raiz
        if atual is None: return None
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def maximo(self):
        atual = self.raiz
        if atual is None: return None
        while atual.direita is not None:
            atual = atual.direita
        return atual

    def remover(self, nome):
        self.raiz, removido = self._remover_recursivo(self.raiz, nome)
        return removido

    def _remover_recursivo(self, no, nome):
        if no is None:
            return no, False

        if nome.lower() < no.nome.lower():
            no.esquerda, removido = self._remover_recursivo(no.esquerda, nome)
        elif nome.lower() > no.nome.lower():
            no.direita, removido = self._remover_recursivo(no.direita, nome)
        else:
            removido = True
            # Caso 1 e 2: Um ou nenhum filho
            if no.esquerda is None:
                return no.direita, removido
            elif no.direita is None:
                return no.esquerda, removido
            
            # Caso 3: Dois filhos (Pega o menor valor da subárvore direita)
            sucessor = no.direita
            while sucessor.esquerda is not None:
                sucessor = sucessor.esquerda
            
            # Copia os dados do sucessor para o nó atual
            no.nome = sucessor.nome
            no.idade = sucessor.idade
            no.telefone = sucessor.telefone
            no.cidade = sucessor.cidade
            
            # Remove o sucessor da subárvore direita
            no.direita, _ = self._remover_recursivo(no.direita, sucessor.nome)

        return no, removido


#--------------------------------------------------------
#                   GRAFO
#--------------------------------------------------------
import heapq

class Grafo:
    def __init__(self):
        # Usaremos um dicionário de adjacências
        self.adjacencias = {}

    def adicionar_aresta(self, u, v, peso):
        if u not in self.adjacencias:
            self.adjacencias[u] = []
        if v not in self.adjacencias:
            self.adjacencias[v] = []
        
        # Como é não-direcionado, a aresta vai para ambos os lados
        self.adjacencias[u].append((v, peso))
        self.adjacencias[v].append((u, peso))

    def dijkstra(self, origem):
        """
        Retorna dois dicionários: as distâncias mínimas da origem para todos os vértices
        e o dicionário de caminhos (para reconstruir a rota).
        """
        distancias = {vertice: float('inf') for vertice in self.adjacencias}
        distancias[origem] = 0
        caminho_anterior = {vertice: None for vertice in self.adjacencias}
        
        # Fila de prioridade armazena tuplas (distancia_acumulada, vertice_atual)
        pq = [(0, origem)]

        while pq:
            dist_atual, vertice_atual = heapq.heappop(pq)

            # Se a distância atual for maior que a registrada, ignoramos (caminho obsoleto)
            if dist_atual > distancias[vertice_atual]:
                continue

            for vizinho, peso in self.adjacencias[vertice_atual]:
                distancia = dist_atual + peso
                
                # Se encontramos um caminho mais curto para o vizinho
                if distancia < distancias[vizinho]:
                    distancias[vizinho] = distancia
                    caminho_anterior[vizinho] = vertice_atual
                    heapq.heappush(pq, (distancia, vizinho))
                    
        return distancias, caminho_anterior

    def reconstruir_caminho(self, caminho_anterior, origem, destino):
        caminho = []
        atual = destino
        while atual is not None:
            caminho.append(atual)
            if atual == origem:
                break
            atual = caminho_anterior[atual]
            
        caminho.reverse() # Inverte para ficar da origem ao destino
        return caminho