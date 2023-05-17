# Gustavo Rodrigues e Mateus Marana

import random

def main():

    menu = [
        '',
        '------------------------------------------',
        '$      |      ECONO-ME BANK      |       $',
        '------------------------------------------',
        '',
        'Usuarios',
        ' Digite 1 - Cadastrar Novo Cliente',
        ' Digite 2 - Apagar Cliente pelo CPF',
        ' Digite 3 - Listar os Clientes Existentes',
        '',
        'Conta',
        ' Digite 4 - Debitar um Valor na Conta',
        ' Digite 5 - Depositar um Valor na Conta',
        ' Digite 6 - Tirar Extrato',
        ' Digite 7 - Transferir um Valor',
        ' Digite 8 - Investir um Valor',
        '',
        'Sair',
        ' Digite 9 - Fechar o programa',
        ''
    ]

    appBanco = {
        'usuarios': [],
        'contas': []
    }

    investimentos_menu = [
        '',
        ' Digite 1 - Criptmoedas',
        ' Digite 2 - Fundo Conservador',
        ' Digite 3 - Fundo Imobiliario',
        ' Digite 4 - Fundo de Ações',
        ' Digite 5 - Poupança',
        ' Digite 6 - Cancelar',
        ''
    ]

    def gerar_valor_aleatorio():
        return random.random()

    opcoes_investimentos = {
        '1': gerar_valor_aleatorio,
        '2': gerar_valor_aleatorio,
        '3': gerar_valor_aleatorio,
        '4': gerar_valor_aleatorio,
        '5': gerar_valor_aleatorio,
    }

    def calcular_retorno_investimento(valor_investido, taxa_retorno):
        return valor_investido * (taxa_retorno)
    
    def limpar_tela():
        linhas_terminal = 40  # número de linhas do terminal
        for _ in range(linhas_terminal):
            print()

    def exibir_menu():
        for linha in menu:
            print(linha)

    def novo_cliente():
        nome = input("Digite o nome do usuário: ")
        cpf = input("Digite o CPF do usuário: ")
        tipo_conta = input("Digite o tipo da conta: ")
        senha = input("Digite a senha do usuário: ")
        valor = float(input("Digite o valor inicial da conta: "))

        for usuario in appBanco['usuarios']:
            if usuario['cpf'] == cpf:
                print("\nCPF já cadastrado. O usuário não será cadastrado novamente.")
                return

        usuario = {
            'nome': nome,
            'senha': senha,
            'cpf': cpf
        }
        conta = {
            'usuario': usuario,
            'saldo': valor,
            'tipoConta': tipo_conta,
            'transacoes': []
        }
        appBanco['usuarios'].append(usuario)
        appBanco['contas'].append(conta)
        print("\nUsuário cadastrado com sucesso!\n")

    def apagar_cliente():
        cpf = input("Digite o CPF do usuário a ser excluído: ")
        print()
        for i, usuario in enumerate(appBanco['usuarios']):
            if usuario['cpf'] == cpf:
                del appBanco['usuarios'][i]
                del appBanco['contas'][i]
                print("Usuário excluído com sucesso!")
                return
        print("\nUsuário não encontrado.")

    def listar_clientes():
        if len(appBanco['usuarios']) == 0 or len(appBanco['contas']) == 0:
            print("Não há clientes cadastrados.")
            return

        print("------------------------------------------")
        print("|   Nome   |      CPF       |     Valor  |")
        print("------------------------------------------")
        for usuario, conta in zip(appBanco['usuarios'], appBanco['contas']):
            nome = usuario['nome']
            cpf = usuario['cpf']
            saldo = conta['saldo']
            print(f"| {nome:<8} | {cpf:<14} | R${saldo:<14.2f}")
        print("------------------------------------------")

    def debitar_valor():
        print("Entrou na função Debitar Valor")
        cpf = input("Digite o CPF do usuário: ")
        senha = input("Digite a senha do usuário: ")
        valor = float(input("Digite o valor a ser debitado: "))
        for usuario, conta in zip(appBanco['usuarios'], appBanco['contas']):
            if usuario['cpf'] == cpf and usuario['senha'] == senha:
                if conta['saldo'] >= valor:
                    conta['saldo'] -= valor
                    conta['transacoes'].append(
                        {'tipo': 'debito', 'valor': valor})
                    print('Valor debitado com sucesso')
                else:
                    print("Saldo insuficiente para debitar valor.")
            return
        print("\nCPF ou senha incorretos.")

    def depositar_valor():
        cpf = input("Digite o CPF do usuário: ")
        senha = input("Digite a senha do usuário: ")
        valor = float(input("Digite o valor a ser debitado: "))
        for usuario, conta in zip(appBanco['usuarios'], appBanco['contas']):
            if usuario['cpf'] == cpf and usuario['senha'] == senha:
                conta['saldo'] += valor
                conta['transacoes'].append(
                    {'tipo': 'deposito', 'valor': valor})
                print("Valor depositado com sucesso!")
            return
        print("\nCPF ou senha incorretos.")

    def extrato_da_conta():
        cpf = input("Digite o CPF do usuário: ")
        senha = input("Digite a senha do usuário: ")
        for usuario, conta in zip(appBanco['usuarios'], appBanco['contas']):
            if usuario['cpf'] == cpf and usuario['senha'] == senha:
                print(f"Extrato da conta de {usuario['nome']}:")
                print(f"Saldo atual: R$ {conta['saldo']:.2f}")
                print("Histórico de transações:")
                for transacao in conta['transacoes']:
                    if transacao['tipo'] == 'debito':
                        print(f"- Debitado R$ {transacao['valor']:.2f}")
                    else:
                        print(f"+ Depositado R$ {transacao['valor']:.2f}")
                return
        print("\nCPF ou senha incorretos.")

    def transferir_valor():
        origem = input("Digite o CPF da conta de origem: ")
        destino = input("Digite o CPF da conta de destino: ")
        valor = float(input("Digite o valor a ser transferido: "))

        conta_origem = None
        conta_destino = None

        for conta in appBanco['contas']:
            if conta['usuario']['cpf'] == origem:
                conta_origem = conta
            if conta['usuario']['cpf'] == destino:
                conta_destino = conta

        if conta_origem is None:
            print("Conta de origem não encontrada.")
            return
        if conta_destino is None:
            print("Conta de destino não encontrada.")
            return
        if conta_origem['saldo'] >= valor:
            conta_origem['saldo'] -= valor
            conta_destino['saldo'] += valor
            print("Transferência realizada com sucesso!")
        else:
            print("Saldo insuficiente para realizar a transferência.")

    def investimentos():
        cpf = input("Digite o CPF do usuário: ")
        senha = input("Digite a senha do usuário: ")
        for usuario, conta in zip(appBanco['usuarios'], appBanco['contas']):
            if usuario['cpf'] == cpf and usuario['senha'] == senha:
                print(f"Saldo atual: R$ {conta['saldo']:.2f}")
                for investimento in investimentos_menu:
                    print(investimento)
                decisao = input("Escolha uma opção de investimento: ")
                if decisao == '6':
                    return
                elif decisao in opcoes_investimentos:
                    valor_investido = float(input("Digite o valor a ser investido: "))
                    conta['saldo'] -= valor_investido
                    taxa_retorno = opcoes_investimentos[decisao]()
                    valor_retorno = calcular_retorno_investimento(valor_investido, taxa_retorno)
                    if(valor_retorno > 0):
                        print(f"Valor de retorno: R${valor_retorno:.2f}")
                        conta['saldo'] += valor_retorno
                    else:
                        print("Seu investimento não lucro, infelizmente você perdeu seu dinheiro")
                    return
                else:
                    print("Opção inválida. Digite um número válido.")
                    return
        print("\nCPF ou senha incorretos.")

    opcoes_menu = {
        '1': novo_cliente,
        '2': apagar_cliente,
        '3': listar_clientes,
        '4': debitar_valor,
        '5': depositar_valor,
        '6': extrato_da_conta,
        '7': transferir_valor,
        '8': investimentos
    }

    while True:
        exibir_menu()
        decisao = input("Escolha uma opção: ")

        if decisao == '9':
            break
        elif decisao in opcoes_menu:
            print()
            limpar_tela()
            opcoes_menu[decisao]()
        else:
            print("Opção inválida. Digite um número válido.")


if __name__ == "__main__":
    main()
