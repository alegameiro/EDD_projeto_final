from estruturas_de_dados import ArvoreBinariaBusca

def converter_lista_para_arvore(lista_de_espera):
    arvore = ArvoreBinariaBusca()
    atual = lista_de_espera.cabeca
    while atual is not None:
        arvore.inserir(atual.nome, atual.idade, atual.telefone, atual.cidade)
        atual = atual.proximo
    return arvore

def acao_alterar_dados(arvore):
    nome_busca = input("Digite o nome da pessoa que você quer editar: ")
    pessoa = arvore.buscar(nome_busca)
    
    if pessoa is None:
        print("Pessoa não cadastrada. Tem certeza que o nome está certo?")
        return
        
    print(f"Nome: {pessoa.nome} | Idade: {pessoa.idade} | Telefone: {pessoa.telefone} | Cidade: {pessoa.cidade}")
    escolha = input("O que você quer editar? Digite 1 para nome, 2 para idade ou 3 para telefone: ")
    
    if escolha == '1':
        novo_nome = input("Digite o novo nome: ")
        # Como o nome é a chave da BST, precisamos remover o nó e reinseri-lo.
        idade = pessoa.idade
        telefone = pessoa.telefone
        cidade = pessoa.cidade
        arvore.remover(pessoa.nome)
        arvore.inserir(novo_nome, idade, telefone, cidade)
        print("Dados atualizados com sucesso.")
    elif escolha == '2':
        nova_idade = int(input("Digite a nova idade: "))
        pessoa.idade = nova_idade
        print("Dados atualizados com sucesso.")
    elif escolha == '3':
        novo_telefone = input("Digite o novo telefone: ")
        pessoa.telefone = novo_telefone
        print("Dados atualizados com sucesso.")
    else:
        print("Opção inválida.")

def acao_descadastrar(arvore):
    nome_busca = input("Digite o nome da pessoa que você quer descadastrar: ")
    pessoa = arvore.buscar(nome_busca)
    
    if pessoa is None:
         print("Pessoa não cadastrada ou lista de espera vazia. Tem certeza que o nome da pessoa está certo?")
         return
         
    print(f"Nome: {pessoa.nome} | Idade: {pessoa.idade} | Telefone: {pessoa.telefone} | Cidade: {pessoa.cidade}")
    confirmacao = input(f"Tem certeza que deseja descadastrar {pessoa.nome}? Digite S ou N: ").upper()
    
    if confirmacao == 'S':
        arvore.remover(pessoa.nome)
        print(f"{pessoa.nome} descadastrado com sucesso.")
    else:
        print("Operação cancelada.")

def acao_primeiro_alfabetico(arvore):
    primeiro = arvore.minimo()
    if primeiro:
        print(f"Nome: {primeiro.nome} | Idade: {primeiro.idade} | Telefone: {primeiro.telefone} | Cidade: {primeiro.cidade}")
    else:
        print("A lista de espera está vazia.")

def acao_ultimo_alfabetico(arvore):
    ultimo = arvore.maximo()
    if ultimo:
        print(f"Nome: {ultimo.nome} | Idade: {ultimo.idade} | Telefone: {ultimo.telefone} | Cidade: {ultimo.cidade}")
    else:
        print("A lista de espera está vazia.")