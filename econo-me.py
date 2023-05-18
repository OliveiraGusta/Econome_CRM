# Gustavo Rodrigues e Mateus Marana

import random
import datetime

def salvar_dados_arquivo(dados, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        for usuario, conta in zip(dados['usuarios'], dados['contas']):
            nome = usuario['nome']
            cpf = usuario['cpf']
            tipo_conta = conta['tipoConta']
            senha = usuario['senha']
            saldo = conta['saldo']
            transacoes = ','.join(str(t) for t in conta['transacoes'])
            linha = f"{nome},{cpf},{tipo_conta},{senha},{saldo},{transacoes}\n"
            arquivo.write(linha)

def carregar_dados_arquivo(nome_arquivo):
    dados = {
        'usuarios': [],
        'contas': []
    }
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            nome, cpf, tipo_conta, senha, saldo, transacoes = linha.strip().split(',')
            usuario = {'nome': nome, 'cpf': cpf, 'senha': senha}
            conta = {'saldo': float(saldo), 'tipoConta': tipo_conta, 'transacoes': []}
            if transacoes:
                transacoes = transacoes.split(';')
                for t in transacoes:
                    tipo, valor = t.split(':')
                    conta['transacoes'].append({'tipo': tipo, 'valor': float(valor)})
            dados['usuarios'].append(usuario)
            dados['contas'].append(conta)
    return dados


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
        retorno = random.randint(-1, 2)
        return valor_investido * (retorno * taxa_retorno)
    
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

        tipo_conta = input("\nTipo da Conta\n\nDigite 1 - Conta Premium\nDigite 2 - Conta Comum\nDigite o tipo da conta: ")
        if tipo_conta == '1':
            print('Cliente Premium!')
            tipo_conta = 'Premium'

        elif tipo_conta == '2':
            print('Cliente Comum!')
            tipo_conta = 'Comum'
        else:
            print("Opção inválida. Digite um número válido.")
            return
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
        VALOR_TARIFA_PREMIUM = 0.03
        VALOR_TARIFA_COMUM = 0.05

        tarifa_comum = valor * VALOR_TARIFA_COMUM
        tarifa_premium = valor * VALOR_TARIFA_PREMIUM
        conta_comum = valor + tarifa_comum
        conta_premium = valor + tarifa_premium
        
        for usuario, conta in zip(appBanco['usuarios'], appBanco['contas']):
            if usuario['cpf'] == cpf and usuario['senha'] == senha:
                if conta['saldo'] >= valor:
                    if conta['tipoConta'] == 'Premium':
                        conta['saldo'] -= conta_premium
                        conta['transacoes'].append({'tipo': 'debito', 'valor': conta_premium, 'tarifa': tarifa_premium })
                        print('Valor debitado com sucesso. Tarifa de R$%.2f cobrada' % tarifa_premium)
                    else:
                        conta['saldo'] -= conta_comum
                        conta['transacoes'].append({'tipo': 'debito', 'valor': conta_comum, 'tarifa': tarifa_comum})
                        print('Valor debitado com sucesso. Tarifa de R$%.2f cobrada' % tarifa_comum)
                    return
                else:
                    print("Saldo insuficiente para debitar valor.")
                    return

        print("\nCPF ou senha incorretos.")




    def depositar_valor():
        cpf = input("Digite o CPF do usuário: ")
        senha = input("Digite a senha do usuário: ")
        valor = float(input("Digite o valor a ser depositado: "))
        
        for usuario, conta in zip(appBanco['usuarios'], appBanco['contas']):
            if usuario['cpf'] == cpf and usuario['senha'] == senha:
                conta['saldo'] += valor
                conta['transacoes'].append({'tipo': 'deposito', 'valor': valor})
                print("Valor depositado com sucesso!")
                return
        
        print("\nCPF ou senha incorretos.")



    def extrato_da_conta():
        cpf = input("Digite o CPF do usuário: ")
        senha = input("Digite a senha do usuário: ")
        for usuario, conta in zip(appBanco['usuarios'], appBanco['contas']):
            if usuario['cpf'] == cpf and usuario['senha'] == senha:
                print(f"Extrato da conta de {usuario['nome']}:")
                print(f"Portador do CPF {usuario['cpf']}")
                print(f"Com a conta {conta['tipoConta']}")
                print("Histórico de transações:")
              
                for transacao in conta['transacoes']:
                    tipo = transacao['tipo']
                    valor = transacao['valor']
                    tarifa = transacao['tarifa']
                    if transacao['tipo'] == 'debito':
                        print(f"| {tipo:<8} | {valor:<14.2f} |")
                    else:
                        print(f"| {tipo:<8} | {valor:<14.2f} | R${tarifa:<14.2f}")
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
                        print(f"Valor de retorno: R${valor_retorno:.2f}")
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

    appBanco = carregar_dados_arquivo('dados_banco.txt')
    while True:
        exibir_menu()
        salvar_dados_arquivo(appBanco, 'dados_banco.txt')
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