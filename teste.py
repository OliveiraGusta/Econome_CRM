import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_sequencia():
    for i in range(1, 6):
        print(f"Olá {i}")

def exibir_menu():
    print("------------------------")
    print("Digite 'limpar' para apagar a sequência")
    print("------------------------")

def main():
    exibir_menu()
    while True:
        comando = input("Digite um comando: ")
        if comando == 'limpar':
            limpar_tela()
            print("Apagou")
            break
        else:
            imprimir_sequencia()

if __name__ == "__main__":
    main()
