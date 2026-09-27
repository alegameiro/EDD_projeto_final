from estruturas_de_dados import ListaEncadeada
import atribuicoes_secretario as sec
import atribuicoes_diretor as dir
import atribuicoes_assistente as ass

def main():
    # 1. Inicializa a estrutura
    lista_de_espera = ListaEncadeada()
    
    # 2. Carrega as cidades do arquivo CSV referenciado
    cidades = sec.carregar_cidades("cidades_vizinhas.csv")
    
    # ======================================================
    # PERFIL 1: SECRETÁRIO(A)
    # ======================================================
    print("-------- Olá, Secretário(a)! --------\n")
    
    while True:
        print("Você deseja:")
        print("(1) Cadastrar nova pessoa na lista de espera.")
        print("(2) Consultar pessoa cadastrada.")
        print("(3) Ver quantidade de pessoas cadastradas.")
        print("(4) Finalizar execução.")
        
        opcao = input("Digite sua opção: ")
        
        if opcao == '1':
            sec.acao_cadastrar_pessoa(lista_de_espera, cidades)
        elif opcao == '2':
            sec.acao_consultar_pessoa(lista_de_espera)
        elif opcao == '3':
            sec.acao_ver_quantidade(lista_de_espera)
        elif opcao == '4':
            print("Fim das atividades sob responsabilidade do(a) Secretário(a).\n")
            break
        else:
            print("Opção inválida. Digite um número de 1 a 4.")
        print()

    # ======================================================
    # TRANSIÇÃO: CONVERTER LISTA PARA ÁRVORE BINÁRIA
    # ======================================================
    arvore_de_espera = dir.converter_lista_para_arvore(lista_de_espera)

    # ======================================================
    # PERFIL 2: DIRETOR(A)
    # ======================================================
    print("\n-------- Olá, Diretor(a)! --------\n")
    
    while True:
        print("Você deseja:")
        print("(1) Alterar nome, idade ou telefone de pessoa cadastrada.")
        print("(2) Descadastrar pessoa.")
        print("(3) Obter informações da primeira pessoa em ordem alfabética de nome.")
        print("(4) Obter informações da última pessoa em ordem alfabética de nome.")
        print("(5) Confirmar validade da lista de espera e finalizar execução.")
        
        opcao = input("Digite sua opção: ")
        
        if opcao == '1':
            dir.acao_alterar_dados(arvore_de_espera)
        elif opcao == '2':
            dir.acao_descadastrar(arvore_de_espera)
        elif opcao == '3':
            dir.acao_primeiro_alfabetico(arvore_de_espera)
        elif opcao == '4':
            dir.acao_ultimo_alfabetico(arvore_de_espera)
        elif opcao == '5':
            print("Fim das atividades sob responsabilidade do(a) Diretor(a).\n")
            break
        else:
            print("Opção inválida. Digite um número de 1 a 5.")
        print() 

    
    # ======================================================
    # TRANSIÇÃO: PREPARAR O GRAFO
    # ======================================================
    grafo_cidades = ass.carregar_grafo("cidades_vizinhas.csv")

    # ======================================================
    # PERFIL 3: ASSISTENTE
    # ======================================================
    print("\n-------- Olá, Assistente! --------\n")
    
    while True:
        print("Você deseja:")
        print("(1) Ver a menor distância entre a cidade da escola e a cidade de uma pessoa.")
        print("(2) Ver a menor distância da cidade da escola até a cidade da pessoa passando por uma cidade específica.")
        print("(3) Ver dados da(s) pessoa(s) que mora(m) na cidade mais perto da cidade da escola (incluindo distância).")
        print("(4) Finalizar execução.")
        
        opcao = input("Digite sua opção: ")
        
        if opcao == '1':
            ass.acao_menor_distancia_pessoa(arvore_de_espera, grafo_cidades)
        elif opcao == '2':
            ass.acao_menor_distancia_indaiatuba(arvore_de_espera, grafo_cidades)
        elif opcao == '3':
            ass.acao_cidade_mais_proxima(arvore_de_espera, grafo_cidades)
        elif opcao == '4':
            print("Fim da execução do sistema.")
            break
        else:
            print("Opção inválida. Digite um número de 1 a 4.")
        print()

if __name__ == "__main__":
    main()