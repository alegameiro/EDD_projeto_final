import csv
import random

def carregar_cidades(nome_arquivo="cidades_vizinhas.csv"):
    cidades_unicas = set() # Usamos um Set (conjunto) para não ter cidades repetidas
    try:
        # Lendo o arquivo CSV
        with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo, delimiter=',') 
            for linha in leitor:
                if len(linha) >= 2:
                    cidades_unicas.add(linha[0].strip())
                    cidades_unicas.add(linha[1].strip())
    except FileNotFoundError:
        print(f"Aviso: O arquivo '{nome_arquivo}' não foi encontrado na pasta.")
        
    return list(cidades_unicas)

def acao_cadastrar_pessoa(lista, cidades_disponiveis):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade: "))
    telefone = input("Digite o telefone: ")
    
    # Escolhe uma cidade aleatória da lista do CSV
    if cidades_disponiveis:
        cidade = random.choice(cidades_disponiveis)
    else:
        cidade = "Desconhecida"
        
    lista.inserir(nome, idade, telefone, cidade)
    print(f"Nome: {nome} | Idade: {idade} | Telefone: {telefone} | Cidade: {cidade}")

def acao_consultar_pessoa(lista):
    nome = input("Digite o nome da pessoa: ")
    pessoa = lista.buscar(nome)
    
    if pessoa:
        print(f"Nome: {pessoa.nome} | Idade: {pessoa.idade} | Telefone: {pessoa.telefone} | Cidade: {pessoa.cidade}")
    else:
        print("Pessoa não cadastrada. Tem certeza que o nome está certo?")

def acao_ver_quantidade(lista):
    qtd = lista.obter_tamanho()
    if qtd == 1:
        print("Há 1 pessoa na lista de espera.")
    else:
        print(f"São {qtd} pessoas na lista de espera.")