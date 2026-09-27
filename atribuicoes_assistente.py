import csv
from estruturas_de_dados import Grafo

def carregar_grafo(nome_arquivo="cidades_vizinhas.csv"):
    grafo = Grafo()
    try:
        with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
            # Se houver erro de leitura, tente alterar delimiter para ';'
            leitor = csv.reader(arquivo, delimiter=';')
            for linha in leitor:
                if len(linha) >= 3:
                    cidade1 = linha[0].strip()
                    cidade2 = linha[1].strip()
                    distancia = int(linha[2].strip())
                    grafo.adicionar_aresta(cidade1, cidade2, distancia)
    except FileNotFoundError:
        print(f"Aviso: O arquivo '{nome_arquivo}' não foi encontrado.")
    return grafo

def acao_menor_distancia_pessoa(arvore, grafo):
    nome_busca = input("Digite o nome da pessoa cuja cidade te interessa: ")
    pessoa = arvore.buscar(nome_busca)
    
    if pessoa is None:
        print("Pessoa não cadastrada ou lista de espera vazia. Tem certeza que o nome da pessoa está certo?")
        return
        
    print(f"Nome: {pessoa.nome} | Idade: {pessoa.idade} | Telefone: {pessoa.telefone} | Cidade: {pessoa.cidade}")
    
    origem = 'Guarujá'
    destino = pessoa.cidade
    
    distancias, caminhos = grafo.dijkstra(origem)
    custo = distancias.get(destino, float('inf'))
    trajeto = grafo.reconstruir_caminho(caminhos, origem, destino)
    
    print(f"Menor caminho = {trajeto} com custo {custo}")

def acao_menor_distancia_indaiatuba(arvore, grafo):
    nome_busca = input("Digite o nome da pessoa cuja cidade te interessa: ")
    pessoa = arvore.buscar(nome_busca)
    
    if pessoa is None:
        print("Pessoa não cadastrada ou lista de espera vazia. Tem certeza que o nome da pessoa está certo?")
        return
        
    print(f"Nome: {pessoa.nome} | Idade: {pessoa.idade} | Telefone: {pessoa.telefone} | Cidade: {pessoa.cidade}")
    
    # Trecho 1: Guarujá -> Indaiatuba
    dist_ate_indaiatuba, caminhos1 = grafo.dijkstra('Guarujá')
    custo1 = dist_ate_indaiatuba.get('Indaiatuba', float('inf'))
    trajeto1 = grafo.reconstruir_caminho(caminhos1, 'Guarujá', 'Indaiatuba')
    
    # Trecho 2: Indaiatuba -> Cidade do Destino
    dist_ate_destino, caminhos2 = grafo.dijkstra('Indaiatuba')
    custo2 = dist_ate_destino.get(pessoa.cidade, float('inf'))
    trajeto2 = grafo.reconstruir_caminho(caminhos2, 'Indaiatuba', pessoa.cidade)
    
    custo_total = custo1 + custo2
    # Combinamos os trajetos removendo a duplicata de 'Indaiatuba' no meio
    trajeto_completo = trajeto1[:-1] + trajeto2
    
    print(f"Menor caminho = {trajeto_completo} com custo {custo_total}")

def acao_cidade_mais_proxima(arvore, grafo):
    # Precisamos de um dicionário agrupando todas as pessoas por cidade
    moradores_por_cidade = {}
    
    # Função recursiva auxiliar para varrer a árvore e coletar as cidades
    def _coletar_moradores(no):
        if no is not None:
            _coletar_moradores(no.esquerda)
            
            if no.cidade not in moradores_por_cidade:
                moradores_por_cidade[no.cidade] = []
            moradores_por_cidade[no.cidade].append(no)
            
            _coletar_moradores(no.direita)
            
    _coletar_moradores(arvore.raiz)
    
    if not moradores_por_cidade:
        print("A lista de espera está vazia.")
        return
        
    distancias, _ = grafo.dijkstra('Guarujá')
    
    cidade_mais_proxima = None
    menor_distancia = float('inf')
    
    # Avalia a distância apenas das cidades que têm moradores na lista
    for cidade in moradores_por_cidade.keys():
        dist = distancias.get(cidade, float('inf'))
        if dist < menor_distancia:
            menor_distancia = dist
            cidade_mais_proxima = cidade
            
    if cidade_mais_proxima:
        print(f"A cidade mais próxima à cidade da escola que tem moradores na lista de espera (ver abaixo) é {cidade_mais_proxima}. Distância = {menor_distancia}")
        for pessoa in moradores_por_cidade[cidade_mais_proxima]:
            print(f"Nome: {pessoa.nome} | Idade: {pessoa.idade} | Telefone: {pessoa.telefone} | Cidade: {pessoa.cidade}")
    else:
        print("Não foi possível calcular a rota para as cidades cadastradas.")