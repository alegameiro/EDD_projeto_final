from estruturas_de_dados import ListaEncadeada
import atribuicoes_secretario as sec

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

if __name__ == "__main__":
    main()