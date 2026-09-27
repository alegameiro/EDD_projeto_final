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